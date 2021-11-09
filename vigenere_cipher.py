def vigenere_encrypt(P, Key):
    Key=Key.lower()
    C = ""
    count = 0
    for i in range(len(P)):
        if P[i].isalpha() and P[i].islower():
            C += chr((ord(P[i])-ord("a")*2 +
                     ord(Key[count % len(Key)])) % 26+ord("a"))
            count += 1
        elif P[i].isalpha() and P[i].isupper():
            C += chr((ord(P[i])-ord("A")-ord("a") +
                     ord(Key[count % len(Key)])) % 26+ord("A"))
            count += 1
        else:
            C += " "
    return C


def vigenere_decrypt(C, Key):
    Key=Key.lower()
    P = ""
    count = 0
    for i in range(len(C)):
        if C[i].isalpha() and C[i].islower():
            P += chr((ord(C[i])-
                     ord(Key[count % len(Key)])) % 26+ord("a"))
            count += 1
        elif C[i].isalpha() and C[i].isupper():
            P += chr((ord(C[i])-
                     ord(Key[count % len(Key)])) % 26+ord("A"))
            count += 1
        else:
            P += " "
    return P

