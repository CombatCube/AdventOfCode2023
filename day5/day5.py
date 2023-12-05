import re

def parse_almanac(s: str):
    pass


def parse_seeds(s: str):
    return re.findall(r"\d+", s)
    pass

def parse_seeds_2(s: str):
    return [(int(match.group(1)), int(match.group(2))) for match in re.finditer(r"(\d+) (\d+)", s)]

class Map:
    def __init__(self, s:str):
        self.entries = {}
        lines = s.splitlines()
        for line in lines[1:]:
            entry = re.findall(r"\d+", line)
            self.entries[int(entry[1])] = [int(entry[0]), int(entry[2])]

    def lookup(self, num: int):
        result = None
        for entry in self.entries.items():
            range_length = entry[1][1]
            source_start = entry[0]
            dest_start = entry[1][0]
            if source_start <= num < source_start + range_length:
                result = dest_start + (num - source_start)
                return result
        return result if result is not None else num




def main():
    with open("puzzle5") as file:
        locations = []
        sections = file.read().split("\n\n")
        # seeds = parse_seeds(sections[0])
        seeds = parse_seeds_2(sections[0])
        seed_soil = Map(sections[1])
        soil_fert = Map(sections[2])
        fert_water = Map(sections[3])
        water_light = Map(sections[4])
        light_temp = Map(sections[5])
        temp_humid = Map(sections[6])
        humid_location = Map(sections[7])
        for seed_range in seeds:
            for seed in range(seed_range[0], seed_range[0] + seed_range[1]):
                soil = seed_soil.lookup(int(seed))
                fert = soil_fert.lookup(int(soil))
                water = fert_water.lookup(fert)
                light = water_light.lookup(water)
                temp = light_temp.lookup(light)
                humid = temp_humid.lookup(temp)
                location = humid_location.lookup(humid)
                locations.append(location)
        print(min(locations))


if __name__ == '__main__':
    main()