pienin = None
suurin = None

while True:

    luku = (input("Syötä luku: "))
    print("Tyhjä vastauskenttä katkaisee ohjelman")

    if luku == "":
        break
    try:
        luku1 = int(luku)

        if pienin is None or luku1 < pienin:
            pienin = luku1

        if suurin is None or luku1 > suurin:
            suurin = luku1

    except ValueError:
        print("Virheellinen syöte, kokeile uudestaan!")
if pienin is None:
    print("Et syöttänyt yhtään lukua")
else:
    print("Pienin lukusi jonka syötit:", pienin)
    print("Suurin luksi jonka syötit:", suurin)