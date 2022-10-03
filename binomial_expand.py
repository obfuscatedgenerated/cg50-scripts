from math import comb

def smart_comb(n, i):
    if i == 0 or i == n:
        return 1
    return comb(n, i)

if __name__ == "__main__":
    print("(a + b)^n\n")

    sub = input("Would you like to sub into a and b? (y/N) ").lower() == "y"

    if sub: # take real integers
        while True:
            try:
                a = int(input("a: "))
                break
            except ValueError:
                print("a must be a valid integer")
        while True:
            try:
                b = int(input("b: "))
                break
            except ValueError:
                print("b must be a valid integer")
    else: # fallback to string values
        a = "a" 
        b = "b"

    while True:
        try:
            n = int(input("n: ")) # get the power
            break
        except ValueError:
            print("n must be a valid integer")

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
    preend = "\n+ " if newline else " + " # pre-generated end string for the print function

    print()

    for i in range(n + 1):
        end = preend if i != n else "\n" # create the end string for the print function, derived from the pre-generated string
        if condense:
            if sub:
                print(f"[{smart_comb(n, i)}({a})^{n - i}][({b})^{i}]", end=end) # print the term in the form of [nCr][a^(n - r)][b^r]
            else:
                print(f"({smart_comb(n, i)}{a}^{n - i})({b}^{i})", end=end) # print the term in the form of [nCr][(a)^(n - r)][(b)^r]
        else:
            print(f"{a}^{n - i} * {b}^{i} * {smart_comb(n, i)}", end=end) # print the term in the form of a^(n - r) * b^r * nCr

    print()

    if sub:
        compute = (
            not input("Would you like to compute the result? (Y/n) ").lower() == "n"
        )

        print()

        if compute:
            assert type(a) is int and type(b) is int, "a and b must be integers to compute the result. this code should never be reached."
            print(f"Result: {(a+b) ** n}")
