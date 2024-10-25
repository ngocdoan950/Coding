

def calSquareNumbers(n):
    sum = 0
    while (n > 0):
        k = n % 10
        sum += k*k
        n = int(n / 10)
    return sum

def isHappy(n):
    """
    :type n: int
    :rtype: bool
    """
    if n == 1:
        return True
    if n in list_square_numbers:
        return False
    list_square_numbers.append(n)
    return isHappy(calSquareNumbers(n))


if __name__ == "__main__":
    n = 19
    #
    list_square_numbers = []
    isHappy(n)
    
