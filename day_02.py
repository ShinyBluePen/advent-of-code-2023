from functools import reduce
from operator import mul
from aocd import get_data

session = None

cube_counts = {"red": 12, "green": 13, "blue": 14}

data = get_data(session=session, year=2023, day=2).splitlines()


def parse_game(game: str) -> dict:
    """Parse useful information from a "cube game"."""
    parsed_game = {
        "id": 0,
        "revealed": [],
        "minimum set": [],
        "invalid": False,
    }
    game = game.removeprefix("Game ")

    # get game ID
    id = ""
    for c in game:
        if c != ":":
            id += c
        else:
            game = game.removeprefix(id + ":")
            break
    parsed_game["id"] = int(id)

    # get revealed sets of cubes and process relevant information
    min_r = 0
    min_g = 0
    min_b = 0
    for group in game.split(";"):
        revealed = []
        for cubes in group.split(","):
            amount, color = cubes.split()
            amount = int(amount)
            revealed.append((color, amount))
            # track "minimums"
            if color == "red" and amount > min_r: 
                min_r = amount
            if color == "green" and amount > min_g: 
                min_g = amount
            if color == "blue" and amount > min_b: 
                min_b = amount

            # disqualify sets who exceed threshholds
            if (color == "red" and amount > cube_counts["red"] or
                color == "green" and amount > cube_counts["green"] or
                color == "blue" and amount > cube_counts["blue"]
                ):
                parsed_game["invalid"] = True

        parsed_game["revealed"] = revealed

    parsed_game["minimum set"] = [min_r, min_g, min_b]

    return parsed_game


if __name__ == "__main__":
    valid_ids = []
    minimum_set_products = []
    for game in data:
        g = parse_game(game)
        if not g["invalid"]:
            valid_ids.append(g["id"])
        minimum_set_products.append(reduce(mul, g["minimum set"]))
    
    print(sum(minimum_set_products))
    print(sum(valid_ids))
