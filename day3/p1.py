import re


def has_special_char(row, col, data_matrix):
    try:
        return re.match(r"[^a-zA-Z0-9.]", data_matrix[row][col]) is not None
    except IndexError:
        return False


def sum_part_numbers(data_matrix):
    matrix_len = len(data_matrix[0])

    total_sum = 0
    for i, line in enumerate(data_matrix):
        for match in re.finditer(r"\d+", line):
            start, end = match.span()
            num = match.group()

            for x in range(start, end):
                sym_pos = [
                    (i - 1, x - 1),
                    (i - 1, x),
                    (i - 1, x + 1),
                    (i, x - 1),
                    (i, x + 1),
                    (i + 1, x - 1),
                    (i + 1, x),
                    (i + 1, x + 1),
                ]

                for a, b in sym_pos:
                    if not 0 <= a < matrix_len or not 0 <= b < matrix_len:
                        continue

                    if has_special_char(a, b, data_matrix):
                        break
                else:
                    continue
                break
            else:
                continue

            total_sum += int(num)

    return total_sum


def main():
    with open("data/inputs.txt", "r") as f:
        data = f.read().splitlines()

    print(sum_part_numbers(data))


if __name__ == "__main__":
    main()
