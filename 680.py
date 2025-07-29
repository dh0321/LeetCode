class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        def is_palindrome_range(left_index, right_index):
            while left_index < right_index:
                if s[left_index] != s[right_index]:
                    return False

                left_index += 1
                right_index -= 1

            return True


        left_index = 0
        right_index = len(s) - 1

        while left_index < right_index:
            if s[left_index] != s[right_index]:
                return is_palindrome_range(left_index + 1, right_index) or is_palindrome_range(left_index, right_index - 1)

            left_index += 1
            right_index -= 1

        return True

# Time: O(n)
# Space: O(1)
