def ROT13_encrypt(P):
    C = ""
    for i in range(len(P)):
        if not P[i].isalpha():
            C += P[i]
        elif ord(P[i]) - ord("a") <= 13 or ord(P[i]) - ord("A") <= 13:
            C += chr(ord(P[i]) + 13)
        else:
            C += chr(ord(P[i]) - 13)
    return C


def ROT13_decrypt(C):
    P = ""
    for i in range(len(C)):
        if not C[i].isalpha():
            P += C[i]
        elif ord(C[i]) - ord("a") <= 13 or ord(C[i]) - ord("A") <= 13:
            P += chr(ord(C[i]) + 13)
        else:
            P += chr(ord(C[i]) - 13)
    return P
