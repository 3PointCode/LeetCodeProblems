from typing import List

def searchInsert(nums: List[int], target: int) -> int:
    left, right = 0, len(nums) - 1      # initialization of left and right pointers, left is 0 and right is at the last index

    while left <= right:                # while left is smaller than right
        middle = (left + right) // 2    # set middle to average of left and right

        if nums[middle] == target:      # if the number at index middle is the same as our target we return the middle index
            return middle

        if target > nums[middle]:       # if target is bigger than the value at index middle we shift our left pointer
            left = middle + 1           # to the next index to the right from middle as middle was already checked
        else:                           # if target is smaller than the value at index middle we shift our right pointer
            right = middle - 1          # to the next index to the left from middle

    return left                         # if target wasn't found we return left pointer as its position gives as the index to insert the new value

if __name__ == "__main__":
    nums = [1, 3, 5, 6]
    print(searchInsert(nums, 2))
    print(searchInsert(nums, 5))