Key1=[]
Key2=[]

for i in range(26):
    for j in range(26):
        if (i+j)%26==0:
            Key1.append(i)
            Key1.append(j)
        if i*j%26==1:
            Key2.append(i)
            Key2.append(j)
Key1=list(set(Key1))
Key2=list(set(Key2))

P='cryptography is fun'
C = ''
for i in range(len(P)):
    if P[i].isalpha():
        j = ord(P[i])-ord('a')
        C += chr((j*Key2[j%12]+Key1[j%26]) % 26+ord('a'))
    else:
        C += ' '
print(C)

# C = 'mwwqegswaqww ec ika'
