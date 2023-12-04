import re

def parse_card(s: str):
    strings = re.split(r":|\|", s)
    card_ind = int(re.findall(r"\d+", strings[0])[0]) - 1
    winning = {e for e in re.findall(r"\d+", strings[1])}
    actual = {e for e in re.findall(r"\d+", strings[2])}

    return card_ind, winning, actual


if __name__ == '__main__':
    with open("puzzle4") as file:
        puzzle = [line for line in file.readlines()]
        num_cards = [1 for i in range(len(puzzle))]
        total = 0
        for card in puzzle:
            card_ind, winning, actual = parse_card(card)
            matching = winning & actual
            num_matches = len(matching)
            total += num_cards[card_ind]
            if num_matches > 0:
                for i in range(num_matches):
                    if card_ind + 1 + i < len(puzzle):
                        num_cards[card_ind + 1 + i] += num_cards[card_ind]
        print(total)
