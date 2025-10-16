class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
    
        count = {}
    
        for char in s:
            if char in count:
                count[char] += 1
            else:
                count[char] = 1
            # count[char] = count.get(char, 0) + 1
    
        for char in t:
            if char not in count:
                return False
            count[char] -= 1
            if count[char] < 0:
                return False
    
        return True


'''
Solution 1.
def isAnagram(self, s: str, t: str) -> bool:
    return sorted(s) == sorted(t)


Solution 2.
def isAnagram(self, s, t):
    if len(s) != len(t):
        return False
    
    count_s = [0] * 26
    count_t = [0] * 26
    
    for i in range(len(s)):
        count_s[ord(s[i]) - ord('a')] += 1
        count_t[ord(t[i]) - ord('a')] += 1
    
    return count_s == count_t
    
    # from collections import Counter
    # return Counter(s) == Counter(t)


Solution 3.
def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        if len(s) != len(t):
            return False

        count = [0] * 26

        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] += 1
            count[ord(t[i]) - ord('a')] -= 1

        for c in count:
            if c != 0:
                return False
        return True

        # return all(c == 0 for c in count)

# ord() returns ascii value of character

'''
