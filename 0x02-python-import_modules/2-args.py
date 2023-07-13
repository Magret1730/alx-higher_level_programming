#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    if argv[1:2]:
        print("{} argument:".format(len(argv) - 1))
    elif argv[1:]:
        print("{} arguments:".format(len(argv) - 1))
    elif argv[:1]:
        print("{} argument.".format(len(argv) - 1))
    for i in range(1, len(argv)):
        if argv[1:2]:
            print("{}: {}".format(i, argv[i]))
        elif argv[1:]:
            print("{}: {}".format(i, argv[i]))
