moi = ("Talvi", "Kevät", "Kesä", "Syksy")

kuukausi = int(input("Luku 1-12: "))

if kuukausi == 12 or kuukausi <= 2:
    vuodenaika = moi[0]

elif kuukausi <= 5:
    vuodenaika = moi[1]

elif kuukausi <=8:
    vuodenaika = moi[2]

else:
    vuodenaika = moi[3]

print("vuodenaika on", vuodenaika)




