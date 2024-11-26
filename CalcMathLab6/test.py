from SolverClass import Solver

#matrix = [[10,1,-0.5,0.7,11.2],[1,15,0.5,4,20.5],[-0.5,0.5,20,1,21],[0.7,4,1,17,22.7]]
matrix = [[3.2,1,1,4],[1,3.7,1,4.5],[1,1,4.2,4]]

s = Solver(matrix,5)
print("is algphutm applicable?",s.applicabilityCheck())
for i in range(s.size):
    for j in range(s.size):
        print(s.A[i][j],end='\t')
    print(s.B[i])
a = s.solve()
print("roots = ",end=' ')
for i in a:
    print(i,end = '\t')
print("\ncorrectness check",end=' ')
a = s.correctnessCheck()
for i in a:
    print(i,end = '\t')