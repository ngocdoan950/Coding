def sumOfUnique(nums: List[int]) -> int:
    dict_value_idx = {}
    sum_of_unique = 0
    #  True/False => 2*N
    for idx, num in enumerate(nums):
        if num not in dict_value_idx.keys():
            dict_value_idx[num] = 1
        else:
            dict_value_idx[num] = 0
    #
    for element in dict_value_idx:
        if dict_value_idx[element]:
            sum_of_unique += element
    #
    return sum_of_unique