import math


def read_input(file_name):
    with open(file_name, 'r') as f:
        times = [int(num) for num in f.readline().rstrip()[9:].split()]
        distances = [int(num) for num in f.readline().rstrip()[9:].split()]
    return times, distances


def part_a(file_name):
    races = zip(*read_input(file_name))
    wins = []
    for time, distance in races:
        winning_races = 0
        for i in range(1, time):
            distance_from_i = i * (time-i)
            if distance_from_i > distance:
                winning_races += 1
        wins.append(winning_races)

    print(f"part A wins: {wins}")
    print(f"part A answer: {math.prod(wins)}")


def part_b(file_name):
    times, distances = read_input(file_name)
    time = int("".join([str(t) for t in times]))
    distance = int("".join([str(d) for d in distances]))

    wins = []
    winning_races = 0
    for i in range(1, time):
        distance_from_i = i * (time-i)
        if distance_from_i > distance:
            winning_races += 1
    wins.append(winning_races)

    print(f"part B wins: {wins}")
    print(f"part B answer: {math.prod(wins)}")


# part_a("sample_input")
part_b("sample_input") #41513103