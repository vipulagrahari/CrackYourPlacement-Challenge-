
# 283. Move Zeroes
# Easy

# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

# Note that you must do this in-place without making a copy of the array.

#approach: Delete all the zeroes using a while loop and add them in the end while creating a counter.

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        x = len(nums)
        i = 0
        counter = 0
        while(i != x):
            if(nums[counter] == 0):
                del nums[counter]
            else:
                counter += 1
            i += 1
        for i in range(x-len(nums)):
            nums.append(0)
        print(nums)