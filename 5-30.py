seed = "1110"

for i in range(20):
    b0 = int(seed[3])
    b1 = int(seed[2])
    b2 = int(seed[1])
    b3 = int(seed[0])
    b4 = b1 ^ b0
    seed = f"{b4}{b3}{b2}{b1}{b0}"
    ki = b0
    print(ki, end="")
