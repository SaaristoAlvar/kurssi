sukupuoli = input("Mikä on sinun biologinen sukupuoli:").lower()
hemo = int(input("Anna hemglobiiniarvo:"))

if sukupuoli == "mies":
    if hemo < 134:
        print("Hemoglobiini on alhainen.")
    elif hemo <=195:
        print("Hemoglobiinisi on normaali.")
    else:
        print("hemoglobiinisi on korkea!")

elif sukupuoli == "nainen":
    if hemo < 117:
        print("Hemoglobiini on alhainen.")
    elif hemo <=175:
        print("Hemoglobiinisi on normaali.")
    else:
        print("hemoglobiinisi on korkea!")
else:
    print("Virhe sukupuolta syöttäessä")
