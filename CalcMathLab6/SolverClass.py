from decimal import Decimal,getcontext

class Solver:
    def __init__(self,matrix,precision):
        self.precision = precision
        self.size = len(matrix)
        self.A = [[None] * self.size for _ in range(self.size)]
        for i in range(0, self.size):
            for j in range(0, self.size):
                self.A[i][j] = Decimal(str(matrix[i][j]))
        self.T = [[None] * self.size for _ in range(self.size)]
        self.B = [None] * self.size
        for i in range(0, self.size):
            self.B[i] = Decimal(str(matrix[i][-1]))
        self.Y = [None] * self.size
        self.X = [None] * self.size


    def setPrecision(self,precision):
        self.precision = precision

    def getRoots(self):
        if self.X[0] is None:
            return self.X
        X = [float(i) for i in self.X]
        return X

    def solve(self):
        buffer = self.A[0][0]
        for i in range(0,self.size):
            for j in range(0,self.size):
                buffer = max(buffer,self.A[i][j])
        buffer = len(str(int(buffer)))

        getcontext().prec=self.precision+buffer
        for i in range(0, self.size):#считаем матрицу T
            buffer = Decimal("0")
            for k in range(0, i):
                buffer = buffer + (self.T[k][i] ** 2)
            self.T[i][i] = (self.A[i][i] - buffer).sqrt()
            buffer = Decimal("0")
            for j in range(i + 1, self.size):
                for k in range(0, i):
                    buffer = buffer + self.T[k][i] * self.T[k][j]
                self.T[i][j] = ((self.A[i][j] - buffer) / self.T[i][i])

        for i in range(0,self.size):#проверяем наличие решений
            if self.T[i][i] == 0:
                return self.getRoots()

        self.Y[0] = self.B[0] / self.T[0][0]#считаем Y
        for i in range(1, self.size):
            buffer = Decimal("0")
            for k in range(0, i):
                buffer = buffer + (self.T[k][i] * self.Y[k])
            self.Y[i] = (self.B[i] - buffer) / self.T[i][i]
        self.X[-1] = self.Y[-1] / self.T[-1][-1]#считаем X
        for i in range(self.size - 2, -1, -1):
            buffer = Decimal("0")
            for k in range(i + 1, self.size):
                buffer = buffer + (self.T[i][k] * self.X[k])
            self.X[i] = (self.Y[i] - buffer) / self.T[i][i]
        return self.getRoots()

    def correctnessCheck(self):
        CheckArray = [None]*self.size
        for i in range(0,self.size):
            CheckArray[i] = self.B[i]
            for j in range(0,self.size):
                CheckArray[i] -= self.A[i][j]*self.X[j]
            CheckArray[i] = abs(CheckArray[i])
        CheckArray = [float(i) for i in CheckArray]
        return CheckArray
    def applicabilityCheck(self):
        for i in range(1,self.size):
            for j in range(0,i):
                if self.A[i][j]!=self.A[j][i]:
                    return "assymetrical matrix"
        for i in range(0,self.size):
            for j in range(0,self.size):
                if (self.A[i][i]>self.A[i][j]) or (i==j):
                    pass
                else:
                    return "no diagonal dominance"
        return 1




