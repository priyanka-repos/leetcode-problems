# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/?envType=problem-list-v2&envId=array
# Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binary_search(nums, target, is_searching_left):
            left = 0
            right = len(nums) - 1
            idx = -1

            while left <= right:
                mid = (left + right) // 2
                if nums[mid] > target:
                    right = mid -1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    idx = mid
                    if is_searching_left:
                        right = mid - 1
                    else:
                        left = mid + 1
            return idx
        left = binary_search(nums, target, True)
        right = binary_search(nums, target, False)

        return [left, right]


        
