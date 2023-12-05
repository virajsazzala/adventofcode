import re


def get_nums_from_line(line):
    nums = re.findall(r"\d", line)
    nums = [int(num) for num in nums]

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
