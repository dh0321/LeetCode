# Brute Force

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

# Time: O(n^2)
# Space: O(1)

'''
Solution 1.
def twoSum(self, nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[j] == target - nums[i]:
                return [i, j]


Solution 2.
# Hash Map
# Time: O(n)
# Space: O(n)
def twoSum(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    index_map = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in index_map:
            return [index_map[complement], i]
        index_map[num] = i


Solution 3.
def twoSum(self, nums: List[int], target: int) -> List[int]:
      hashmap = {}
      for i in range(len(nums)):
          hashmap[nums[i]] = i
      for i in range(len(nums)):
          complement = target - nums[i]
          if complement in hashmap and hashmap[complement] != i:
              return [i, hashmap[complement]]


'''
