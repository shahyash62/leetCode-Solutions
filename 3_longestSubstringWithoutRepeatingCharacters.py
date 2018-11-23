class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = len(s)
        tList = []
        maxCount = 0
        count = 0
        i = 0
        while (i < length):
            if (s[i] not in tList):
                tList.append(s[i])
                i += 1
            else:
                count = len(tList)
                del tList[0]
                if(count > maxCount):
                    maxCount = count
        if(len(tList) > maxCount): maxCount = len(tList)
        return maxCount
