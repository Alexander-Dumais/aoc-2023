
def read_calibrations(filename):
    lines = []
    with open(filename) as f:
        for line in f:
            lines.append(line.rstrip())
    
    return lines



def get_calibrations_nums(garbled, num_map):
    calibrated_vals = []
    for line in garbled:

        indexes_of_nums_firsts = {}
        indexes_of_nums_lasts = {}

        for key in num_map:
            index_of_key = line.find(key)
            if  index_of_key > -1:
                indexes_of_nums_firsts[index_of_key] = num_map[key]
            
            index_of_key = line.rfind(key)
            if  index_of_key > -1:
                indexes_of_nums_lasts[index_of_key] = num_map[key]

        sorted_firsts = sorted(indexes_of_nums_firsts)
        first = indexes_of_nums_firsts[sorted_firsts[0]]
        sorted_lasts = sorted(indexes_of_nums_lasts, reverse=True)
        last = indexes_of_nums_lasts[sorted_lasts[0]]

        calibrated_vals.append(int(first+last))

    return calibrated_vals

if __name__ == "__main__":

    num_map = {"one":   "1",
           "two":   "2",
           "three": "3",
           "four":  "4",
           "five":  "5",
           "six":   "6",
           "seven": "7",
           "eight": "8",
           "nine":  "9",
           "1": "1",
           "2": "2",
           "3": "3",
           "4": "4",
           "5": "5",
           "6": "6",
           "7": "7",
           "8": "8",
           "9": "9"
           }

    cals = read_calibrations("input")
    cal_vals = get_calibrations_nums(cals, num_map)

    line_num = 1
    for val in cal_vals:
        print(f"line {line_num}: {val}")
        line_num += 1

    cal_sum = sum(cal_vals)

    print(cal_sum)