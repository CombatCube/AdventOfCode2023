# AdventOfCode

import re

from typing import Tuple


def find_digits(s: str) -> Tuple[str, str]:
    matches = []
    matches += [(match.start(), match.group(0)) for match in re.finditer(r"\d", s)]
    matches += [(match.start(), "1") for match in re.finditer(r"one", s)]
    matches += [(match.start(), "2") for match in re.finditer(r"two", s)]
    matches += [(match.start(), "3") for match in re.finditer(r"three", s)]
    matches += [(match.start(), "4") for match in re.finditer(r"four", s)]
    matches += [(match.start(), "5") for match in re.finditer(r"five", s)]
    matches += [(match.start(), "6") for match in re.finditer(r"six", s)]
    matches += [(match.start(), "7") for match in re.finditer(r"seven", s)]
    matches += [(match.start(), "8") for match in re.finditer(r"eight", s)]
    matches += [(match.start(), "9") for match in re.finditer(r"nine", s)]
    matches.sort(key=lambda match: match[0])
    return (matches[0][1], matches[-1][1])


if __name__ == '__main__':
    with open("puzzleinput") as file:
        print(sum([int("".join(find_digits(line))) for line in file.readlines()]))
