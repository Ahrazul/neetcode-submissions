class Solution:
    def tribonacci(self, n: int) -> int:
        n1,n2,n3 = 0,1,1

        if not n:
            return 0

        for _ in range(n-2):
            temp = n1
            n1 = n2
            n2 = n3
            n3 = temp + n1 + n3

        return n3
        