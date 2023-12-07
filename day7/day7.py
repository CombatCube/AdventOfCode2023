import re
from functools import cmp_to_key

RANK_ORDER = {
    "A": 1,
    "K": 2,
    "Q": 3,
    "T": 4,
    "9": 5,
    "8": 6,
    "7": 7,
    "6": 8,
    "5": 9,
    "4": 10,
    "3": 11,
    "2": 12,
    "J": 13
}

HAND_ORDER = {
    "FIVE_OF_A_KIND": 1,
    "FOUR_OF_A_KIND": 2,
    "FULL_HOUSE": 3,
    "THREE_OF_A_KIND": 4,
    "TWO_PAIR": 5,
    "ONE_PAIR": 6,
    "HIGH_CARD": 7
}


def hand_type(cards):
    card_count = {}
    for card in cards:
        if card_count.get(card) is None:
            card_count[card] = 1
        else:
            card_count[card] += 1
    keys = card_count.keys()
    values = card_count.values()
    jokers = card_count["J"] if card_count.get("J") is not None else 0
    if 5 in values:                     # AAAAA
        return "FIVE_OF_A_KIND"
    elif 4 in values:                   # AAAAB
        if jokers == 1:                 # AAAAJ
            return "FIVE_OF_A_KIND"
        if jokers == 4:                 # AJJJJ
            return "FIVE_OF_A_KIND"
        return "FOUR_OF_A_KIND"         # AAAAB
    elif 3 in values:                   # AAABC
        if jokers == 3:                 # ABJJJ
            return "FOUR_OF_A_KIND"
        if jokers == 2:                 # AAAJJ
            return "FIVE_OF_A_KIND"
        if jokers == 1:                 # AAABJ
            return "FOUR_OF_A_KIND"
        if 2 in values:                 # AAABB
            return "FULL_HOUSE"
        return "THREE_OF_A_KIND"        # AAABC
    elif len(keys) == 3:                # AABBC
        if jokers == 2:                 # AAJJB
            return "FOUR_OF_A_KIND"
        if jokers == 1:                 # AABBJ
            return "FULL_HOUSE"
        return "TWO_PAIR"               # AABBC
    elif len(keys) == 4:                # AABCD
        if jokers == 2:                 # ABCJJ
            return "THREE_OF_A_KIND"
        if jokers == 1:                 # AABCJ
            return "THREE_OF_A_KIND"
        return "ONE_PAIR"               # AABCD
    elif jokers == 1:
        return "ONE_PAIR"               # ABCDJ
    return "HIGH_CARD"                  # ABCDE


class Hand:
    def __init__(self, cards: str, bid: int):
        self.cards = cards
        self.bid = bid
        self.hand_type = hand_type(cards)
        pass


def parse_hand(line: str):
    match = re.match(r"(\w+) (\d+)", line)
    return Hand(match.group(1), int(match.group(2)))


def comparator(x, y):
    ret = HAND_ORDER[y.hand_type] - HAND_ORDER[x.hand_type]
    if ret == 0:
        ret = RANK_ORDER[y.cards[0]] - RANK_ORDER[x.cards[0]]
    if ret == 0:
        ret = RANK_ORDER[y.cards[1]] - RANK_ORDER[x.cards[1]]
    if ret == 0:
        ret = RANK_ORDER[y.cards[2]] - RANK_ORDER[x.cards[2]]
    if ret == 0:
        ret = RANK_ORDER[y.cards[3]] - RANK_ORDER[x.cards[3]]
    if ret == 0:
        ret = RANK_ORDER[y.cards[4]] - RANK_ORDER[x.cards[4]]
    return ret

def main():
    with open("puzzle7") as file:
        hands = []
        lines = file.readlines()
        for line in lines:
            hands.append(parse_hand(line))
        sorted_hands = sorted(hands, key=cmp_to_key(comparator))
        hand_rank = 0
        total = 0
        for hand in sorted_hands:
            hand_rank += 1
            total += hand.bid * hand_rank
        print(total)


if __name__ == '__main__':
    main()