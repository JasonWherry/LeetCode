from functools import lru_cache
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0 or len(digits) >= 5:
            return []
        
        # dictionary to hold lists of chars 
        table = {
                '2': ['a', 'b', 'c'], 
                '3': ['d', 'e','f'], 
                '4': ['g', 'h', 'i'], 
                '5': ['j', 'k', 'l'], 
                '6': ['m', 'n', 'o'], 
                '7': ['p', 'q', 'r', 's'],
                '8': ['t', 'u', 'v'], 
                '9': ['w', 'x', 'y', 'z']
                 }
        ret = []    # the list to be returned
        length = len(digits)    # length of each combo
        
        @lru_cache(maxsize=None)
        def recur(pos, s, curr):
            if len(curr) == length:
                ret.append(curr[:])
                return
            
            number = s[pos]
            for char in table[number]:
                recur(pos+1, s, curr+char)  # call again with updated char in group and updated str curr
            
        recur(0, digits, '')    # first call
        return ret