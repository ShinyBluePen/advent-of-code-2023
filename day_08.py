from aocd import get_data
import math

session = "53616c7465645f5f0f5451a354d16a73ff1278c469a8aa02d3cb039cbb083f50820e16f4f0da22934519af7dbaa242043137749bebd7f381a3b4314910b4641a"


class Solution:
    def __init__(self):
        self.data = get_data(session=session, year=2023, day=8).splitlines()
        self.routes = self.parse_routes(self.data[2:])
        self.steps = 0

    @property
    def instructions(self):
        sequence = self.data[0]
        while True:
            for direction in sequence:
                yield direction

    def parse_routes(self, route_data: list[str]):
        parsed_routes = {}
        for row in route_data:
            node, route = row.split(" = ")
            parsed_routes[node] = (route[1:4], route[6:9])
        return parsed_routes

    def solve(self, flag):
        if flag == "puzzle 1":
            print("solution 1")
            self.node = "AAA"

            # loop instructions if "ZZZ" isn't found in first pass
            while self.node != "ZZZ":
                for inst in self.instructions:
                    if inst == "L":
                        self.node = self.routes[self.node][0]
                    if inst == "R":
                        self.node = self.routes[self.node][1]
                    self.steps += 1
                    if self.node == "ZZZ":
                        print(self.steps)
                        return

        if flag == "puzzle 2":
            print("solution 2")
            step_counts = []
            self.nodes = [node for node in self.routes.keys() if node[-1] == "A"]
            
            for node in self.nodes:
                current_node = node
                steps = 0
                inst = self.instructions
                while not current_node[-1] == "Z":
                    n_left, n_right = self.routes[current_node]
                    current_node = n_left if next(inst) == 'L' else n_right
                    steps += 1
                step_counts.append(steps)

            self.steps = math.lcm(*step_counts)
            print(self.steps)
                

if __name__ == '__main__':
    solution = Solution()
    solution.solve("puzzle 1")
    solution.solve("puzzle 2")