'''
Friend Circles

There are N students in a class. Some of them are friends, while some are not. 
Their friendship is transitive in nature. 
For example, if A is a direct friend of B, and B is a direct friend of C, then A is an indirect friend of C. 
And we defined a friend circle is a group of students who are direct or indirect friends.

Given a N*N matrix M representing the friend relationship between students in the class. 
If M[i][j] = 1, then the ith and jth students are direct friends with each other, otherwise not. 
And you have to output the total number of friend circles among all the students.

Method used --> Depth First Search ~ DFS

'''
def findCircleNum(M) -> int:
    circles = 0 # number of friend circles
    
    visited = set() # track nodes that are visisted
    
    for person in range(len(M)): # each row is a person
        if person not in visited:
            circles += 1
            dfs(person, M, visited)

    return circles            
    
def dfs(node, M, visited):
    for person, is_friend in enumerate(M[node]):
        if person not in visited and is_friend:
            visited.add(person)
            dfs(person, M, visited)

def test():
	arr = [	[1, 1, 0],
				[1, 1, 0],
				[0, 0, 1]	]

	arr2 = [	[1, 1, 1],
				[1, 1, 0],
				[1, 0, 1]	]

	if findCircleNum(arr2) > 1:
		print('There are {} friend circles'.format(findCircleNum(arr2)))
	else:
		print('There is {} friend circle'.format(findCircleNum(arr2)))

def main():
    test()

if __name__ == "__main__":
    main()