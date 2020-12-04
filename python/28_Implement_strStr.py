class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0
            # needle is empty
    
        else:
            # search for needle
            result = haystack.find(needle)
            # return the index of the first occurrence of needle in haystack
            if result != -1:
                return result         
        
        # needle is not part of haystack
        return -1