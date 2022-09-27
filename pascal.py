from math import comb


def line(n):
    return [str(comb(n, k)) for k in range(n + 1)]


def pascal(n):
    lookahead = " ".join(line(n))
    length = len(lookahead)

    for i in range(n):
        output = " ".join(line(i))
        print(output.center(length))

    print(lookahead)


if __name__ == "__main__":
    n = int(input("Number of lines: "))

    print()

    pascal(n)
