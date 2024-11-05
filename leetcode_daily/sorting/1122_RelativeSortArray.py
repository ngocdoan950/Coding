def relativeSortArray(arr1: List[int], arr2: List[int]) -> List[int]:
    """
    NOTE: check keys() have time complexity (1)
    """
    dict_nums_count = {}
    list_not_exist_numb = []
    #
    for element in arr1:
    
        if element in dict_nums_count.keys():
            dict_nums_count[element] += 1
        else:
            dict_nums_count[element] = 1
        #
        if element not in arr2:
            list_not_exist_numb.append(element)
    #
    list_not_exist_numb.sort()
    #
    list_refined_arr1 = []
    for element in arr2:
        count = dict_nums_count[element]
        list_refined_arr1 += [element]*count
    return list_refined_arr1 + list_not_exist_numb