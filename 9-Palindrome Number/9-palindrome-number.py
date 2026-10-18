class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        return str(x) == str(x)[::-1]


print(Solution().isPalindrome(121))
print(Solution().isPalindrome(-121))
print(Solution().isPalindrome(10))
print(Solution().isPalindrome(9))
