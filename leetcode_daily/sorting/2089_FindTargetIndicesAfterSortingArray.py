def targetIndices(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]

        TODO: 
            + self-implement sort algorithm
            + inconsistent  time complexity
        """
        #       sort
        nums.sort()
        #
        arr_results = []
        #
        for i in range(len(nums)):
            if nums[i] == target:
                arr_results.append(i)
        return arr_results