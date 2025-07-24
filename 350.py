from collections import Counter

class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        
        counts = Counter(nums1)
        result = []

        for n in nums2:
            if counts[n] > 0:
                result.append(n)
                counts[n] -= 1

        return result

# Hashmap - Counter
# Time: O(n+m)
# Space: O(n)

'''
Solution 1. 
class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        
        nums1.sort()
        nums2.sort()

        i, j = 0, 0
        result = []

        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                result.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1

        return result

# Sorting + Two Pointers
# Time: O(n+m)
# Space: O(n)


'''
