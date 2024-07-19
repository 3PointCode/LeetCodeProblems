from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}                                    # map of previous values, value : index

        for index, number in enumerate(nums):           # enumerate through indexes and values
            difference = target - number                # set difference to target - current number
            if difference in prevMap:                   # if difference is already in our map
                return [prevMap[difference], index]     # we return index of the current number and index of number equal to difference
            prevMap[number] = index                     # assign current index as value to its key - number

if __name__ == "__main__":
    solution = Solution()
    nums = [2, 1, 5, 3]
    target = 4
    print(solution.twoSum(nums, target))
