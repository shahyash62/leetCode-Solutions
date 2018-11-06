class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        str = str.strip()
        number = ['0','1','2','3','4','5','6','7','8','9']
        sign = ['-', '+']
        isNegative = False
        result = ''
        multiplier = 1
        if (len(str) == 0):
            return 0
        fC = str[0]
        if ((len(str) == 1 and fC not in number) or (fC not in sign and fC not in number)):
            return 0
        if(len(str) == 1 and fC in number):
            return (int(str))
        sC = str[1]
        if (sC not in number and fC not in number):
            return 0
        if(fC in sign):
            result = fC
        index = 0
        for s in str:
            if(s in number):
                result = result + s
            else:
                if(s in sign and index == 0):
                    continue
                break
            index += 1
        print(result)
        resultInt = int(result)
        if (resultInt > 2147483647):
            resultInt = 2147483647
        elif(resultInt < -2147483648):
            resultInt = -2147483648
        return resultInt
