class Solution:
    def isPalindrome(self, s: str) -> bool:
        return self.v1(s)

    def v2(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left <= right:
            leftStr, rightStr = s[left].lower(), s[right].lower()
            if leftStr.isalnum() and rightStr.isalnum():
                if leftStr != rightStr:
                    return False
                else:
                    left, right = left + 1, right - 1
                    continue
            left += not leftStr.isalnum()
            right -= not rightStr.isalnum()
        return True
    # Time Complexity: O(N)
    # Space Complexity: O(1)

    def v1(self, s: str) -> bool:
        s = ''.join(filter(str.isalnum, s)).lower()
        left, right = 0, len(s) - 1
        while left <= right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True
    # Time Complexity: O(N)
    # Space Complexity: O(N)


print(Solution().isPalindrome("asa1"))
