class Solution:
    def pow(self, x,n):
        if n == 0:
            return 1
        print(x,n)
        a = self.pow(x,int(n//2))
        if n&1:
            return a*a*x
        return a*a

    def myPow(self, x: float, n: int) -> float:
        if x == 0: return 0
        if n == 0: return 1
        if n < 0: return 1/self.myPow(x, -n)
        a = self.pow(x,int(n//2))
        if n&1:
            return a*a*x
        return a*a

s =Solution()
r = s.myPow(2,10)
print(r)