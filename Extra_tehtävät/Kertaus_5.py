while True:
        print("\n Valitse toiminto:")
        print("1) plus")
        print("2) minus")
        print("3) kerto")
        print("4) jako")
        print("5) Lopeta ohjelma")

        lasku = input("Valitse toiminto 1-5: ")

        if lasku == "5":
            print("Ohelma keskeytetty")
            break

        if lasku not in ("1", "2", "3", "4"):
            print("Virhe!")
            break
        luku1 = int(input("Anna luku:"))
        luku2 = int(input("Anna toinen luku:"))

        if lasku == "1":
            print("Yhteensä" , luku1 + luku2)
        elif lasku == "2":
            print("yhteensä", luku1 - luku2)
        elif lasku == "3":
            print("Yhteensä", luku1 * luku2)
        elif lasku == "4":
            print("Yhteensä", luku1 / luku2)

