class MyMath:
    def __init__(self):
        total = float(3.00)
        st = 2 
        for i in range(50):
            if i%2==0 : total += 4/(st*(st+1)*(st+2))
            else : total -= 4/(st*(st+1)*(st+2))
            st += 2
        self.pi = total 
    def is_even(self,num):
        if num % 2 == 0 : return True
        else : return False
    def fac(self,num):
        ans = 1
        for i in range(1,num+1):
            ans *= i
        return ans
    def is_prime(self,num):
        n = num
        prime = [True for i in range(n+1)] 
        p = 2
        while (p * p <= n): 
            if (prime[p] == True): 
                for i in range(p * p, n+1, p): 
                    prime[i] = False
            p += 1
        if prime[num] : return True
        else : return False
    def divide_by(self,num,k):
        if num % k == 0 : return True
        else : return False
    def ten_to_any(self,num,an):
        arr = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
        dec = num
        ans = ''
        while(dec > 0):
            ans = str(arr[dec % an]) + ans
            dec = dec // an
        return ans
    def ten_to_bi(self,num):
        return self.ten_to_any(num,2)
    def ten_to_oct(self,num):
        return self.ten_to_any(num,8)
    def ten_to_sixteen(self,num):
        return self.ten_to_any(num,16)
    def int_to_roman(self,num):
        val = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
            ]
        syb = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
            ]
        roman_num = ''
        i = 0
        while  num > 0:
            for _ in range(num // val[i]):
                roman_num += syb[i]
                num -= val[i]
            i += 1
        return roman_num