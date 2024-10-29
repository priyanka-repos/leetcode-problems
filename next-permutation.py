# https://leetcode.com/problems/next-permutation/?envType=problem-list-v2&envId=array
# A permutation of an array of integers is an arrangement of its members into a sequence or linear order

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = len(nums) -2
        while i >= 0 and nums[i] >= nums[i+1]:
            i-=1
        if i == -1:
            return nums.reverse()

        for n in sorted(nums[i+1:]):
            if n > nums[i]:
                break
        j = nums[i+1:].index(n)

        nums[i], nums[i+j+1] = nums[i+j+1], nums[i]
        nums[i+1:] = sorted(nums[i+1:])
        return nums
