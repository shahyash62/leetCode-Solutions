class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        largestStr = ''
        count = 1
        if(len(s) == 1):
            return s
        while (count < len(s)):
            tempStr = s[count]
            tempStr2 = s[count]
            pre = count - 1
            nex = count + 1
            while (pre > -1 and nex < len(s) and s[pre] == s[nex]):
                tempStr = s[pre] + tempStr +s[nex]
                pre -= 1
                nex += 1     
            pre = count - 1
            nex = count + 1
            if(pre > -1 and s[pre] == s[count]):
                tempStr2= s[pre] + s[count]
                #print (tempStr2)
                pre = pre - 1
                while (pre > -1 and nex < len(s) and s[pre] == s[nex]):
                    tempStr2 = s[pre] + tempStr2 +s[nex]
                    pre -= 1
                    nex += 1
            #print(len(largestStr))
            #print(tempStr)
            #print(tempStr2)
            if(len(tempStr) > len(largestStr)):
                largestStr = tempStr
            if(len(tempStr2) > len(largestStr)):
                largestStr = tempStr2
            count += 1
        return largestStr
