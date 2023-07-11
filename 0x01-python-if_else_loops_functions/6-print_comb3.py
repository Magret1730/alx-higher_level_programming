#!/usr/bin/python3
for i in range(0, 100):
    if i == 89:
        print("{:02d}".format(i))
    elif i < 99:
        first_digit = i // 10
        second_digit = i % 10
        if first_digit == second_digit:
            continue
        elif first_digit or second_digit == second_digit or first_digit:
            if first_digit < second_digit:
                print("{:02d}".format(i), end=", ")

# print()
