#!/usr/bin/env python3

with open("../data/inputs.txt", "r") as f:
    d = f.readlines()

dt = {}
for ln in d:
    h, b = ln.strip("\n").split(" ")
    dt.update({h: b})


def hand_type(vc):
    vv = list(vc.values())

    if vv == [5]:
        return 7
    if vv == [1, 4] or vv == [4, 1]:
        return 6
    if vv == [3, 2] or vv == [2, 3]:
        return 5
    if vv == [3, 1, 1] or vv == [1, 1, 3] or vv == [1, 3, 1]:
        return 4
    if vv == [2, 2, 1] or vv == [1, 2, 2] or vv == [2, 1, 2]:
        return 3
    if (
        vv == [2, 1, 1, 1]
        or vv == [1, 2, 1, 1]
        or vv == [1, 1, 2, 1]
        or vv == [1, 1, 1, 2]
    ):
        return 2
    if vv == [1, 1, 1, 1, 1]:
        return 1

    return -1


def rank(h):
    p = {
        "2": 0,
        "3": 1,
        "4": 2,
        "5": 3,
        "6": 4,
        "7": 5,
        "8": 6,
        "9": 7,
        "T": 8,
        "J": 9,
        "Q": 10,
        "K": 11,
        "A": 12,
    }

    order = []
    for i in h:
        order.append(p[i])

    h = list(h)
    vc = {}
    hs = set(h)
    for v in hs:
        h.count(v)
        vc.update({v: h.count(v)})

    ht = hand_type(vc)
    return ht, order


def get_keys_by_value(idt, search_value):
    input_dict = {}
    for k, v in idt.items():
        tv = v[0]
        input_dict.update({k: tv})

    matching_keys = [key for key, value in input_dict.items() if value == search_value]
    return matching_keys


ranks = {}


for h, b in dt.items():
    ht, order = rank(h)
    ranks.update({h: [ht, order]})


def rank_hands(h):
    pass


def reverse_rank_dict_by_list_order(input_dict):
    # Sort the dictionary items based on the order of their value lists
    sorted_items = sorted(input_dict.items(), key=lambda x: x[1], reverse=False)

    # Create a new dictionary with keys mapped to their ranks
    ranked_dict = {key: rank + 1 for rank, (key, _) in enumerate(sorted_items)}

    return ranked_dict


final_ranks = {}
for v, o in ranks.values():
    kbv = get_keys_by_value(ranks, v)

    orders = {}
    for j in kbv:
        orders.update({j: ranks[j][1]})

    ranked = reverse_rank_dict_by_list_order(orders)

    for k, x in ranked.items():
        final_ranks.update({k: x})


br = {}
for k, v in ranks.items():
    tv = v[0]
    br.update({k: tv})


def rank_dict_with_ties(primary_dict, secondary_dict):
    # Sort the dictionary items based on the primary values and then the secondary order
    sorted_items = sorted(
        primary_dict.items(), key=lambda x: (x[1], secondary_dict[x[0]])
    )

    # Create a new dictionary with keys mapped to their ranks
    ranked_dict = {key: rank + 1 for rank, (key, _) in enumerate(sorted_items)}

    return ranked_dict


rwt = rank_dict_with_ties(br, final_ranks)

rs = 0
for k, v in rwt.items():
    y = int(dt[k]) * int(v)
    rs += y

print(rs)
