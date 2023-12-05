import re


def count_scratchcards(data):
    total_scratchcards = 0

    card_count = {key: 1 for key in range(1, len(data) + 1)}

    for idx, line in enumerate(data):
        card_name, line = line.strip().split(":")

        card_no = idx + 1

        winning, has = line.split("|")
        winning = re.findall(r"\d+", winning)
        has = re.findall(r"\d+", has)

        common = set(winning).intersection(set(has))

        for _ in range(card_count[card_no]):
            for i in range(card_no + 1, card_no + len(common) + 1):
                card_count[i] += 1

    for _, v in card_count.items():
        total_scratchcards += v

    return total_scratchcards


def main():
    with open("data/inputs.txt", "r") as f:
        data = f.read().splitlines()

    print(count_scratchcards(data))


if __name__ == "__main__":
    main()
