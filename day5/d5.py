def parse_almanac(filename, keys_locations):
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
    almanac["seeds"] = [int(num) for num in lines[0][7:].rstrip("\n").split()]
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
        source_range = range(sd_map[1], sd_map[1] + sd_map[2])
        offset = 0
        for value in source_range:
            if target == value:
                destination = sd_map[0] + offset
            offset += 1

    return destination


keys = ("sample_input.txt", [3, 7, 12, 18, 22, 27, 31])
# keys = ("input", [3, 37, 57, 107, 142, 180, 211])
seed_almanac = parse_almanac(keys[0], keys[1])

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
keys = ["seeds", "seed-to-soil", "soil-to-fertilizer", "fertilizer-to-water", "water-to-light", "light-to-temperature", "temperature-to-humidity", "humidity-to-location"]
while key < len(keys):
    print(keys[key])
    s_to_d_mapping[keys[key]] = [source_to_destination(seed_almanac[keys[key]], i) for i in s_to_d_mapping[keys[key - 1]]]
    key += 1

print(s_to_d_mapping["humidity-to-location"])
print("lowest location:", min(s_to_d_mapping["humidity-to-location"]))