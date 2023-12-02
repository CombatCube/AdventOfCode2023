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
        total = 0
        i = 0
        for line in file.readlines():
            i = i + 1
            impossible = False
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
                    break
            if not impossible:
                games.append(i)
        print(sum(games))



