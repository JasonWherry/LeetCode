class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0 or len(digits) >= 5:
            return []
        
        # dictionary to hold lists of chars 
        table = {
                '2': 'abc', 
                '3': 'def', 
                '4': 'ghi', 
                '5': 'jkl', 
                '6': 'mno', 
                '7': 'pqrs',
                '8': 'tuv', 
                '9': 'wxyz'
                 }
        
        def dfs(i, curr, ret):
            if i == len(digits):
                if curr != "":
                    ret.append(curr[:])
                return
            for char in table[digits[i]]:
                dfs(i+1, curr+char, ret)
            
        
        ret = []    # the list to be returned
        dfs(0, '', ret)    # first call
        
        return ret