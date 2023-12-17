from aocd import get_data

session = "53616c7465645f5f0f5451a354d16a73ff1278c469a8aa02d3cb039cbb083f50820e16f4f0da22934519af7dbaa242043137749bebd7f381a3b4314910b4641a"

class Card:
    def __init__(self, numbers, winning_numbers):
        self.count = 1
        self.numbers = numbers.split()
        self.winning_numbers = winning_numbers.split()
        self.points = 0
        self.winners_total = 0
        self.calc_points()

    def copy_winners(self, cards_to_copy):
        for card in cards_to_copy:
            card.count += self.count
        
    def calc_points(self):
        for number in self.winning_numbers:
            for mine in self.numbers:
                if number == mine:
                    if self.points:
                        self.points = self.points*2
                    else:
                        self.points = 1
                    self.winners_total += 1
                    break

class Solution:
    def __init__(self):
        self.data = get_data(session=session, year=2023, day=4).splitlines()


    def solve(self):
        cards = [''.join(x.split(':')[1:]) for x in self.data]
        cards = [x.split('|') for x in cards]
        card_objs = [Card(card, winners) for winners, card in cards]

        for idx, card in enumerate(card_objs,1):
            card.copy_winners(card_objs[idx:idx+card.winners_total])

        print(f'Part 1: {sum([card.points for card in card_objs])}')
        print(f'Part 2: {sum([card.count for card in card_objs])}')

if __name__ == '__main__':
    solution = Solution()
    solution.solve()