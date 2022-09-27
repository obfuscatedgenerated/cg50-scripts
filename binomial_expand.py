from math import comb

if __name__ == "__main__":
    print("(a + b)^n\n")

    sub = input("Would you like to sub into a and b? (y/N) ").lower() == "y"

    if sub:
        a = int(input("a: "))
        b = int(input("b: "))
    else:
        a = "a"
        b = "b"

    n = int(input("n: "))

    print()

    print(f"Using ({a} + {b})^{n}\n")

    condense = (
        not input("Would you like to condense down the multiplication? (Y/n) ").lower()
        == "n"
    )

    newline = (
        not input("Would you like to print each term on a new line? (Y/n) ").lower()
        == "n"
    )
    preend = "\n+ " if newline else " + "

    print()

    for i in range(n + 1):
        end = preend if i != n else "\n"
        if condense:
            if sub:
                print(f"[{comb(n, i)}({a})^{n - i}][({b})^{i}]", end=end)
            else:
                print(f"({comb(n, i)}{a}^{n - i})({b}^{i})", end=end)
        else:
            print(f"{a}^{n - i} * {b}^{i} * {comb(n, i)}", end=end)

    print()

    if sub:
        compute = (
            not input("Would you like to compute the result? (Y/n) ").lower() == "n"
        )

        print()

        if compute:
            result = 0
            for i in range(n + 1):
                result += comb(n, i) * (a ** (n - i)) * (b ** i)
            print(f"Result: {result}")
