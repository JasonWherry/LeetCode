'''
Option 1 ~ Brute Force

Option 2 ~ Dynamic Programming

Option 3 ~ Longest Common Substring

Option 4 ~ Expand Around the Center

Option 5 ~ Manacher's Algorithm

'''

def longestPalindrome(self, s: str) -> str:
    
    # return if string is empty
    if not s:
    	return s

    pal = ""
    for i in range(len(s)):
    	j = i + 1

    	# while j is <= string length & subtring length is >= to pal length
    	while j <= len(s): # and len(s[i:j]) >= len(pal):
    		
    		# if substring is a palindrome & subtring length is >= to pal length
    		if s[i:j] == s[i:j][::-1] and len(s[i:j]) >= len(pal):
    			sub = s[i:j]

    		j += 1

    return pal