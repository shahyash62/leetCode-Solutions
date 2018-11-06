class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        temp = x
        y = 0
        while temp > 0 :
            y = temp % 10 + (y*10)
            temp = int(temp/10)
        print(y)
        if y == x:
            return True
        else:
            return False
