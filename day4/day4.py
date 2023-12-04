import re

def parse_card(s: str):
    strings = re.split(r":|\|", s)
    card_ind = {e for e in re.findall(r"\d+", strings[0])}
    winning = {e for e in re.findall(r"\d+", strings[1])}
    actual = {e for e in re.findall(r"\d+", strings[2])}

    return card_ind, winning, actual


if __name__ == '__main__':
    with open("puzzle4") as file:
        puzzle = [line for line in file.readlines()]
        total = 0
        for card in puzzle:
            card_ind, winning, actual = parse_card(card)
            matching = winning & actual
            if len(matching) > 0:
                total += 2 ** (len(matching) - 1)
        print(total)