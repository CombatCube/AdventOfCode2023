import re


class Game:
    id = 0
    red = 0
    green = 0
    blue = 0

    def __init__(self, id, red, green, blue):
        self.id = id
        self.red = int(red)
        self.green = int(green)
        self.blue = int(blue)


if __name__ == '__main__':
    with open("puzzle2") as file:
        games = []
        powers = []
        total = 0
        i = 0
        for line in file.readlines():
            i = i + 1
            impossible = False
            max_red, max_green, max_blue = 0, 0, 0
            game_id, gamelist = line.split(":")
            grab_strings = [game.strip() for game in (gamelist.split(";"))]
            for grab in grab_strings:
                red_matches = re.search(r"(\d*) red", grab)
                red = int(red_matches.group(1)) if red_matches else 0
                green_matches = re.search(r"(\d*) green", grab)
                green = int(green_matches.group(1)) if green_matches else 0
                blue_matches = re.search(r"(\d*) blue", grab)
                blue = int(blue_matches.group(1)) if blue_matches else 0
                if red > 12 or green > 13 or blue > 14:
                    impossible = True
                max_red = max(max_red, red)
                max_green = max(max_green, green)
                max_blue = max(max_blue, blue)
            if not impossible:
                games.append(i)
            powers.append(max_red * max_green * max_blue)
        print(sum(games))
        print(sum(powers))
