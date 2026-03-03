luvut = []


while True:

    luku = (input("Syötä luku: "))
    print("Tyhjä vastauskenttä katkaisee ohjelman")

    if luku == "":
        break
    try:
       luku1 = int(luku)
       luvut.append(luku1)

    except ValueError:
        print("Virheellinen syöte, kokeile uudestaan!")
if len(luvut) == 0:
    print("Et syöttänyt yhtään lukua")
else:
    luvut.sort(reverse=True)
    print("Viisi isointa lukua: ")
    print(luvut[:5])
