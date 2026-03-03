while True:
    nimi = input("Käyttäjätunnus: ")
    salasana = input ("Salasana: ")

    if nimi == "python" and salasana == "rules":
        print("Tervetuloa")
        break
    else:
        print("Väärä käyttäjätunnus tai salasana. Yritä uudelleen.")