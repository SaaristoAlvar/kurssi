palkka = float(input("Tuntipalkkasi?:"))
tunnit = int(input("Kuinka monta tuntia työskentelit?:"))
paiva  = str(input("Mikä päivä olit töissä?:"))
if paiva == "sunnuntai":
    print("Tienasit ",(palkka * tunnit) * 2 , "€" )

else:
    print("Tienasit" , palkka * tunnit  , "€")