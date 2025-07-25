class Solution(object):
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

'''
Solution 1.
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



