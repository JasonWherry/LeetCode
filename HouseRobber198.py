'''
You are a professional robber planning to rob houses along a street. 
Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them 
is that adjacent houses have security system connected and it will automatically contact the police if 
two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, 
determine the maximum amount of money you can rob tonight without alerting the police.

Method used --> 

'''

import unittest

def rob(nums) -> int:
    evenSum = 0
    oddSum = 0
    
    for i in range(len(nums)):
        if i % 2 == 0:
            # choose max of evenSum + current money or the last number calculated
            evenSum = max(evenSum + nums[i], oddSum) 
        else:
            oddSum = max(oddSum + nums[i], evenSum)
            
    return max(evenSum, oddSum)

class TestRob(unittest.TestCase):
	
	def testRob(self):
		nums1 = [2, 1, 1, 2, 1, 3]
		# expected value = 2 + 2 + 3 => 7
		self.assertEqual(rob(nums1), 7) 

		nums2 = [2,1,1,2]
		# expected value = 2 + 2 => 4
		self.assertEqual(rob(nums2), 4)

if __name__ == '__main__':
    unittest.main()