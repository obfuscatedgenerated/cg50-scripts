if __name__ == "__main__":
    i = 0
    o = 1

    targ = float(input("Target (or type inf):\n"))

    while targ != i and i < targ:
        print(i)
        nth = i + o
        i = o
        o = nth

    print(i)

    print(f"{targ} in sequence: {i == targ}")
