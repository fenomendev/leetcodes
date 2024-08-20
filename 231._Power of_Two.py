class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        count=0
        i=0
        if n<=0:
            return True
        while(1<n):
            if n%2==0:
                count+=1
            n=n/2
            i+=1
        if count==i:
            return True
        return False

ob=Solution()
print(ob.isPowerOfTwo(16))