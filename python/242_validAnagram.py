class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # sorted() returns a list of the argument's chars, sorted of course
        if sorted(s) == sorted(t):
            return True
        
        else: 
            return False