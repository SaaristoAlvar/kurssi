tarina = []
sama = ""
while True:
    sana = input("Anna sana lisättäväksi tarinaan:")

    if sana == "loppu":
        break
    if sana == sama:
        break

    tarina.append(sana)
    sama = sana

print(" ".join(tarina))
