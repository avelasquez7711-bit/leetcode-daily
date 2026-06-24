''' 
This is my solution for the Two Sum problem on Leetcode. 

Complexity:
    Time Complexity: O(n) - Single pass through the list with O(1) hash map lookups.
    Space Complexity: O(n) - Storing up to n elements in the dictionary.

Problem: 
    Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
    You may assume that each input would have exactly one solution, and you may not use the same element twice.
    You can return the answer in any order.
'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # tracks previously seen values and indices for O(1) lookups
        num_to_index = {}  

        for index, num in enumerate(nums):
            complement = target - num 

            # check if matching pair needed for target was processed
            if complement in num_to_index:
                return [num_to_index[complement], index]
            else:
                num_to_index[num] = index  # save current number to index

        return []  # no solution
