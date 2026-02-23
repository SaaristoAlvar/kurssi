kuha = float(input("Kuinka pitkän kuhan sait sentteinä:"))

if kuha <= 37:
    puuttuu = 37 - kuha
    print("Kuha on liian pieni. Laske se takaisin veteen!")
    print("kuhan pitäisi olla " , puuttuu, " cm pidempi.")


if kuha >= 37:
    print("Kuha on hyvän kokoinen nostettavaksi!")
