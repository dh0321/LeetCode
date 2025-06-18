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

'''
Solution 1.
def twoSum(self, nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[j] == target - nums[i]:
                return [i, j]


Solution 2.
def twoSum(self, nums: List[int], target: int) -> List[int]:
      hashmap = {}
      for i in range(len(nums)):
          hashmap[nums[i]] = i
      for i in range(len(nums)):
          complement = target - nums[i]
          if complement in hashmap and hashmap[complement] != i:
              return [i, hashmap[complement]]

Solution 3.
 def twoSum(self, nums: List[int], target: int) -> List[int]:
      hashmap = {}
      for i in range(len(nums)):
          complement = target - nums[i]
          if complement in hashmap:
              return [i, hashmap[complement]]
          hashmap[nums[i]] = i

'''
