def VigenereCipherEncrypto(P, Key):
    C = ""
    count = 0
    for i in range(len(P)):
        if P[i].isalpha():
            C += chr((ord(P[i])-ord("a")+ord(Key[count % len(Key)])) % 26+ord("a"))
            count += 1
        else:
            C += " "
    return C

def VigenereCipherDecrypto(C, Key):
    P = ""
    count = 0
    for i in range(len(C)):
        if C[i].isalpha():
            P += chr((ord(C[i])-ord("a")-ord(Key[count % len(Key)])) % 26+ord("a"))
            count += 1
        else:
            P += " "
    return P
