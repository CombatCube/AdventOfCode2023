import re
import numpy


def main():
    total = 0
    with open("puzzle11") as file:
        start_array = numpy.asarray([[1 if c == '#' else 0 for c in (list(s.strip()))] for s in file.readlines()])
        empty_rows = list(numpy.nonzero(numpy.logical_not(numpy.any(start_array, 0))))[0]
        empty_cols = list(numpy.nonzero(numpy.logical_not(numpy.any(start_array, 1))))[0]
        array = numpy.insert(start_array, obj=empty_rows, values=False, axis=1)
        array = numpy.insert(array, obj=empty_cols, values=False, axis=0)
        coords = numpy.argwhere(array == 1)
        for i in range(len(coords)):
            for j in range(i, len(coords)):
                if i != j:
                    total += (abs(coords[j][1] - coords[i][1]) + abs(coords[j][0] - coords[i][0]))
        print(total)


if __name__ == '__main__':
    main()
