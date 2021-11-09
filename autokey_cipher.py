def AutokeyCipherEncrypto(P,Key):
    C=''
    C += chr((ord(P[0])-ord("a")+key) % 26+ord("a"))
    for i in range(1,len(P)):
        if P[i].isalpha():
            C += chr((ord(P[i])-ord("a")*2+ord(P[i-1])) % 26+ord("a"))
        else:
            C += " "
    return C


def AutokeyCipherDecrypto(C,Key):
    P = ''
    P += chr((ord(C[0])-ord("a")-key) % 26+ord("a"))
    for i in range(1, len(C)):
        if C[i].isalpha():
            P += chr((ord(C[i])-ord(P[i-1])) % 26+ord("a"))
        else:
            P += " "
    return P
