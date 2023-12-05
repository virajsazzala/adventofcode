def clean_gamedata(data):
    gd = data.split(":")
    gd = [d.split(",") for d in gd[1].split(";")]
    gd = [tuple(d.strip().split(" ")) for ld in gd for d in ld]

    return gd


def is_possible(gamedata, query):
    # clean gamedata
    gd = clean_gamedata(gamedata)

    # get max balls per color
    max_vals = {"red": float("-inf"), "green": float("-inf"), "blue": float("-inf")}

    for v, c in gd:
        if int(v) > max_vals[c]:
            max_vals[c] = int(v)

    qr, qg, qb = query

    return max_vals["red"] <= qr and max_vals["green"] <= qg and max_vals["blue"] <= qb


def find_possible_games(data, query):
    possible_games = []

    for d in data:
        if is_possible(d, query):
            possible_games.append(d)

    return possible_games


def sum_game_ids(possible_games):
    total = 0

    for game in possible_games:
        gid = int((game.split(":")[0]).split(" ")[1])
        total += gid

    return total


def main():
    with open("data/inputs.txt", "r") as f:
        data = f.read().splitlines()

    # [red, green, blue]
    query = [12, 13, 14]

    pg = find_possible_games(data, query)

    print(sum_game_ids(pg))


if __name__ == "__main__":
    main()
