# Palindrome Number
# 29.10.2025
# 4ms 80.02%
# 17.98 19.81%
# Solution 1
class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]


# 29.10.2025
# 7ms 62.53%
# 18mb 19.81%
# Solution 2
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        if x == 0:
            return True
        org = x
        rev = 0
        while org:
            rev = rev * 10 + org%10
            org = org//10
        return x == rev
