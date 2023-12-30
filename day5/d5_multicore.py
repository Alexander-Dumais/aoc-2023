import time
from multiprocessing import Pool

from helpers.helpers import pairs


def parse_almanac(filename, keys_locations, pair_seeds=False):
    almanac = {"seeds": [],
               "seed-to-soil": [],
               "soil-to-fertilizer": [],
               "fertilizer-to-water": [],
               "water-to-light": [],
               "light-to-temperature": [],
               "temperature-to-humidity": [],
               "humidity-to-location": []}

    with open(filename, 'r') as f:
        lines = f.readlines()

    seeds = [int(num) for num in lines[0][7:].rstrip("\n").split()]
    if pair_seeds:
        # pair the seeds up instead if doing part 2
        seeds = pairs([int(num) for num in lines[0][7:].rstrip("\n").split()])

    almanac["seeds"] = seeds
    almanac["seed-to-soil"] = [[int(num) for num in line.rstrip("\n").split()] for line in
                               lines[keys_locations[0]:keys_locations[1] - 1] if not line == "\n"]
    almanac["soil-to-fertilizer"] = [[int(num) for num in line.rstrip("\n").split()] for line in
                                     lines[keys_locations[1]:keys_locations[2] - 1] if not line == "\n"]
    almanac["fertilizer-to-water"] = [[int(num) for num in line.rstrip("\n").split()] for line in
                                      lines[keys_locations[2]:keys_locations[3] - 1] if not line == "\n"]
    almanac["water-to-light"] = [[int(num) for num in line.rstrip("\n").split()] for line in
                                 lines[keys_locations[3]:keys_locations[4] - 1] if not line == "\n"]
    almanac["light-to-temperature"] = [[int(num) for num in line.rstrip("\n").split()] for line in
                                       lines[keys_locations[4]:keys_locations[5] - 1] if not line == "\n"]
    almanac["temperature-to-humidity"] = [[int(num) for num in line.rstrip("\n").split()] for line in
                                          lines[keys_locations[5]:keys_locations[6] - 1] if not line == "\n"]
    almanac["humidity-to-location"] = [[int(num) for num in line.rstrip("\n").split()] for line in
                                       lines[keys_locations[6]:] if not line == "\n"]

    return almanac


def source_to_destination(s_to_d, target):
    """
    If the source range contains the target, return the location in the destination range
     where the target was found. If no target is found, the destination is the target.
    """
    destination = target
    for sd_map in s_to_d:
        start = sd_map[1]
        end = sd_map[1] + sd_map[2]
        if start <= target < end:
            destination = sd_map[0] + target - start

    return destination


def parta():
    input_and_keys = ("sample_input.txt", [3, 7, 12, 18, 22, 27, 31])
    # input_and_keys = ("input", [3, 37, 57, 107, 142, 180, 211])
    seed_almanac = parse_almanac(input_and_keys[0], input_and_keys[1], pair_seeds=False)

    # new mapping for simplicity
    s_to_d_mapping = {
        "seeds": seed_almanac["seeds"],
        "seed-to-soil": [],
        "soil-to-fertilizer": [],
        "fertilizer-to-water": [],
        "water-to-light": [],
        "light-to-temperature": [],
        "temperature-to-humidity": [],
        "humidity-to-location": []}

    # Process of calculating source to destination for each starting seed
    key = 1
    input_and_keys = ["seeds", "seed-to-soil", "soil-to-fertilizer", "fertilizer-to-water", "water-to-light",
                      "light-to-temperature", "temperature-to-humidity", "humidity-to-location"]
    while key < len(input_and_keys):
        print(input_and_keys[key])
        s_to_d_mapping[input_and_keys[key]] = [source_to_destination(seed_almanac[input_and_keys[key]], i) for i in
                                               s_to_d_mapping[input_and_keys[key - 1]]]
        key += 1

    # Part A complete
    print(s_to_d_mapping["humidity-to-location"])
    print("lowest location:", min(s_to_d_mapping["humidity-to-location"]))
    print("PartA Done\n\n")

def partb_parallel(args):
    # partb_parallel(almanac, this_range)
    input_and_keys = ["seed-to-soil", "soil-to-fertilizer", "fertilizer-to-water", "water-to-light",
                      "light-to-temperature", "temperature-to-humidity", "humidity-to-location"]
    _best_so_far = 100000000000000000000

    start, steps = args[0]
    almanac = args[1]
    print(f"Checking {start} to {start + steps}:")
    start_time = time.time()
    for seed in range(start, start + steps):
        target = seed
        for step in input_and_keys:
            target = source_to_destination(almanac[step], target)
            if target < _best_so_far:
                _best_so_far = target
                print(f"new best location: {_best_so_far}")
    print(f"Time taken: {time.time() - start_time}")


def partb():
    # input_and_keys = ("sample_input.txt", [3, 7, 12, 18, 22, 27, 31])
    input_and_keys = ("input", [3, 37, 57, 107, 142, 180, 211])
    seed_almanac = parse_almanac(input_and_keys[0], input_and_keys[1], pair_seeds=True)

    partb_parallel_args = list(zip(list(seed_almanac["seeds"]), [seed_almanac] * 10))

    with Pool(10) as p:
        p.map(partb_parallel, partb_parallel_args)


if __name__ == "__main__":
    # parta()
    partb()
