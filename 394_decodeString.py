class Solution:
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        #s = '1[a2[b3[c]]]'
        stack = []
        numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        count = 0
        while (count < len(s)):
            flag = False
            tempInt = 0
            tempStr = ''
            while(s[count] in numbers and count < len(s)):
                tempInt = int(s[count]) + (tempInt*10)
                count += 1
                flag = True
            if(flag):
                stack.append(tempInt)
                continue
            if(s[count] == '[' or s[count] == ']'):
                stack.append(s[count])
                count += 1
                continue
            else:
                while(count < len(s) and (s[count] not in numbers and s[count] != '[' and s[count] != ']')):
                    tempStr = tempStr + s[count]
                    count += 1
                stack.append(tempStr)
        print(stack)
        s = stack
        stack = []
        for x in s:
            tempStr = ''
            result = ''
            multiplier = 1
            if(x == ']'):
                temp = stack.pop()
                while(temp != '['):
                    tempStr = temp + tempStr
                    temp = stack.pop()
                else:
                    multiplier = stack.pop()
                while(multiplier > 0):
                    result = tempStr + result
                    multiplier -= 1
                stack.append(result)
            else:
                stack.append(x)
        result = ''
        for x in stack:
            result = result + x
        return result
