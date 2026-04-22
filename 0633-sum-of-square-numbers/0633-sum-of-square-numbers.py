import math
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        a = 0
        b = int(math.sqrt(c))
        while a <= b:
            total = a*a + b*b
            if total == c:
                return True
            if total > c:
                b -= 1
            else:
                a += 1
        return False                
            

        