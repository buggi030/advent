class Solution:
    def multiply_two(self, num1: str, num2: str) -> str:
        print(num1, num2)
        n = len(num1)
        r_num1 = num1[::-1]
        r_num2 = num2[::-1]
        m = len(num2)
        result = []
        memory = 0
        j = 0
        while j<len(r_num2):
            r = 0
            for i in range(j+1):
                print(j , (i, j - i),r_num2[i], r_num1[j - i])
                r += int(r_num2[i])* int(r_num1[j - i])
            total = r + memory
            toAppend = total % 10
            result.append(str(toAppend))
            memory = total // 10
            print(memory, toAppend, result)
            j+=1
        result.append(str(memory))
        return ''.join(result[::-1])
#         for i in range(1,len(num2)+1):
#             result.append(0)
#             a = num2[len(num2)-i]
#             for j in range(1, len(num1)+1):
#                 b = num1[len(num1)-j]
#                 print(a,'*',b)

    def multiply(self, num1: str, num2: str) -> str:
        _ = 0
        endResult = None
        for multiplier in num2[::-1]:
            result = self.simpleMultiply(num1, int(multiplier))
            if endResult is None:
                endResult = result
            else:
                endResult = self.mergeArrays(endResult, ['0'] * _ + result)
            _ += 1
        return ''.join(endResult[::-1])

    def simpleMultiply(self, multiplicand, multiplier):
        result = []
        memory = 0
        for i in range(len(multiplicand)-1,-1,-1):
            multiplied = multiplier * int(multiplicand[i])
            value = memory + multiplied % 10
            result.append(str(value))
            memory = multiplied // 10
        return result

    def mergeArrays(self, arr1, arr2):
        memory = 0
        returnArray = arr1 if len(arr1)>len(arr2) else arr2
        for i in range(len(returnArray)):
            a = arr1[i] if i < len(arr1) else '0'
            b = arr2[i] if i < len(arr2) else '0'
            sum = memory + int(a) + int(b)
            returnArray[i] = str(sum % 10)
            print(returnArray)
            memory = sum // 10
        if memory != 0:
            returnArray.append(str(memory))
        return returnArray
s = Solution()

# print(s.multiply('2', '3'))
# print(s.multiply('9', '9'))
# print(s.multiply('123', '56'))
# print(s.multiply('123', '456'))
print(s.multiply_two('123', '456'))