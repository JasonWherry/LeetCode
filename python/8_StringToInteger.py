'''
This problem taught me more about patience than anything.
'''
class Solution:
    def myAtoi(self, str: str) -> int:
        INT_MAX =  2147483647
        INT_MIN = -2147483648
        result = 0
        
        if not str: # empty string, return 0
            return result

        i = 0
        while i < len(str) and str[i] == ' ':   # check for whitespace
            i += 1  # iterate over whitespace

        sign = 1
        if i != len(str):
            if str[i] == '+':
                i += 1
            elif str[i] == '-':
                sign = -1
                i += 1
        else:
            return 0

        while i < len(str) and (str[i] >= '0' and str[i] <= '9'):
            result = (result * 10 + ord(str[i]) - ord('0') )
            if result > INT_MAX:
                return INT_MAX if sign > 0 else INT_MIN
            i += 1

        return sign * result