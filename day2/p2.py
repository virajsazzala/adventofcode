def clean_gamedata(data):
    gd = data.split(":")
    gd = [d.split(",") for d in gd[1].split(";")]
    gd = [tuple(d.strip().split(" ")) for ld in gd for d in ld]

    return gd


def find_min_cubes(gamedata):
    gd = clean_gamedata(gamedata)

    max_vals = {"red": float("-inf"), "green": float("-inf"), "blue": float("-inf")}

    for v, c in gd:
        if int(v) > max_vals[c]:
            max_vals[c] = int(v)

    return list(max_vals.values())  # [r, g, b]


def find_power(values):
    return values[0] * values[1] * values[2]


def sum_of_powers(gamedata):
    total = 0

    for data in gamedata:
        cubes = find_min_cubes(data)
        power = find_power(cubes)
        total += power

    return total


def main():
    with open("data/inputs.txt", "r") as f:
        data = f.read().splitlines()

    print(sum_of_powers(data))


if __name__ == "__main__":
    main()
