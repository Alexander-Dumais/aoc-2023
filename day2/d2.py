from typing import List, Dict


def read_games(filename):
    lines = []
    with open(filename) as f:
        for line in f:
            lines.append(line[5:].rstrip("\n"))

    return lines


def decode_games(lines):
    """
    Creates a map where the game number is the key and the hands are the values
    """
    game_map = {}

    for game in lines:
        game_num, games = game.split(": ")
        hands = games.split("; ")
        game_map[int(game_num)] = hands

    return game_map


def count_colours(blocks):
    counts = {"red": 0, "green": 0, "blue": 0}

    for block in blocks:
        count, colour = block.split()
        counts[colour] = int(count)

    return counts


def all_valid_games(game_map: Dict[int, List[str]], config: Dict[str, int]):
    valid_games = []
    red_lim, green_lim, blue_lim = config.values()

    for game_id, hands in game_map.items():
        invalid = False
        # print(f"handiling game {game_id}:")
        for hand in hands:
            hand_colours = count_colours(hand.split(","))
            # print(hand_colours)
            if hand_colours["red"] > red_lim or hand_colours["green"] > green_lim or hand_colours["blue"] > blue_lim:
                invalid = True
                break
        if not invalid:
            valid_games.append(game_id)
        # print()

    return valid_games


def max_of_each_game(game_map: Dict[int, List[str]]):
    max_cubes_sums = []

    for game_id, hands in game_map.items():
        max_colours = {"red": 0, "green": 0, "blue": 0}
        for hand in hands:
            hand_colours = count_colours(hand.split(","))
            for colour, count in hand_colours.items():
                max_colours[colour] = max(count, max_colours[colour])  # Update new bhighest count for that colour

        max_cubes_sums.append(max_colours["red"] * max_colours["green"] * max_colours["blue"])

    return max_cubes_sums


if __name__ == "__main__":
    game_map = decode_games(read_games("input"))
    configuration = {"red": 12, "green": 13, "blue": 14}  # The day2-1 configuration

    valid_games = all_valid_games(game_map, configuration)
    print(f"Sum of valid game numbers: {sum(valid_games)}")

    max_cubes = max_of_each_game(game_map)
    print(f"Sum of product of max cube counts to make for a valid config: {sum(max_cubes)}")
