def stoneGame(piles):
    n = len(piles)
    data = piles[:]
    for i in range(2, n + 1):
        for j in range(0, n - i + 1):
            l = j + i - 1
            data[j] = max(piles[j] - data[j+1], piles[l] - data[j])
    return data[0] > 0