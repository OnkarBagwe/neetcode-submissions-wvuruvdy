class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        divisor = 1

        while x >= divisor*10:
            divisor *= 10

        while x:
            left = x // divisor
            right = x % 10

            if left != right:
                return False
            
            x = x % divisor #chop left
            x = x // 10 #chop right
            divisor = divisor // 100

        return True