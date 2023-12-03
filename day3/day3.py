import re


def search_for_symbol(start_ind, end_ind, prev_line, current_line, next_line):
    candidates = []

    candidate_start = start_ind - 1 if (start_ind > 0) else start_ind
    candidate_end = end_ind + 1 if (end_ind < len(current_line) - 1) else end_ind

    prev_candidate = prev_line[candidate_start:candidate_end]
    if re.search(r"[^.\d\n]", prev_candidate):
        return True
    current_candidate = current_line[candidate_start:candidate_end]
    if re.search(r"[^.\d\n]", current_candidate):
        return True
    next_candidate = next_line[candidate_start:candidate_end]
    if re.search(r"[^.\d\n]", next_candidate):
        return True
    return False


if __name__ == '__main__':
    with open("puzzle3") as file:
        schematic = [line for line in file.readlines()]
        total = 0
        for i in range(len(schematic)):
            prev_line = schematic[i - 1] if i > 0 else ""
            current_line = schematic[i]
            next_line = schematic[i + 1] if i < len(schematic) - 1 else ""
            # Find all integers in line
            results = re.finditer(r"\d+", current_line)
            for result in results:
                if search_for_symbol(result.start(), result.end(), prev_line, current_line, next_line):
                    total += int(result.group(0))
        print(total)
