# 26. Remove Duplicates from Sorted Array
# Easy

# Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same.

# Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

# Return k after placing the final result in the first k slots of nums.

# Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        res = len(set(nums))
        x = len(nums) - res
        # nums = list(set(nums))
        
        t = nums[0]
        for i in range(1, len(nums)):
            if(nums[i] == t):
                nums[i] = 101
            elif(nums[i] != t):
                t = nums[i]
        
        nums.sort()
        
        return res
        
#approach: replace the duplicate elemnts with something bigger than the range given and then sort the array 