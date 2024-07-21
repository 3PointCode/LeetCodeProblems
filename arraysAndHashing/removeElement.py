from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        currentIndex = 0                # setting currentIndex to 0, it is also the value that indicates how many non val values we have

        for right in range(len(nums)):  # iterating through nums with right pointer
            if nums[right] != val:      # if value at index right is different from the val
                nums[currentIndex] = nums[right]    # swap the value at currentIndex with the value at index right
                currentIndex += 1                   # increment currentIndex and also the current number of non val values

        return currentIndex

if __name__ == "__main__":
    solution = Solution()
    nums = [0, 1, 2, 2, 3, 0, 4, 2]
    print(solution.removeElement(nums, 2))
