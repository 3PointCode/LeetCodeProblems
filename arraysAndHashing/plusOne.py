from typing import List

def plusOne(digits: List[int]) -> List[int]:
    digits = digits[::-1]           # reverse digits to go from behind
    carry, index = 1, 0             # set carry to 1 and index to 0

    while carry:
        if index < len(digits):     # check if index is less than len(digits) so we are not out of bounds
            if digits[index] == 9:  # check if the digit at current index is 9
                digits[index] = 0   # if it was 9, then set its value to 0 and leave the carry equal to 1
            else:
                digits[index] += 1  # if the number at current index was different from 9 we can simply add 1 to it
                carry = 0           # set carry to 0 to break out of the loop
        else:                       # if index was bigger than length
            digits.append(1)        # append 1 to the end of our array
            carry = 0               # set carry to 0 to break out of the loop
        index += 1

    return digits[::-1]             # reverse array again so its in correct order

if __name__ == "__main__":
    digits = [1, 2, 4]
    digits2 = [9, 9, 9]
    print(plusOne(digits))
    print(plusOne(digits2))
