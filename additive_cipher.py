def AdditiveCipherEncrypto(P, Key):
    C = ""
    for i in range(len(P)):
        if P[i].isalpha():
            C += chr((ord(P[i]) - ord("a") + Key) % 26 + ord("a"))
        else:
            C += " "
    return C


def AdditiveCipherDecrypto(C, Key):
    P = ""
    for i in range(len(C)):
        if C[i].isalpha():
            P += chr((ord(C[i]) - ord("a") + Key) % 26 + ord("a"))
        else:
            P += " "
    return P
