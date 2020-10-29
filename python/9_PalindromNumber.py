# solved it with converting the integer to a string:

def isPalindrome(x) -> bool:
    y = str(x)
    length = len(y)
    result = False
    
    if length == 0:
        return result
    elif length == 1:
        result = True
        return result
    else:
        # result = False
        start = 0
        end = length - 1
        while start <= end:
            if y[start] == y[end]:
                start += 1
                end -= 1
                result = True
            else:
                return False
            
    return result

assert isPalindrome(121) == True
'''
STEPS, Without converting the integer to a string:
    - check base cases
    - reverse half of the integer
    - compare halfs for equality
        odd number is special case
    - return result -> boolean
'''

def isPalindrome2(x) -> bool:
    if x == 0:
        return True

    # base case: x is negative or a multiple of 10
    if x < 0 or x % 10 == 0:
        return False

    revInt = 0
    while(x > revInt):
        pop = x % 10
        x = int(x / 10)
        revInt = (revInt * 10) + pop

    if x == revInt or x == int(revInt / 10):
        return True
    else:
        return False

assert isPalindrome2(121) == True

assert isPalindrome2(12321) == True

assert isPalindrome2(122321) == False