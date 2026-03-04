import math

while True:
    luku = int(input("Syötä kokonaisluku:"))
    if luku < 0:
        print("Virheellinen arvo")
    elif luku > 0:
        print("Luvun neliöjuuri on" , math.sqrt(luku))
    else:
        print("Ohjelma katkaistu")
        break
