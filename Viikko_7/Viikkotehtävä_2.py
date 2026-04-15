nimet = set()
while True:
    nimi = input("Syötä nimi(tyhjä vastaus katkaisee ohjelman): ")
    if nimi == "":
        break

    elif nimi in nimet:
        print("Nimi on jo mainittu")

    else :
        nimet.add(nimi)
        print("Nimi on uusi Jatka")

        print("\nSyötetyt nimet: ")
        for n in nimet:
            print(n)