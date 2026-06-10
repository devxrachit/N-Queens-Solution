# N-Queens Solver

So this is my take on the classic N-Queens puzzle. Python & just backtracking. If you've never run into it before: you've got an N×N chessboard and N queens, and you need to place all of them so that nobody can attack anybody else. Queens hit along rows, columns, and both diagonals, so it's trickier than it sounds.

I built this mostly to actually *understand* backtracking instead of just nodding along to a YouTube video. Turns out the best way to get it is to sit down with a 4×4 grid on paper and move queens around by hand until you see why it works. Highly recommend doing that before reading the code.

## The one trick that makes it click

Here's the thing that took me a while to notice: no two queens can ever share a row, so you might as well put **exactly one queen per row**. That immediately kills half the problem. Now you're not picking (row, col) pairs out of thin air, you're just walking down the rows one at a time and asking "okay, which column for this row?"

That's why a whole solution is just a list of column numbers. `[1, 3, 0, 2]` means row 0's queen sits in column 1, row 1's in column 3, and so on. Compact and easy to print.

## How do I know if a square is safe?

Checking the column is obvious. The diagonals are the clever bit. Two squares are on the same diagonal when their `row - col` matches (one direction) or their `row + col` matches (the other). So every diagonal gets a single number, and I can just keep three sets of "stuff that's already taken":

- `cols` for occupied columns
- `diag` for occupied `row - col` diagonals
- `anti` for occupied `row + col` diagonals

A square is safe if none of its three numbers are sitting in those sets. Sets give O(1) lookups, so this stays fast even as N grows.

## The actual search

For each row, try every column. Skip the ones that are attacked. When you find a safe spot, drop a queen there, record its column and diagonals, and recurse into the next row. Once the recursion comes back, lift the queen off and free those squares again so you can try the next column with a clean slate.

That last "lift it back off" step is the whole soul of backtracking. Without it, the sets fill up with stale entries and nothing works. It's the same thing you do in a maze: walk down a path, hit a dead end, walk back to the fork, try the other way.

When you've managed to place a queen in *every* row, that's a complete solution and it gets saved.

```
Enter N: 8
92 solution(s) -> /path/to/nqueens_8.txt
```

Everything gets written to `nqueens_<N>.txt`, each solution shown both as a column list and as an actual board you can look at.

## What the output looks like

For `N = 4`:

```
N = 4, 2 solution(s)

#1: [1, 3, 0, 2]
. Q . .
. . . Q
Q . . .
. . Q .
 The other one's just the mirror image of the first one. 
 #2: [2,0,3,1]
 
```

## A few numbers, if you're curious

| N | Solutions |
|---|-----------|
| 1 | 1 |
| 4 | 2 |
| 5 | 10 |
| 6 | 4 |
| 8 | 92 |

Fun fact: N = 2 and N = 3 have zero solutions. 
