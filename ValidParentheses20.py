class Solution:
    def isValid(self, s: str) -> bool:
        # follow LIFO st we'll use a stack
        Dict = {
                '(': ')',
                '[': ']',
                '{': '}'
               }
        stack = []
        
        for char in s:
            # for every open char, push the respective closed char to stack
            if char in Dict:
                stack.append(Dict[char])
            else:
                if not stack or stack.pop() != char:
                    return False
        return not stack # stack is mpty so there was no extra symbols