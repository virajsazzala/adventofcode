import re


def get_total(data):
    total = 1

    for line in data:
        _, line = line.strip().split(":")

        winning, has = line.split("|")
        winning = re.findall(r"\d+", winning)
        has = re.findall(r"\d+", has)

        common = set(winning).intersection(set(has))

        if len(common) == 0:
            continue

        card_total = 1

        for _ in range(1, len(common)):
            card_total *= 2

        total += card_total

    return total - 1


def main():
    with open("data/inputs.txt", "r") as f:
        data = f.read().splitlines()

    print(get_total(data))


if __name__ == "__main__":
    main()
