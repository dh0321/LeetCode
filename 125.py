class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left_idx = 0
        right_idx = len(s) - 1

        while left_idx < right_idx:
            if not s[left_idx].isalnum():
                left_idx += 1
                continue

            if not s[right_idx].isalnum():
                right_idx -= 1
                continue

            if s[left_idx].lower() == s[right_idx].lower():
                left_idx += 1
                right_idx -= 1
            else:
                return False
        return True

'''
Solution 1.

def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        i = 0
        j = len(s) - 1

        while i < j:
            while i < j and not s[i].isalnum():
                i += 1
            while i < j and not s[j].isalnum():
                j -= 1

            if s[i].lower() != s[j].lower():
                return False

            i += 1
            j -= 1

        return True

# Time: O(n)
# Space: O(1)

Solution 2.

def isPalindrome(self, s):
    """
    :type s: str
    :rtype: bool
    """
    filtered = ''.join(c.lower() for c in s if c.isalnum())
    if filtered == filtered[::-1]:
        return True
    else:
        return False

    # return filtered == filtered[::-1]

# Space : O(n)  # need to make new string
'''



