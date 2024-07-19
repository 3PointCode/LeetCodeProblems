from collections import Counter

# Time complexity should be O(n) where n is the length of both strings and memory complexity should be O(s + t)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):        # if the length is not the same in both strings we can return False immediately
            return False

        countS, countT = {}, {}     # Creating HashMaps for both string if length of them is the same

        for i in range(len(s)):     # filling HashMaps with values
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)

        for character in countS:    # Checking if each character has the same count in both strings
            if countS[character] != countT.get(character, 0):
                return False

        return True

# Solution with less memory used than the basic one, time complexity should stay the same but depends on Counter object
class Solution2:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)     # with the use of Counter object


# Solution with less memory used than the basic solution, time complexity is based on sorted function complexity
class Solution3:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)       # while sorted both string should be exactly the same


if __name__ == "__main__":
    s = "nabana"
    t = "banana"

    solution = Solution()
    solution2 = Solution2()
    solution3 = Solution3()

    print(solution.isAnagram(s, t))
    print(solution2.isAnagram(s, t))
    print(solution3.isAnagram(s, t))