class Matrix:
    def __init__(self, A):
        self.data = A

    def show(self):
        for i in range(3):
            for j in range(3):
                print(f'{self.data[i][j]:^6}', end=' ')
            print()

    def plus(self, any):
        A = self.data
        B = any.data
        ans = [[A[i][j] + B[i][j] for j in range(3)] for i in range(3)]
        return Matrix(ans)

    def minus(self, any):
        A = self.data
        B = any.data
        ans = [[A[i][j] - B[i][j] for j in range(3)] for i in range(3)]
        return Matrix(ans)

    def multiply(self, any):
        A = self.data
        B = any.data
        ans = [ [ sum( A[i][k] * B[k][j] for k in range(3)) for j in range(3)] for i in range(3) ]
        return Matrix(ans)

    def det(self):
        Z = []
        for i in range(3):
            Z.append(self.data[i])
            Z[i].append(self.data[i][0])
            Z[i].append(self.data[i][1])
        a = 0
        b = 0
        for i in range(2, -1, -1):
            x = 1
            for j in range(3):
                x *= Z[j][i+j]
            a += x
        for i in range(4, 1, -1):
            x = 1
            for j in range(3):
                x *= Z[j][i-j]
            b += x
        return a-b
