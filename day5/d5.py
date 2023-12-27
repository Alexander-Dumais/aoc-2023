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





sample_keys = [3, 7, 12, 18, 22, 27, 31]
real_keys = [3, 37, 57, 107, 142, 180, 211]
seed_almanac = parse_almanac('sample_input.txt', sample_keys)
# seed_almanac = parse_almanac("input.txt", real_keys)

for k,v in seed_almanac.items():
    print(k, v)
