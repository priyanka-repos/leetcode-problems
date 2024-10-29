# https://leetcode.com/problems/two-sum/description/?envType=problem-list-v2&envId=array
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(n-1):
            for j in range(i+1, n):
                if nums[i] + nums[j] == target:
                    return [i,j]
        return []            
        
