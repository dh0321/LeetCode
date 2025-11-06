class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        count = {}
        result = []

        for num in nums1:
            count[num] = True
            # count[num] = count.get(num, 0) + 1

        for num in nums2:
            if num in count:
                result.append(num)
                del(count[num])

        return result

# Hash Table -> Not best answer
# Time: O(n+m)
# Space : O(n)


'''
Solution 1.
Using 'set'
Time: O(n+m)
Space: O(n+m)

def intersection(self, nums1, nums2):
    return list(set(nums1) & set(nums2))



Solution 2.
Using 'sort' and 'two pointer'
Time: O(n log n + m log m)
Space: O(k) or O(1)

def intersection(self, nums1, nums2):
    nums1.sort()
    nums2.sort()
    result = set()
    i = j = 0

    while i < len(nums1) and j < len(nums2):
        if nums1[i] == nums2[j]:
            result.add(nums1[i])
            i += 1
            j += 1
        elif nums1[i] < nums2[j]:
            i += 1
        else:
            j += 1
            
    return list(result)


'''




