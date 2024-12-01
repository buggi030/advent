import sys
import math

n,k = sys.argv[1:]
n,k = int(n), int(k)

class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        print(n,k)
        if n==1:
            return '0'
        prev = self.kthGrammar(n-1,math.ceil(k/2))
        new = []
#         print()
        for i in prev:
            new.append('01' if i == '0' else '10')
#         print(k,new)
        return ''.join(new)[k-1]

s = Solution()
answer = s.kthGrammar(n,k)
print(answer)