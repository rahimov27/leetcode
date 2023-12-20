from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)


solution = Solution()
s = "hello"
t = "olleh"
result = solution.isAnagram(s, t)
print(result)
