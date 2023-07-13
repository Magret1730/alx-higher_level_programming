#!/usr/bin/python3
if __name__ == "__main__":
    import calculator_1 as calc
    from sys import argv

    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    a = int(argv[1])
    operator = argv[2]
    b = int(argv[3])

    if operator == "+":
        result_add = calc.add(a, b)
        print("{} {} {} = {}".format(a, operator, b, result_add))
    elif operator == "-":
        result_sub = calc.sub(a, b)
        print("{} {} {} = {}".format(a, operator, b, result_sub))
    elif operator == "*":
        result_mul = calc.mul(a, b)
        print("{} {} {} = {}".format(a, operator, b, result_mul))
    elif operator == "/":
        result_div = calc.div(a, b)
        print("{} {} {} = {}".format(a, operator, b, result_div))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
