# TOP_DOWN_APPROACH = MEMOIZATION
# Dynamic Programming example, a better way to find out
# how to do the fibonacci sequence and not just using the recursion method.
# A technique is known as memoization #Keeping memos of things that we learned
# Memoization is also known as a top down approach


def fib_memoization(n: int, lookup: dict) -> int:
    if n < 1:
        return -1
    if n == 1 or n == 2:  # The Base Case
        lookup[n] = 1
    if lookup.get(n, None) is None
        lookup[n] = fib_memoization(n - 1, lookup) + fib_memoization(n - 2, lookup)
    return lookup[n]


def main() -> int:
    my_dictionary = {}
    f = fib_memoization(6, my_dictionary)
    print(f)


# Use a dictionary to remember things that we can remove inefficeny so that we dont call for the same values we already
# Have completed


# BOTTOM_UP_APPROACH = TABULATION

# Using an array and has the indecies set at 0

def fib_tabulation(n: int) -> int:
    f = [0] * [n + 1]
    # Base Case
    f[1] = 1
    for i in range(2. n+1)
    f[i] = f[i - 1] + f[i - 2]
    return f[n]
