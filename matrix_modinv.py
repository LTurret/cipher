# from sympy import Matrix
# import numpy as np
K=[[3,2],[5,7]]
# Keyinv = np.array(Matrix(K).inv_mod(26))
# print(Keyinv)

# step1 det
det=0
detinv=0
if len(K)==2:
    det=K[0][0]*K[1][1]-K[0][1]*K[1][0]
for i in range(26):
    if det*i%26==1:
        detinv=i

#step2 transpose matrix
for i in range(len(K)):
    for j in range(len(K)):
        if i<j:
            K[j][i],K[i][j]=K[i][j],K[j][i]
        
# step3 find minor
i=0
K[i][i], K[i+1][i+1] = K[i+1][i+1], K[i][i]
K[i][i+1], K[i+1][i] = K[i+1][i], K[i][i+1]

for i in range(len(K)):
    for j in range(len(K)):
        if i%2 ^ j%2:
            K[i][j]=0-K[i][j]
        K[i][j]=K[i][j]*detinv%26

print(K)
