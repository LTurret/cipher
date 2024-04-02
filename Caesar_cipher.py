def Ceacar_encrypt(P, offset):
    C = ""
    for i in range(len(P)):
        if not P[i].isalpha():
            C += " "
        C += chr((ord(P[i]) - ord("a") + offset) % 26 + ord("a"))
    return C


def Ceacar_decrypt(C, offset):
    P = ""
    for i in range(len(C)):
        if not C[i].isalpha():
            P += " "
        P += chr((ord(C[i]) - ord("a") - offset) % 26 + ord("a"))
    return P
