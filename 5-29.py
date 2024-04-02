seed = "0001"
seedset = set()
for i in range(20):
    b0 = int(seed[3])
    b1 = int(seed[2])
    b2 = int(seed[1])
    b3 = int(seed[0])
    b4 = b2 ^ b0 ^ b3
    seed = f"{b4}{b3}{b2}{b1}{b0}"
    ki = b0
    print(f"round {i}|{seed}|{ki}")
    seedset.add(seed)

print("period:", len(seedset))
