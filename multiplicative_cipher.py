def MultiplicativeCipherEncrypto(P,Key):
  C=''
  for i in range(len(P)):
    if P[i].isalpha():
      C+=chr(((ord(P[i])-ord('a'))*Key)%26+ord('a'))
    else:
      C+=' '
  return C

def MultiplicativeCipherDecrypto(C,Key):
  P=''
  ReverseKey=0
  for j in range(26):
    if Key*j%26==1:
      ReverseKey=j
  for i in range(len(C)):
    if C[i].isalpha():
      P+=chr(((ord(C[i])-ord('a'))*ReverseKey)%26+ord('a'))
    else:
      P+=' '
  return P
