#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    num = len(sys.argv) - 1
    if num != 3:
        print("usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    a = sys.argv[2]
    if a != "+" and a != "-" and a != "*" and a != "/":
        print("Unknown operator. Only +, -, * and / are supported.")
        sys.exit(1)

    from calculator_1 import add, sub, mul, div
    x = int(sys.argv[1])
    y = int(sys.argv[3])

    if a == "+":
        print("{} + {} = {}".format(x, y, add(x, y)))
    elif a == "-":
        print("{} - {} = {}".format(x, y, sub(x, y)))
    elif a == "*":
        print("{} * {} = {}".format(x, y, mul(x, y)))
    elif a == "/":
        print("{} / {} = {}".format(x, y, div(x, y)))
    else:
        print("Unknown operator. Only +, -, * and / are supported.")
        sys.exit(1)



