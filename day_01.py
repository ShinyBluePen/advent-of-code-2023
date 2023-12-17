from aocd import get_data

session = None

data = get_data(session=session, year=2023, day=1).splitlines()
digit_words = "one two three four five six seven eight nine".split()
DIGITS = {word: digit for word, digit in zip(digit_words, range(1, len(digit_words)+1))}

def check_digit(string):
    if string[0].isdigit():
        return int(string[0])

    d = next(filter(string.startswith, DIGITS), None)
    return DIGITS.get(d, 0)

total1 = total2 = 0

for line in data:
    total1 += 10 * int(next(filter(str.isdigit, line)))
    total1 += int(next(filter(str.isdigit, line[::-1])))

    for i in range(len(line)):
        a = check_digit(line[i:])
        if a:
            break

    for i in range(len(line) - 1, -1, -1):
        b = check_digit(line[i:])
        if b:
            break
    total2 += 10 * a + b

print('Part 1:', total1)
print('Part 2:', total2)
