import re


schematic = []
gears = dict()


def search_for_symbol(start_ind, end_ind, line_length, prev_line_ind, current_line_ind, next_line_ind):
    candidates = []

    candidate_start = start_ind - 1 if (start_ind > 0) else start_ind
    candidate_end = end_ind + 1 if (end_ind < line_length - 1) else end_ind

    prev_candidate = schematic[prev_line_ind][candidate_start:candidate_end] if prev_line_ind is not None else ""
    if re.search(r"[^.\d\n]", prev_candidate):
        return True
    current_candidate = schematic[current_line_ind][candidate_start:candidate_end]
    if re.search(r"[^.\d\n]", current_candidate):
        return True
    next_candidate = schematic[next_line_ind][candidate_start:candidate_end] if next_line_ind is not None else ""
    if re.search(r"[^.\d\n]", next_candidate):
        return True
    return False


def search_for_gear(prev_line_ind, current_line_ind, next_line_ind):
    # Find all integers in line
    results = re.finditer(r"\d+", schematic[current_line_ind])
    for result in results:
        candidate_start = result.start() - 1 if (result.start() > 0) else result.start()
        candidate_end = result.end() + 1 if (result.end() < len(schematic[0]) - 1) else result.end()

        if prev_line_ind is not None:
            check_line_for_gear(candidate_end, candidate_start, prev_line_ind, result)

        check_line_for_gear(candidate_end, candidate_start, current_line_ind, result)

        if next_line_ind is not None:
            check_line_for_gear(candidate_end, candidate_start, next_line_ind, result)


def check_line_for_gear(candidate_end, candidate_start, line_ind, result):
    line_gears = re.finditer(r"\*", schematic[line_ind])
    for gear in line_gears:
        if candidate_start <= gear.start() < candidate_end:
            gear_coords = (gear.start(), line_ind)
            if gear_coords not in gears:
                gears[gear_coords] = [int(result.group(0))]
            else:
                gears[gear_coords] += [int(result.group(0))]


if __name__ == '__main__':
    with open("puzzle3") as file:
        schematic = [line for line in file.readlines()]
        total = 0
        for i in range(len(schematic)):
            prev_line_ind = i - 1 if i > 0 else None
            current_line_ind = i
            next_line_ind = i + 1 if i < len(schematic) - 1 else None
            search_for_gear(prev_line_ind, current_line_ind, next_line_ind)
        for gear in gears:
            if len(gears[gear]) == 2:
                total += gears[gear][0] * gears[gear][1]
        print(total)
