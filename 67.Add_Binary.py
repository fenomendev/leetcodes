class Solution:
    def addBinary(self, a: str, b: str) -> str:
        num1=int(a,2)
        num2=int(b,2)
        sum=num1+num2
        return int(str(bin(sum))[2:])
obeykt=Solution()
print(obeykt.addBinary("11","1"))