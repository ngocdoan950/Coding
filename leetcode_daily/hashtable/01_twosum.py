def twoSum(nums: List[int], target: int) -> List[int]:
    dict_value_idx = {}
    for idx, num in enumerate(nums):
        if num not in dict_value_idx.keys():
            dict_value_idx[target - num] = idx
        else:
            return [idx, dict_value_idx[num]]