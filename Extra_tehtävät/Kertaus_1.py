nimi = input("Nimi?: ")
if nimi == "matti":
    print("Seuraava asiakas")
else:

    luku = int(input("Montako keittoa?: "))

    hinta = luku*5.90

    print(nimi , "tilauksesi maksaa" , hinta,  "€ Kiitos!")
