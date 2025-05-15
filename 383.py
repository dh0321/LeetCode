class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        magazineDict = {}

        for cha in magazine:
            if cha not in magazineDict:
                magazineDict[cha] = 1
            else:
                magazineDict[cha] += 1

        for cha in ransomNote:
            if cha not in magazineDict or magazineDict[cha] <= 0:
                return False
            else:
                magazineDict[cha] -= 1

        return True


'''
Solution1.
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        maga_hash = {}

        for c in magazine:
            maga_hash[c] = 1 + maga_hash.get(c, 0)

        for c in ransomNote:
            if c not in maga_hash or maga_hash[c] <= 0:
                return False
            maga_hash[c] -= 1
        
        return True

Solution2.
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        # Create a dictionary to store character counts
        dictionary = {}

        # Iterate through the magazine and count characters
        for char in magazine:
            if char not in dictionary:
                dictionary[char] = 1
            else:
                dictionary[char] += 1

        # Iterate through the ransom note and check character counts
        for char in ransomNote:
            if char in dictionary and dictionary[char] > 0:
                dictionary[char] -= 1
            else:
                return False
        
        return True

Solution3.
from collections import Counter

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        ransom_count = Counter(ransomNote)
        magazine_count = Counter(magazine)

        for char, count in ransom_count.items():
            if magazine_count[char] < count:
                return False

        return True

'''
