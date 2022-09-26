class Solution:
    def sum(self, num1: int, num2: int) -> int:
        return num1 + num2

class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        str_num = str(num)
        return sum(
            num % int(str_num[i - k:i]) == 0
            for i in range(k, len(str_num) + 1)
            if int(str_num[i - k:i]) != 0)
        
class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        if n % 2 ==0 and n < n * 2:
            return n
        return n * 2
    
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count=0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if(nums[i]==nums[j]):
                    count+=1
        return count

class Solution:
    def minimumSum(self, num: int) -> int:
        _arr = list(str(num))
        _arr.sort()
        
        return (int(_arr[0]+_arr[3])) + (int(_arr[1]+_arr[2]))
class Solution:
 def subtractProductAndSum(self, n: int) -> int:
        digit_prod = 1
        digit_sum = 0
        for i in range(len(str(n))):
            digit_prod *= int(str(n)[i]) 
            digit_sum += int(str(n)[i])
        return digit_prod - digit_sum 
class Solution:
    def numberOfSteps(self, num: int) -> int:
        count=0
        while num:
            count+=1
            if num%2==0:
                num=num/2
            else:
                num-=1
                
                
        return count

class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        first = start
        for i in range(1, n):
            first ^= (start + 2 * i)
        
        return first