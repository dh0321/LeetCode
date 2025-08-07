class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        mapping = {')': '(', '}': '{', ']': '['}

        for char in s:
            if char in mapping:
                if not stack or stack[-1] != mapping[char]:
                    return False
                stack.pop()
            else:
                stack.append(char)

        return not stack

# Time: O(n)
# Space: O(n) in worst case

'''
Solution 1.

def isValid(self, s):

    stack = []
    pair = {'(': ')', '{': '}', '[': ']'}

    for char in s:
        if char in pair:
            stack.append(pair[char])
        else:
            if not stack or stack.pop() != char:
                return False

    return not stack



'''
