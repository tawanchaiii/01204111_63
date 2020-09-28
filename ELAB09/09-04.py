class py_solution:
    def __init__(self,L):
        self.L = L
        self.stack = []
        self.A = ['(','[','{']
        self.B = [')',']','}']
    def is_valid_parentheses(self):
        for i in self.L :
            if i in self.A :
                self.stack.append(i)
            else : 
                if len(self.stack) == 0 : return False 
                else :
                    ind = self.re(self.stack[-1])
                    if (i == self.B[ind]) : self.stack.pop()
                    else : return False 
        if len(self.stack) != 0 : return False
        return True
    def re(self,q):
        for i in range(len(self.B)):
            if self.A[i] == q : return i 
            
st = input('input: ')
ob = py_solution(st)
if ob.is_valid_parentheses() : 
    print("valid parentheses")
else :
    print("invalid parentheses")