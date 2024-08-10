from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> List[int]:
        lastIndex = m + n - 1                       # Set lastIndex to the value of last index in nums1 array

        while m > 0 and n > 0:                      # while both m and n pointers are bigger than 0
            if nums1[m - 1] > nums2[n - 1]:         # if the last number in nums1 is bigger than the last one in nums2
                nums1[lastIndex] = nums1[m - 1]     # we put this bigger number at the end of nums1 because both arrays are already sorted
                m -= 1                              # decrement the m pointer in nums1
            else:
                nums1[lastIndex] = nums2[n - 1]     # otherwise we do the same thing but we take a number from nums2 instead
                n -= 1                              # decrement the n pointer in nums2
            lastIndex -= 1                          # decrement the lastIndex value as we now look to put the smaller number
        return nums1

if __name__ == "__main__":
    nums1 = [1, 2, 3, 0, 0, 0]
    nums2 = [2, 5, 6]
    m, n = 3, 3
    solution = Solution()
    print(solution.merge(nums1, m, nums2, n))

