def smallerNumbersThanCurrent(nums: List[int]) -> List[int]:
    #
    org_nums = nums.copy()
    nums.sort()
    #
    dict_number_idx = {}
    dict_number_idx[nums[0]] = 0
    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1]:
            continue
        dict_number_idx[nums[i]]  = i
    list_number_smaller = []
    for unsorted_numb in org_nums:
        idx = dict_number_idx[unsorted_numb]
        list_number_smaller.append(idx)
    return list_number_smaller