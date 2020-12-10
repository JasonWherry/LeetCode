'''
First of all, this is one of the most difficulty problems. It is hard to think through all different cases. The problem should be simplified to handle 2 basic cases:

the second char of pattern is "*"
the second char of pattern is not "*"
'''
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        x = re.search(p, s)
        if x and x.group() == s:
            print(x, x.group())
            return True
        else:
            return False