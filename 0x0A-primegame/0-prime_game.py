#!/usr/bin/python3
"""  prime game module
"""

def isWinner(x, nums):
    """ Return: name of the player that
    won the most rounds
    """
    if not nums or x < 1:
        return (None)

    n = max(nums)
    array = [True for _ in range(max(n + 1, 2))]
    for i in range(2, int(pow(n, 0.5)) + 1):
        if array[i]:
            for j in range(i*i, n + 1, i):
                array[j] = False

    array[0] = array[1] = False
    c = 0
    for i in range(len(array)):
        if array[i]:
            c += 1
        array[i] = c

    player1 = 0
    for n in nums:
        player1 += array[n] % 2 == 1
    if player1 * 2 == len(nums):
        return None
    if player1 * 2 > len(nums):
        return "Maria"
    return "Ben"