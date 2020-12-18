class Solution:
    def generateParenthesis(self, n):
        if n < 1 or n > 8:
            return []
   
        def dfs(ret, string, left, right):
            if left > right:
                return
            
            if left == 0 and right == 0:
                ret.append(string)
                return
            
            if left > 0:
                dfs(ret, string+'(', left-1, right)
                
            if right > 0:
                dfs(ret, string+')', left, right-1)


        ret = []
        dfs(ret, '', n, n)
        
        return ret

if __name__ == '__main__':
    print(Solution().generateParenthesis(2))


'''
case: n = 2 -> dfs(ret, '', n, n)
    # left = right = n
    
    self.dfs(ret, str + '(', left-1, right) left-1 = 1, right = 2
    {
        self.dfs(ret, str + '(', left-1, right) left-1 = 0, right = 2
        {
            self.dfs(ret, str + ')', left, right-1) left = 0, right-1 = 1
            {
                self.dfs(ret, str + ')', left, right-1) left = 0, right-1 = 0
                {   ret.append(str)
                    return
                }
            }
        }
        self.dfs(ret, str + ')', left, right-1) left = 1, right-1 = 1
        {
            self.dfs(ret, str + '(', left-1, right) left-1 = 0, right = 1
            {
                self.dfs(ret, str + ')', left, right-1) left = 0, right-1 = 0
                {
                    ret.append(str)
                    return
                }
            }
        }
    }


ret = ['(())', '()()']

'''

