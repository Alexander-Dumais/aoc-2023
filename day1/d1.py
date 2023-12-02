def read_calibrations(filename):
    lines = []
    with open(filename) as f:
        for line in f:
            lines.append(line.rstrip())
    
    return lines


def get_calibrations_nums(garbled, num_map):
    calibrated_vals = []
    for line in garbled:
        # Keep track of the earliest number and the latest number. These default vals should always be overwritten.
        earliest_index = (len(line), "invalid")
        latest_index   = (-1, "invalid")

        # This loop only updates the earliest or latest number if they come before or after the one stored.
        # The previous solution looped over the whole line for every key then sorted, keeping the earliest and latest.
        for key in num_map:
            index_of_key = line.find(key) 
            if  index_of_key > -1 and index_of_key < earliest_index[0]:
                earliest_index = (index_of_key, num_map[key])
            
            index_of_key = line.rfind(key)
            if  index_of_key > -1 and index_of_key > latest_index[0]:
                latest_index = (index_of_key, num_map[key])

        calibrated_vals.append(int(earliest_index[1]+latest_index[1]))

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
    cal_sum = sum(cal_vals)

    # line_num = 1
    # for val in cal_vals:
    #     print(f"line {line_num}: {val}")
    #     line_num += 1

    print(cal_sum)