from aocd import get_data

session = None


class Solution:
    def __init__(self):
        self.data = get_data(session=session, year=2023, day=9).splitlines()

    def solve(self, flag):
        if flag == "puzzle 1":
            for sequence in self.data:
                patterns = [[int(n) for n in sequence.split()]]
                while not all(value - value == 0 for value in patterns[-1]) == 0:
                    patterns.append([val - patterns[-1][i-1] for i, val in enumerate(patterns[-1][1:])] + [0])
                
                for pattern in patterns[::-1]:
                    print(pattern)
                break


        if flag == "puzzle 2":
            print("solution 2")
                

if __name__ == '__main__':
    solution = Solution()
    solution.solve("puzzle 1")
    # solution.solve("puzzle 2")
