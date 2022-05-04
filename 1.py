
# sort the array and traverse in a linear fassion so that you get the repeating number.


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        x = nums[0]
        res = 0
        for i in range(1,len(nums)):
            if(nums[i] == x):
                res = x
            else:
                x = nums[i]
        return res            