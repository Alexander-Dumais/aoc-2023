import numpy as np
import numpy.typing as npt


def read_schematic(filename):
    lines = []
    with open(filename) as f:
        for line in f:
            lines.append([str(c) for c in line.rstrip("\n")])

    return np.array(lines)


def check_if_part(schematic, num_indexes):

    valid_chars = "1234567890."
    for row, col in num_indexes:
        _slice = schematic[max(0, row-1):row+2, max(0, col-1):col+2]

        for char in _slice.flat:
            if char not in valid_chars:
                return True

    return False


def parse_part_numbers(schematic: np.ndarray):
    parts = []
    num_chars = ""
    num_chars_indexes = []

    total_numbers = 0
    total_parts = 0

    row = 0
    while row < schematic.shape[0]:
        col = 0
        while col < schematic.shape[1]:
            current_char = schematic[row, col]

            # If not digit, reset tracking of numbers
            if not np.char.isdigit(current_char):
                num_chars = ""
                num_chars_indexes = []

            # Otherwise it is a digit
            else:
                total_numbers += 1
                num_chars += current_char
                num_chars_indexes.append((row, col))
                while col+1 < schematic.shape[1] and np.char.isdigit(schematic[row, col+1]):
                    col += 1
                    current_char = schematic[row, col]
                    num_chars += current_char
                    num_chars_indexes.append((row, col))
                is_part = check_if_part(schematic, num_chars_indexes)
                if is_part:
                    total_parts += 1
                    parts.append(int(num_chars))
            col += 1
        row += 1

    # print(total_numbers, total_parts)
    return parts


def parse_part_nums(schematic, location):
    part_nums = []
    indexes_checked = []

    def consume_nums(schematic, location):
        r, c = location
        indexes_checked.append((r, c))
        if c < 0 or c >= schematic.shape[1] or schematic[r, c] not in "0123456789":
            return ""
        else:
            L = consume_nums(schematic, (r, c - 1)) if (r, c-1) not in indexes_checked else ""
            R = consume_nums(schematic, (r, c + 1)) if (r, c+1) not in indexes_checked else ""
            return L + schematic[r, c] + R

    # Given an index pair as a location, seek left and right to return the whole number
    row, col = location
    for i in range(row-1, row+2):
        for j in range(col-1, col+2):
            if schematic[i, j] in "0123456789" and (i, j) not in indexes_checked:
                # parse left and right for full number
                part_nums.append(int(consume_nums(schematic, (i, j))))

    while len(part_nums) < 2:
        part_nums.append(0)
    print(part_nums)
    return part_nums


def parse_for_gears(schematic: np.ndarray):
    gear_ratios = []

    # Find a symbol
    for row in range(schematic.shape[0]):
        for col in range(schematic.shape[1]):
            char = schematic[row, col]
            if char not in "0123456789.":  # Symbol found
                # search for numbers adjacent to a symbol
                # If there are two numbers adjacent to the symbol, multiply them and track the result as a gear ratio
                num1, num2 = parse_part_nums(schematic, (row, col))
                gear_ratios.append(num1 * num2)  # This result is 0 if there's only one part near a symbol

    return gear_ratios


schematic = read_schematic("input")

# First star
# engine_parts = parse_part_numbers(schematic)
# print(sum(engine_parts))

# Second star
gears = parse_for_gears(schematic)
sum_of_gear_ration = sum(gears)
print(sum_of_gear_ration)
