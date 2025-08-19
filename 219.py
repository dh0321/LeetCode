# Hash Map
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        seen = {}
        for i, num in enumerate(nums):
            if num in seen and i - seen[num] <= k:
                return True
            seen[num] = i
        return False

# Time: O(n)
# Space: O(n)


'''
Solution1.

# Sliding Window
def containsNearbyDuplicate(self, nums, k):
    window = set()
    for i, num in enumerate(nums):

        if num in window:
            return True
        window.add(num)

        if len(window) > k:
            window.remove(nums[i - k])

    return False

# Time: O(n)
# Space: O(k)


'''
