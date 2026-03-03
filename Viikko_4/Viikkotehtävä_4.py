import random

luku =  random.randint(1,10)

while True:
    try:
        arvaus = int(input("Arvaa luku väliltä 1-10:"))
        if arvaus > luku:
            print("Pienenmpi")
        elif arvaus < luku:
            print("Suurempi")
        else:
            print("Oikein!!!")
            break

    except ValueError:
        print("Kokeile jotain muuta lukua")

