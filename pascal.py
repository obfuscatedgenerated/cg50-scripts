from math import comb


def line(n): # list comprehension to generate a list of the numbers in a line of Pascal's triangle, with each element being a string
    return [str(comb(n, k)) for k in range(n + 1)]


def pascal(n):
    lookahead = " ".join(line(n)) # calculate and string together the numbers in the last line
    length = len(lookahead) # used for centering the other lines

    for i in range(n):
        output = " ".join(line(i)) # calculate and string together the numbers in the current line
        print(output.center(length)) # center the current line and print it

    print(lookahead) # print the last line


if __name__ == "__main__":
    n = int(input("Number of lines: "))

    print()

    pascal(n)
