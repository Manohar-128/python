def test(M,T):
    return [[i,j] for i,row in enumerate(M) for j,n in enumerate (row) if n==T]
M=[[1,3,2,32,19],[19,2,48,19],[],[9,35,4],[3,19]]
T=19
print("Matrix:")
print(M)
print("Target value:")
print(T)
print("indiaces f all occurrences of he trget value in the said uneven matrix:")
print(test(M,T))