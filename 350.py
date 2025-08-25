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
# do not use Counter
# Counter return none value automatically, but dict should check it.

def intersect(self, nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: List[int]
    """
    counts = {}
    result = []

    for num in nums1:
        counts[num] = counts.get(num, 0) + 1

    for num in nums2:
        if num in counts and counts[num] > 0:
            result.append(num)
            counts[num] -= 1

    return result


Solution 2. 
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
