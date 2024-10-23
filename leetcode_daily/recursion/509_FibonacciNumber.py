def fib(n):
    """
    :type n: int
    :rtype: int
    """
    if n < 2:
        return n
    fibo_values = [0, 1]
    for i in range(2, n + 1):
        update_value = fibo_values[-1] + fibo_values[-2]
        fibo_values.append(update_value)
    return fibo_values[-1]

if __name__ == "__main__":
    list_numb = [2, 3, 4]
    for n in list_numb:
        # Expect: 1, 2, 3
        print(fib(n))    