from word2number import w2n


def get_nums_from_line(input):
    nums = []

    for i in range(len(input)):
        for j in range(i + 1, len(input) + 1):
            substring = input[i:j]

            try:
                number = w2n.word_to_num(substring)
                nums.append(number)
            except ValueError:
                pass

    if len(nums) == 0:
        return 0

    return int(f"{nums[0]}{nums[-1]}")


def main():
    with open("data/inputs.txt", "r") as f:
        data = f.read().splitlines()

    total = 0
    for line in data:
        total += get_nums_from_line(line)

    print(total)


if __name__ == "__main__":
    main()
