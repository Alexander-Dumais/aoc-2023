import numpy as np
import numpy.typing as npt


def print_engine(schematic):
    for line in schematic:
        for char in line:
            print(char, end="")
        print()


def read_schematic(filename):
    """
    Split the lines up into individual characters and insert them into a numpy array
    """
    lines = []
    with open(filename) as f:
        for line in f:
            lines.append([c for c in line.rstrip("\n")])

    return np.array(lines)


def parse_numbers_and_symbols(schematic: np.ndarray[str]):
    number_locations = {}
    symbol_locations = {}

    num_mapped_to_indexes = {}

    for row in range(schematic.shape[0]):
        for col in range(schematic.shape[1]):
            char = schematic[row, col]
            if np.char.isdigit(char):
                number_locations[(row, col)] = char
            elif char == ".":
                pass
            else:
                symbol_locations[(row, col)] = char

    print(number_locations)


def check_if_part(schematic, num_indexes):

    valid_chars = "1234567890."
    for row, col in num_indexes:
        slice = schematic[max(0, row-1):row+2, max(0, col-1):col+2]

        for char in slice.flat:
            if char not in valid_chars:
                return True

    return False


def parse_part_numbers(schematic: np.ndarray[np.str_]):
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

    print(total_numbers, total_parts)
    return parts


schematic = read_schematic("input")

engine_parts = parse_part_numbers(schematic)
print(sum(engine_parts))
