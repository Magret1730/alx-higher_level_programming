#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    a = 10
    b = 5
    calculator_add = add(a, b)
    calculator_sub = sub(a, b)
    calculator_mul = mul(a, b)
    calculator_div = div(a, b)
    print("{0} + {1} = {2}".format(a, b, calculator_add))
    print("{} - {} = {}".format(a, b, calculator_sub))
    print("{} * {} = {}".format(a, b, calculator_mul))
    print("{1} / {2} = {0}".format(calculator_div, a, b))
