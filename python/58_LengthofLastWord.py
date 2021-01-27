class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # base case
        if not s or len(s.strip()) == 0: 
            return  0
        
        else:
            # separate s into words
            words = s.split()
            # return length of last word in list of words
            return len(words[-1])
        
        
      