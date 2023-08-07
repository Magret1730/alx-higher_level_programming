#!/usr/bin/python3
"""A program that solves the N queens problem.

The N queens puzzle is the challenge of placing N
non-attacking queens on an N×N chessboard.
"""

import sys


def main():
    """A program that solves the N queens problem"""

    if __name__ == "__main__":
        if len(sys.argv) != 2:
            print("Usage: nqueens N")
            sys.exit(1)

        try:
            N = int(sys.argv[1])
            solve_nqueens(N)
        except ValueError:
            print("N must be a number")
            sys.exit(1)
