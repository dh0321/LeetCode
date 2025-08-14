# Using Set
# Time : O(n)

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False


'''
# Using Sort
# Time : O(n log n)
def containsDuplicate(self, nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    nums.sort()
    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1]:
            return True
    return False


# Using Map
# Time : O(n)
def containsDuplicate(self, nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    seen = {}
    for num in nums:
        if num in seen:
            return True
        seen[num] = 1
    return False


# Using BF
# Time limit exceeded
# not efficient for large array
# Time : O(n^2)
def containsDuplicate(self, nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    n = len(nums)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if nums[i] == nums[j]:
                return True
    return False


'''

