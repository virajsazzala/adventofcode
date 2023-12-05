import re


def has_special_char(row, col, data_matrix):
    try:
        return re.match(r"[^a-zA-Z0-9.]", data_matrix[row][col]) is not None
    except IndexError:
        return False


def find_part_numbers(matrix):
    matrix_length = len(matrix[0])
    part_nums = {}

    for i, line in enumerate(matrix):
        for match in re.finditer(r"\d+", line):
            start, end = match.span()
            number = match.group()

            for x in range(start, end):
                positions = [
                    (i - 1, x - 1),
                    (i - 1, x),
                    (i - 1, x + 1),
                    (i, x - 1),
                    (i, x + 1),
                    (i + 1, x - 1),
                    (i + 1, x),
                    (i + 1, x + 1),
                ]

                for row, col in positions:
                    if 0 <= row < matrix_length and 0 <= col < matrix_length:
                        if (
                            has_special_char(row, col, matrix)
                            and matrix[row][col] == "*"
                        ):
                            part_nums[(row, col)] = part_nums.get((row, col), []) + [
                                number
                            ]
                            break

                else:
                    continue

                break

    return part_nums


def sum_part_numbers(part_nums):
    total_sum = 0

    for k, v in part_nums.items():
        if len(v) == 2:
            a, b = map(int, v)
            total_sum += a * b

    return total_sum


def main():
    with open("data/inputs.txt") as f:
        data = f.read().splitlines()

    part_nums = find_part_numbers(data)
    print(sum_part_numbers(part_nums))


if __name__ == "__main__":
    main()
