def isPerfectSquare(num: int) -> bool:
    low = 1
    high = num
    while low <= high:
        middle = low + int((high - low) / 2)
        if middle ** 2 == num:
            return True
        elif middle ** 2 > num:
            high = middle - 1
        else:
            low = middle + 1
    return False