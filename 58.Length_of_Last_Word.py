class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s=s.split()
        return len(s[len(s)-1])
ob=Solution()
print(ob.lengthOfLastWord("Hello World sal"))