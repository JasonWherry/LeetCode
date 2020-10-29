def lengthOfLongestSubstring(s: str) -> int:
    length = len(s)
    i = 0
    
    # base case:
    if length == 0:
        return 0
    elif length == 1:
        return 1
    else:
        maxSub = 0
        visited = [] # store visited characters
        count = 0
    
        while i < length:
            if s[i] not in visited:
                count += 1
                visited.append(s[i])
                i += 1
                maxSub = max(maxSub, count)
            else:
                maxSub = max(maxSub, count)
                loc = visited.index(s[i]) # location of first match
                visited = visited[loc+1:]
                visited.append(s[i])
                count = len(visited)
                i += 1
                
        return maxSub