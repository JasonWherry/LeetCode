class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0 or len(digits) >= 5:
            return []
        
        table = ['0','1', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs',
                 'tuv', 'wxyz']
        ret = ['']  # needed by the list comprehension below
        
        # loops through each group of letters ex. 'a', 'b', 'c' for 'abc'
        for char in digits:
            if int(char) < 2 or int(char) > 9:
                pass
            else:
                group = table[int(char)]
                # make all combos of 2 letters within the range returned by the input
                ret = [pre + letter for pre in ret for letter in group]
        
        return ret