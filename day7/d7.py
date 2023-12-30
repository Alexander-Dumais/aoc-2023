def read_input(file_name):
    hands = []
    with open(file_name, 'r') as f:
        for line in f:
            line = line.rstrip().split()
            hands.append({"cards": card_values(line[0]), "bid": int(line[1])})
    return hands


def card_values(cards: [str]):
    card_vals = []
    for card in cards:
        match card.isdigit():
            case True:
                card_vals.append(int(card))
            case False:
                card_vals.append({"T": 10, "J": 11, "Q": 12, "K": 13, "A": 14}[card])
    return card_vals


def hand_kind(hand):
    types_and_rank = {0: 'highc', 1: '1pair', 2: '2pair', 3: '3kind', 4: 'fhouse', 5: '4kind', 6: '5kind'}
    counted_cards = {}

    # Count cards
    for card in hand:
        if card in counted_cards:
            counted_cards[card] += 1
        else:
            counted_cards[card] = 1

    card_vals = sorted(list(counted_cards.values()), reverse=True)
    if len(card_vals) == 1:  # 5kind
        kind = 6
    elif len(card_vals) == 2 and card_vals[0] == 4:  # 4kind
        kind = 5
    elif len(card_vals) == 2 and card_vals[0] == 3:  # fhouse
        kind = 4
    elif len(card_vals) == 3 and card_vals[0] == 3:  # 3kind
        kind = 3
    elif len(card_vals) == 3:  # 2pair
        kind = 2
    elif len(card_vals) == 4:  # 1pair
        kind = 1
    else:  # highc
        kind = 0

    return kind, types_and_rank[kind]


def compare(hand_kind1, hand_kind2):
    if hand_kind1[1] < hand_kind2[1]:
        return -1
    elif hand_kind1[1] == hand_kind2[1]:
        if hand_kind1[0] < hand_kind2[0]:
            return -1
        elif hand_kind1[0] > hand_kind2[0]:
            return 1
        else:
            return 0
    else:
        return 1


def sort_hands(hands, kinds):
    sorted_hands = [(hands[0], kinds[0])]

    i = 1
    while i < len(hands):
        h = 0
        while h < len(sorted_hands):
            if compare((hands[i]["cards"], kinds[i]), (sorted_hands[h][0]["cards"], sorted_hands[h][1])) > 0:
                h += 1
            else:
                break
        sorted_hands.insert(h, (hands[i], kinds[i]))
        i += 1

    return sorted_hands


def rank_hands(hands):
    kinds = []
    ranked_hands = []

    for hand in hands:
        kind = hand_kind(hand["cards"])
        kinds.append(kind)

    ranked_hands = sort_hands(hands, kinds)
    return ranked_hands


def part_a(file_name):
    hands = read_input(file_name)


    ranked_hands = rank_hands(hands)
    rank = 1
    total_bid_value = 0
    for hand, kind in ranked_hands:
        bid_value = hand['bid'] * rank
        total_bid_value += bid_value
        print(f"cards: {hand['cards']} -- kind: {kind[1]} -- bid value: {hand['bid']} * {rank} := {bid_value}")
        rank += 1
    print(f"total bid value of hands: {total_bid_value}")


part_a('input')
