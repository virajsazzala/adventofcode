def parse_data(lines):
    seeds = [int(s) for s in lines[0].split()[1:]]

    maps = []
    for line in lines[2:]:
        if "map" in line:
            maps.append([])
        elif line != "":
            maps[-1].append([int(l) for l in line.split()])

    return seeds, maps


def to_dest(map, index):
    for entry in map:
        if entry[1] <= index < (entry[1] + entry[2]):
            return index - entry[1] + entry[0]
    return index


def find_min(lines):
    seeds, maps = lines

    result = []
    for seed in seeds:
        for map in maps:
            seed = to_dest(map, seed)
        result.append(seed)

    return min(result)


def main():
    lines = []
    with open("data/inputs.txt", "r") as f:
        for line in f:
            lines.append(line.strip())

    print(find_min(parse_data(lines)))


if __name__ == "__main__":
    main()
