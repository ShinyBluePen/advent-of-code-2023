from aocd import get_data

session = None


class Race:
    def __init__(self, time, distance_record):
        self.time = time
        self.distance_record = distance_record
    
    @property
    def ways_to_win(self):
        winning_time_1, winning_time_2 = 0, 0
        for t in range(self.time+1):
            if t * (self.time - t) > self.distance_record:
                # print(t)
                winning_time_1 = t
                break
        for t in range(self.time, 0, -1):
            if t * (self.time - t) > self.distance_record:
                winning_time_2 = t
                break

        return len([t for t in range(winning_time_1, winning_time_2+1)])


class Solution:
    def __init__(self):
        self.data = get_data(session=session, year=2023, day=6).splitlines()
        self.times = self.data[0].removeprefix("Time:").strip()
        self.distance_records = self.data[1].removeprefix("Distance:").strip()

    def solve(self, flag):
        if flag == "puzzle 1":
            print("solution 1")
            self.times = self.times.split()
            self.distance_records = self.distance_records.split()
            self.ways_to_break_record = []

        if flag == "puzzle 2":
            print("solution 2")
            self.times = ["".join(self.times)]
            self.distance_records = ["".join(self.distance_records)]
            self.ways_to_break_record = []

        for time, distance in zip(self.times, self.distance_records):
            race = Race(int(time), int(distance))
            self.ways_to_break_record.append(race.ways_to_win)

        if flag == "puzzle 1":
            wbr_product = self.ways_to_break_record[0]
            for n in self.ways_to_break_record[1:]:
                wbr_product *= n
            print(wbr_product)
        else:
            print(race.ways_to_win)


if __name__ == '__main__':
    solution = Solution()
    solution.solve("puzzle 1")
    solution.solve("puzzle 2")
