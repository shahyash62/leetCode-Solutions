class Solution:
    def nCr(n, r):
        factN = 1
        factR = 1
        factNminusR = 1
        nMinusr = n - r
        while(n > 0):
            factN *=  n
            n -= 1
        while(r > 0):
            factR *=  r
            r -= 1
        while(nMinusr > 0):
            factNminusR *=  nMinusr
            nMinusr -= 1
        return (int(factN/(factNminusR * factR)))
                
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        return (int(Solution.nCr(2*n,n)/(n + 1)))
