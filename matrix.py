import random

A_rows=input('A_rows:')
A_cols=input('A_cols:')
B_rows=input('B_rows:')
B_cols=input('B_cols:')
A1=int(A_rows)
A2=int(A_cols)
B1=int(B_rows)
B2=int(B_cols)

class Matrix:
    def __init__(self, nrows, ncols):
        self.nrows = nrows
        self.ncols= ncols
        self.x=[]
        self.exist=True
        for j in range(nrows):
            a=[]
            self.x.append(a)
            for i in range(ncols):
                a.append(random.randint(0,9))

    def add(self, B): #相加
        if self.nrows == B.nrows and self.ncols==B.ncols:
            C=Matrix(self.nrows,self.ncols)
            for i in range(self.nrows):
                for j in range(self.ncols):
                    C.x[i][j]=self.x[i][j]+B.x[i][j]
            return C  
        else:
            F=Matrix(0,0)
            F.exist=False
            return F

    def sub(self, B): #相減
        if self.nrows == B.nrows and self.ncols==B.ncols:
            D=Matrix(self.nrows,self.ncols)        
            for i in range(self.nrows):
                for j in range(self.ncols):
                    D.x[i][j]=self.x[i][j]-B.x[i][j] 
            return D
        else:
            F=Matrix(0,0)
            F.exist=False
            return F

    def mul(self, B): #相乘
        if self.ncols==B.nrows:
            M=Matrix(self.nrows,B.ncols)
            for i in range(self.nrows):
                for j in range(B.ncols):
                    value=0
                    for k in range(self.ncols):
                        value += self.x[i][k] * B.x[k][j]
                    M.x[i][j]=value
            return M
        else:
            F=Matrix(0,0)
            F.exist=False
            return F

    def transpose(self,B): #轉置
        if self.ncols==B.nrows:
            M=Matrix(self.nrows,B.ncols)
            for i in range(self.nrows):
                for j in range(B.ncols):
                    value=0
                    for k in range(self.ncols):
                        value += self.x[i][k] * B.x[k][j]
                    M.x[i][j]=value
                                
            T=Matrix(B.ncols,self.nrows)
            for i in range(B.ncols):
                for j in range(self.nrows):
                    T.x[i][j]=M.x[j][i]
                    T.display()
            return T
        else:
            F=Matrix(0,0)
            F.exist=False
            return F

    def display(self):
        if self.exist==False:
            print('None')
        else:
            for i in range(self.nrows):
                for j in range(self.ncols):
                    print(self.x[i][j],end=" ")
                print("\n")
        
A= Matrix(A1,A2) #建立 instance object
B= Matrix(B1,B2)
print('A:')
A.display()
print('B:')
B.display()
C=A.add(B)
D=A.sub(B)
M=A.mul(B)
T=A.transpose(B)
print('add:')
C.display()
print('sub:')
D.display()
print('mul:')
M.display()
print('transpose:')
T.display()
