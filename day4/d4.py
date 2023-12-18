
def read_input(file_name, ignore_chars):
    scratch_cards = []
    with (open(file_name, "r") as f):
        for line in f:
            line = line[ignore_chars:]
            winning_nums, scratch_nums = line.split("|")
            card = {"winning": [int(num) for num in winning_nums.split()],
                    "numbers": [int(num) for num in scratch_nums.split()]}
            scratch_cards.append(card)

    # print(card)
    # lines will be a list of dictionaries. Each record contains 'winning' and 'numbers'
    return scratch_cards


def winning_scores(cards):
    card_scores = []
    for card in cards:
        count_winning_nums = 0
        for num in card["numbers"]:
            if num in card["winning"]:
                count_winning_nums += 1
        card_scores.append(2**(count_winning_nums-1) if count_winning_nums > 0 else 0)

    return card_scores

def multiples_of_cards(cards):
    multiples = {}
    for i in range(len(cards)):
        multiples[i+1] = 0

    for card_num in range(1, len(cards)+1):
        count_winning_nums = 0
        current_card = cards[card_num-1]
        for num in current_card["numbers"]:
            if num in current_card["winning"]:
                count_winning_nums += 1


        multiples[card_num] = multiples[card_num] + 1
        keys = multiples.keys()
        while count_winning_nums > 0:
            if card_num + count_winning_nums in keys:
                multiples[card_num + count_winning_nums] = multiples[card_num + count_winning_nums] + 1
            count_winning_nums -= 1


    return multiples

def expanded_cards(cards):
    new_card_set = cards.copy()

    # card_iter = iter(new_card_set)
    # card = next(card_iter)
    # while card:

    for card_num in range(1, len(cards)+1):
        count_winning_nums = 0
        current_card = cards[card_num-1]
        for num in current_card["numbers"]:
            if num in current_card["winning"]:
                count_winning_nums += 1

        new_card_set.append(card_num)
        while count_winning_nums > 0:
            if card_num + count_winning_nums < len(cards):
                new_card_set.append(card_num + count_winning_nums)
            count_winning_nums -= 1

    return new_card_set


scratch_cards = read_input("example_input.txt", ignore_chars=7)  # ignore_chars = 10 for real input

# Part 1
scores = winning_scores(scratch_cards)
print("scores:", scores)
print("total_score:", sum(scores))

# Part 2
new_cards = expanded_cards(scratch_cards)
for card in new_cards:
    print(card)