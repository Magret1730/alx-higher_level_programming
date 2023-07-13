#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    add_argv = 0
    for i in range(1, len(argv)):
        add_argv = add_argv + int(argv[i])
    print("{}".format(add_argv))
