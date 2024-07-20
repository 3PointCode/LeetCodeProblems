from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:     # starting from number of index 1 because the array is sorted
        left = 1                                # left pointer that points to current value in the array and overall number of unique values

        for right in range(1, len(nums)):       # right pointer is used to compare value at its index with value at index left
            if nums[right] != nums[right - 1]:  # if value at index right is different from the value of right-1 it means that its a new unique value
                nums[left] = nums[right]        # swap the place of the new unique value with the use of our left pointer
                left += 1                       # increment left pointer so it moves to the next index

        return left

if __name__ == "__main__":
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    solution = Solution()
    print(solution.removeDuplicates(nums))