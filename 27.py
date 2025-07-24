def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        start_index = 0
        nums_len = len(nums)

        while start_index < nums_len:
            if nums[start_index] == val:
                nums[start_index] = nums[nums_len - 1]
                nums_len -= 1
            else:
                start_index += 1

        return start_index

# Time : O(n)
# Space : O(1)

'''
Solution 2.
def removeElement(self, nums, val):
    k = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[k] = nums[i]
            k += 1

    return k

# Time : O(n)
# Space : O(1)
'''
