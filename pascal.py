def factorial(n):
    fact = 1
    for num in range(2, n + 1):
        fact *= num
    return fact

def comb(n, r):
    return factorial(n) // factorial(r) // factorial(n-r)

def smart_comb(n, i):
    if i == 0 or i == n:
        return 1
    return comb(n, i)

def line(n): # list comprehension to generate a list of the numbers in a line of Pascal's triangle, with each element being a string
    return [str(smart_comb(n, k)) for k in range(n + 1)]

def center(string, length): # center a string python 2
    n = length - len(string)
    return " " * (n // 2) + string + " " * (n - n // 2)

def pascal(n):
    lookahead = " ".join(line(n)) # calculate and string together the numbers in the last line
    length = len(lookahead) # used for centering the other lines

    for i in range(n):
        output = " ".join(line(i)) # calculate and string together the numbers in the current line
        print(center(output, length)) # center the current line and print it

    print(lookahead) # print the last line



n = int(input("Number of lines: "))

print()

pascal(n)
