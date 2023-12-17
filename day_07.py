from aocd import get_data

session = None

_hand_ranking = ("five of a kind.four of a kind.full house.three of a kind.two pair.two of a kind.high card").split(".")
_cards = "2 3 4 5 6 7 8 9 T J Q K A".split()
HAND_RANKING = {rank: value for rank, value in zip(_hand_ranking, range(7, 0, -1))}
CARDS = {card: value for card, value in zip(_cards, range(2, 15))}

class CamelHand:
    def __init__(self, hand, bid, wilds=None):
        self.wilds = wilds
        self.hand = self.parse(hand)
        self.bid = int(bid)
        self.rank = 0

        for is_rank in self.ranks():
            if is_rank():
                break

    def parse(self, hand: str) -> dict:
        """Extract useful information out of the raw hand.
        
        Return a dictionary of that information with the values:
        "score": int, 
        "pairs": list[int],
        "hand": list[str]
        """
        # all wild hand edge case
        if hand == "JJJJJ":
            return {"score": 7, "pairs": [5], "hand": hand, "kickers": [1, 1, 1, 1, 1]}
        
        # convert wilds to most highest value common card in hand
        wild_hand = []
        most_common = max(set(hand.replace("J", "")), key=lambda x: (hand.count(x), x))
        for card in hand:
            if card == self.wilds:
                wild_hand.append(most_common)
            else:
                wild_hand.append(card)

        pairs = sorted([wild_hand.count(i) for i in set(wild_hand)], reverse=True)
        score = 0
        hand = hand
        kickers = [CARDS[card] for card in hand]
        
        return {"score": score, "pairs": pairs, "hand": hand, "kickers": kickers}

    def ranks(self) -> list:
        """Return a list of single-hand ranking functions."""
        return [self.is_five_kind,
                self.is_four_kind, 
                self.is_full_house,
                self.is_three_kind, 
                self.is_two_pair,
                self.is_two_kind, 
                self.is_high_card,]

    def is_five_kind(self) -> bool:
        """Check if hand is a five of a kind."""
        if self.hand["pairs"] == [5]:
            self.hand["score"] = HAND_RANKING["five of a kind"]
            return True
        return False

    def is_four_kind(self) -> bool:
        """Check if hand is a four of a kind."""
        if self.hand["pairs"] == [4, 1]:
            self.hand["score"] = HAND_RANKING["four of a kind"]
            return True
        return False

    def is_full_house(self) -> bool:
        """Check if hand is a full house."""
        if self.hand["pairs"] == [3, 2]:
            self.hand["score"] = HAND_RANKING["full house"]
            return True
        return False

    def is_three_kind(self) -> bool:
        """Check if hand is a three of a kind."""
        if self.hand["pairs"] == [3, 1, 1]:
            self.hand["score"] = HAND_RANKING["three of a kind"]
            return True
        return False

    def is_two_pair(self) -> bool:
        """Check if hand is a two pair."""
        if self.hand["pairs"] == [2, 2, 1]:
            self.hand["score"] = HAND_RANKING["two pair"]
            return True
        return False

    def is_two_kind(self) -> bool:
        """Check if hand is a two of a kind."""
        # print("pair")
        if self.hand["pairs"] == [2, 1, 1, 1]:
            self.hand["score"] = HAND_RANKING["two of a kind"]
            return True
        return False

    def is_high_card(self) -> bool:
        """Check if hand is high card."""
        # print("high card")
        if self.hand["pairs"] == [1, 1, 1, 1, 1]:
            self.hand["score"] = HAND_RANKING["high card"]
            return True
        return False


class Solution:
    def __init__(self):
        self.data = get_data(session=session, year=2023, day=7).splitlines()
        self.data = [line.split() for line in self.data]

    def solve(self, flag):
        hands = []
        total_winnings = 0
        if flag == "puzzle 1":
            CARDS["J"] = 11
            wilds = None
            print("solution 1")

        if flag == "puzzle 2":
            CARDS["J"] = 1
            wilds = "J"
            print("solution 2")
            
        for hand, bid in self.data:
            hands.append(CamelHand(hand, bid, wilds))

        hands = sorted(hands, key=lambda hand: hand.hand["kickers"])
        hands = sorted(hands, key=lambda hand: hand.hand["score"])

        for rank, hand in enumerate(hands, 1):
            hand.rank = rank
            total_winnings += hand.bid * hand.rank

        print(total_winnings)


if __name__ == '__main__':
    solution = Solution()
    solution.solve("puzzle 1")
    solution.solve("puzzle 2")
