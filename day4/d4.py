
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


def card_copies(cards):
    copies = {}
    for i in range(len(cards)):
        copies[i] = 0

    for card_num in range(len(cards)):
        count_winning_nums = 0
        current_card = cards[card_num]
        for num in current_card["numbers"]:
            if num in current_card["winning"]:
                count_winning_nums += 1

        copies[card_num] = copies[card_num] + 1
        duplicate = copies[card_num]
        while duplicate > 0:
            counts = count_winning_nums
            while counts > 0:
                if card_num + counts in copies:
                    copies[card_num + counts] += 1
                counts -= 1
            duplicate -= 1

    return copies


scratch_cards = read_input("input.txt", ignore_chars=10)  # ignore_chars = 10 for real input

# Part 1
scores = winning_scores(scratch_cards)
print("scores:", scores)
print("total_score:", sum(scores))

# Part 2
copies = card_copies(scratch_cards)
print("total scratch cards (part 2):", sum(copies.values()))
