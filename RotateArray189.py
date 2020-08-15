'''
Rotate Array - 189

Method 1 ~ reverse whole array, then subarrays
	rotate alg:
	    reverse the entire array: [1, 2, 3, 4, 5, 6] -> [6, 5, 4, 3, 2, 1]
	    reverse the sub arrays, determined by the shift, k

Method 2 ~ pop and replace
    rotate alg:
    	loop from 0 to k:
	    	store last item in the array
        	insert the item in the front

'''

# METHOD 1
def reverseArr(self, arr, start, end): # Runtime: 56 ms
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

def rotate(self, nums, k) -> None: # Runtime 
    n = len(nums)
    k %= n

    reverseArr(nums, 0, n - 1)
    reverseArr(nums, 0, k - 1)
    reverseArr(nums, k, n - 1)


# METHOD 2
def rotate(self, nums, k): # Runtime 
    for i in range(k):
        temp = nums.pop()
        nums.insert(0, temp)

