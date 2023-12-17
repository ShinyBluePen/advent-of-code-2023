from aocd import get_data

session = "53616c7465645f5f0f5451a354d16a73ff1278c469a8aa02d3cb039cbb083f50820e16f4f0da22934519af7dbaa242043137749bebd7f381a3b4314910b4641a"

seed_inputs, *data_blocks = get_data(session=session, year=2023, day=5).splitlines()

seed_inputs = list(map(int, seed_inputs.split(":")[1].split()))
seeds = []

for i in range(0, len(seed_inputs), 2):
    seeds.append([seed_inputs[i], seed_inputs[i] + seed_inputs[i + 1]])

for data_block in data_blocks:
    ranges_list = []
    for line in data_block.splitlines()[1:]:
        ranges_list.append(list(map(int, line.split())))

    new_seeds = []

    while len(seeds) > 0:
        start, end = seeds.pop()

        for destination, source, length in ranges_list:
            overlap_start = max(start, source)
            overlap_end = min(end, source + length)

            if overlap_start < overlap_end:
                new_seeds.append(
                    [overlap_start - source + destination, overlap_end - source + destination])
                if overlap_start > start:
                    seeds.append([start, overlap_start])
                if overlap_end < end:
                    seeds.append([overlap_end, end])
                break
        else:
            new_seeds.append([start, end])

    seeds = new_seeds

ans = min(seeds)[0]
print(ans)
