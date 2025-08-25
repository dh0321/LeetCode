class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        freq = {}
        for char in s:
            freq[char] = freq.get(char, 0) + 1

        for i, char in enumerate(s):
            if freq[char] == 1:
                return i

        return -1

# Time: O(n)

'''
Solution 1.

def firstUniqChar(self, s):
    """
    :type s: str
    :rtype: int
    """
    count = Counter(s)
    for i, char in enumerate(s):
        if count[char] == 1:
            return i

    return -1

# Time: O(n)

'''

