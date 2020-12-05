class Solution:
    def __init__(self):
        self.count:int = 1
            
    def countAndSay(self, n: int) -> str:
        return self.recursiveSay(n)

    def recursiveSay(self, n: int) -> str:
        if n == 1:
            return "1"
        
        result = ''
        recSay = self.recursiveSay(n - 1) + '$'
        
        for i in range(1, len(recSay)):
            if recSay[i-1] == recSay[i]:
                self.count += 1
            else:
                result += str(self.count) + recSay[i-1] 
                self.count = 1
        
        return result