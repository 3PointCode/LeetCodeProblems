from typing import List

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashset = set()         # creating hashset so we can check if the value is already there

        for number in nums:          # iterating through every number in our list
            if number in hashset:    # check if current number is already in hashset
                return True     # if it is then we return true
            hashset.add(number)      # otherwise we add the number and go to the next one
        return False            # if we iterated through all the numbers we return False

if __name__ == "__main__":
    nums_t = [1, 2, 3, 1]
    nums_f = [1, 2, 3, 4]
    solution = Solution()
    print(solution.hasDuplicate(nums_t))
    print(solution.hasDuplicate(nums_f))
