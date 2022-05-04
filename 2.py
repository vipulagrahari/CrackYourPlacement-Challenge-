
# 75. Sort Colors
# Medium

# Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

# We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

# You must solve this problem without using the library's sort function.

from collections import Counter 

class Solution:
    
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        temp = Counter(nums)
        x,y,z = temp[0], temp[1], temp[2]
        # print(x,y,z)

        t = len(nums)
        i = 0
        while( i != t ):
        
            if(x>0):
                nums[i] = 0
                x -= 1
            elif(y>0):
                nums[i] = 1
                y -= 1
            elif(z>0):
                nums[i] = 2
                z -= 1
            i += 1
                
        