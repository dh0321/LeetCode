class Solution(object):
    def merge(self, nums1, m, nums2, n):

        i, j, k = m - 1, n - 1, m + n - 1
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1

        # if nums2 still has values
        while j >= 0:
            nums1[k] = nums2[j]
            k -= 1
            j -= 1

# Time: O(n+m)
# Space: O(1)


'''
Solution 1.
def merge(self, nums1, m, nums2, n):
    nums1[m:] = nums2
    nums1.sort()
    print(nums1)

# Time: O((m + n) log(m + n))  becuase of sort
# Space: O(1)

'''
        
