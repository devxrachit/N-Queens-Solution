import os
import sys


def solve(n):
    solutions = []
    cols, diag, anti = set(), set(), set()
    queens = [-1] * n

    def place(row):
        if row == n:
            solutions.append(queens.copy())
            return
        for col in range(n):
            if col in cols or row - col in diag or row + col in anti:
                continue
            queens[row] = col
            cols.add(col)
            diag.add(row - col)
            anti.add(row + col)
            place(row + 1)
            cols.discard(col)
            diag.discard(row - col)
            anti.discard(row + col)
        queens[row] = -1

    place(0)
    return solutions


def render(queens):
    return "\n".join(
        " ".join("Q" if c == col else "." for c in range(len(queens)))
        for col in queens
    )


def write_solutions(solutions, n, path):
    with open(path, "w") as f:
        f.write(f"N = {n}, {len(solutions)} solution(s)\n\n")
        for i, queens in enumerate(solutions, 1):
            f.write(f"#{i}: {queens}\n")
            f.write(render(queens) + "\n\n")


def main():
    try:
        n = int(input("Enter N: "))
    except ValueError:
        sys.exit("N must be an integer.")
    if n < 1:
        sys.exit("N must be at least 1.")

    solutions = solve(n)
    path = f"nqueens_{n}.txt"
    write_solutions(solutions, n, path)
    print(f"{len(solutions)} solution(s) -> {os.path.abspath(path)}")


if __name__ == "__main__":
    main()