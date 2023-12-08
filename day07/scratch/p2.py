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
        "J": 0,
        "2": 1,
        "3": 2,
        "4": 3,
        "5": 4,
        "6": 5,
        "7": 6,
        "8": 7,
        "9": 8,
        "T": 9,
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

    # maximize ht by changing j

    
    cvc = vc.copy()
    ccvc = {}
    mht = hand_type(vc)
    if 'J' in cvc.keys():
        for k, v in cvc.items():
            if k == 'J': continue
            cvc[k] += cvc['J']

            cbc = cvc.copy()

            del cbc ['J']
            cht = hand_type(cbc)

            if cht > mht:
                mht = cht
                cvc = vc.copy()
                ccvc = cbc.copy()
            else:
                cvc = vc.copy()

    return mht, order


def get_keys_by_value(idt, search_value):
    id = {}
    for k, v in idt.items():
        tv = v[0]
        id.update({k: tv})

    matching_keys = [key for key, value in id.items() if value == search_value]
    return matching_keys


ranks = {}


for h, b in dt.items():
    ht, order = rank(h)
    ranks.update({h: [ht, order]})


def rank_hands(h):
    pass


def rank_dt_li(id):
    si = sorted(id.items(), key=lambda x: x[1], reverse=False)
    rd = {key: rank + 1 for rank, (key, _) in enumerate(si)}
    return rd


final_ranks = {}
for v, o in ranks.values():
    kbv = get_keys_by_value(ranks, v)

    orders = {}
    for j in kbv:
        orders.update({j: ranks[j][1]})

    ranked = rank_dt_li(orders)

    for k, x in ranked.items():
        final_ranks.update({k: x})


br = {}
for k, v in ranks.items():
    tv = v[0]
    br.update({k: tv})


def rank_dt_mix(pd, sd):
    si = sorted(
        pd.items(), key=lambda x: (x[1], sd[x[0]])
    )
    rd = {key: rank + 1 for rank, (key, _) in enumerate(si)}

    return rd


rwt = rank_dt_mix(br, final_ranks)

rs = 0
for k, v in rwt.items():
    y = int(dt[k]) * int(v)
    rs += y

print(rs)
