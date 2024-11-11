
def guessNumber(n: int) -> int:
    left_idx = 1
    right_idx = n
    #
    while (left_idx <= right_idx):
        middle_idx = left_idx + int((right_idx - left_idx)/2)
        guess_result = guess(middle_idx)
        if guess_result == 0:
            return middle_idx
        elif guess_result > 0:
            left_idx = middle_idx + 1
        else:
            right_idx = middle_idx - 1
    return -1