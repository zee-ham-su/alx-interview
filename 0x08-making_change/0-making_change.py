#!/usr/bin/python3
""" making change module
"""


def makeChange(coins, total):
    """ Find the minimum number of coins required
    to reach a specified total amount."""
    if total <= 0:
        return 0
    coins.sort(reverse=True)
    balance = 0
    for c in coins:
        if total == 0:
            return balance
        if total >= c:
            balance += total // c
            total = total % c
    return -1