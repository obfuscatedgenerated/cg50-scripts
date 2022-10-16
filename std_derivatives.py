from math import sin, cos, tan, log, e

ln = lambda x: log(x, e)
sec = lambda x: 1 / cos(x)
csc = lambda x: 1 / sin(x)
cot = lambda x: 1 / tan(x)

funcs_2_names = {
    sin: "sin",
    cos: "cos",
    tan: "tan",
    sec: "sec",
    csc: "csc",
    cot: "cot",
    ln: "ln",
    e: "e"
}

derivative_func = {
    sin: cos,
    cos: lambda x: -sin(x),
    tan: lambda x: 1 / cos(x) ** 2,
    sec: lambda x: sec(x) * tan(x),
    csc: lambda x: -csc(x) * cot(x),
    cot: lambda x: -1 / sin(x) ** 2,
    ln: lambda x: 1 / x,
    e: lambda x: e ** x,
}

derivative_str = {
    "sin": "cos",
    "cos": "-sin",
    "tan": "sec^2",
    "sec": "sec tan",
    "csc": "-csc cot",
    "cot": "-csc^2",
    "ln": "1/x",
    "e": "e^x",
}

def template_derivative(func, x):
    templates = {
        "sin": "cos"+x,
        "cos": "-sin"+x,
        "tan": "sec^2"+x,
        "sec": "sec"+x+"tan"+x,
        "csc": "-csc"+x+"cot"+x,
        "cot": "-csc^2"+x,
        "ln": "1/"+x,
        "e": "e^"+x,
    }

    return templates[func]

def soft_derivative(func, x, h=0.0001):
    return (func(x + h) - func(x)) / h

def std_derivative(func, x):
    return derivative_func[func](x)


i = 0
for func in derivative_func:
    print(str(i+1)+") "+funcs_2_names[func]+"'(x) = "+template_derivative(funcs_2_names[func], '(x)'))
    i += 1
print()

while True:
    option = input("Select a function by number (leave blank to exit): ")
    if option == "":
        break
    try:
        option = int(option)
        if option not in range(1, len(derivative_func)+1):
            raise ValueError
    except ValueError:
        print("Invalid option")
        continue
    
    func = list(derivative_func)[option-1]

    x = float(input("Enter a value for x: "))
    print(funcs_2_names[func]+"'("+str(x)+") = "+str(std_derivative(func, x)))