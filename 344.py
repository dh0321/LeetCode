class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        left_index = 0
        right_index = len(s) - 1

        while left_index < right_index:
            # it's for c or other language
            # temp = s[left_index]
            # s[left_index] = s[right_index]
            # s[right_index] = temp

            # python can do in one line
            s[left_index], s[right_index] = s[right_index], s[left_index]

            left_index += 1
            right_index -= 1

        return s


# Time: O(n)
# Space: O(1)
