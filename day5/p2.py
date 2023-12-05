import numpy as np
from tqdm import trange


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
        if entry[0] <= index < (entry[0] + entry[2]):
            return index - entry[0] + entry[1]
    return index


def find_min(lines):
    seeds, maps = lines

    maps.reverse()
    init = None

    for i in trange(0, 100000000, 1000):
        seed = i
        for map in maps:
            seed = to_dest(map, seed)
        for seeed, rang in np.array(seeds).reshape((-1, 2)):
            if seed >= seeed and seed < seeed + rang:
                init = i
                break
        else:
            continue
        break

    for i in trange(init - 1000, init + 1):
        seed = i
        for map in maps:
            seed = to_dest(map, seed)
        for seeed, rang in np.array(seeds).reshape((-1, 2)):
            if seed >= seeed and seed < seeed + rang:
                return i
        else:
            continue


def main():
    lines = []
    with open("data/inputs.txt", "r") as f:
        for line in f:
            lines.append(line.strip())

    print(find_min(parse_data(lines)))


if __name__ == "__main__":
    main()
