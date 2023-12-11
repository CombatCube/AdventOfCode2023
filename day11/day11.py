import re
import numpy


def main():
    total = 0
    with open("puzzle11") as file:
        start_array = numpy.asarray([[1 if c == '#' else 0 for c in (list(s.strip()))] for s in file.readlines()])
        empty_rows = list(numpy.nonzero(numpy.logical_not(numpy.any(start_array, 1))))[0]
        empty_cols = list(numpy.nonzero(numpy.logical_not(numpy.any(start_array, 0))))[0]
        coords = numpy.argwhere(start_array == 1)
        for a in range(len(coords)):
            for b in range(a, len(coords)):
                if a != b:
                    a_row = coords[a][0]
                    a_col = coords[a][1]
                    b_row = coords[b][0]
                    b_col = coords[b][1]

                    if a_row < b_row:
                        row_space = sum([a_row <= z < b_row for z in empty_rows])
                    else:
                        row_space = sum([b_row <= z < a_row for z in empty_rows])
                    if a_col < b_col:
                        col_space = sum([a_col <= z < b_col for z in empty_cols])
                    else:
                        col_space = sum([b_col <= z < a_col for z in empty_cols])

                    delta = abs(b_row - a_row) + col_space*999999 + abs(b_col - a_col) + row_space*999999
                    total += delta
                    pass
        print(total)


if __name__ == '__main__':
    main()
