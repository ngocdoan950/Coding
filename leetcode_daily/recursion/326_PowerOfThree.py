def isPowerOfThree(n):
    """
    :type n: int
    :rtype: bool
    """
    if n == 1:
        return True
    if n % 3 != 0 or n == 0:
        return False
    #  solution 1
    # list_values = [n]
    # while (n % 3 == 0):
    #     n = n /3
    #     list_values.append(n)
    # if list_values[-1] == 1:
    #     return True
    # else:
    #     return False
    #       solution 2: 
    isPowerOfThree(n/3)
    
if __name__ == "__main__":
    list_numb = [27, 0, -1, 1]
    for n in list_numb:
        # True, False, False, True
        print(isPowerOfThree(n))    