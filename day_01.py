from aocd import get_data

session = "53616c7465645f5f0f5451a354d16a73ff1278c469a8aa02d3cb039cbb083f50820e16f4f0da22934519af7dbaa242043137749bebd7f381a3b4314910b4641a"

data = get_data(session=session, year=2023, day=6).splitlines()

import re

digit_words = "one two three four five six seven eight nine".split()
digit_map = {word: str(digit) for word, digit in zip(digit_words, range(1, len(digit_words)+1))}
pattern = "(?=(" + "|".join(digit_words) + "|\\d))"

calibration_values = []
for line in data:
    digits = re.findall(pattern, line)
    for i, d in enumerate(digits):
        if d in digit_map:
            digits[i] = digit_map[d]
    calibration_values.append(int(digits[0] + digits[-1]))

print(len(calibration_values))
print(sum(calibration_values))







