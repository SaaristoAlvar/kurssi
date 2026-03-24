import random

def heitto(tahkot):
    return random.randint(1, tahkot)

def noppa():
    koko= int(input("Nopan suurin silmäluku: "))
    tahkot =  int(input("Nopan tahkojen määrä:"))
    while True:
        arvo = heitto(tahkot)
        print(f"Sait luvun: {arvo}")
        if arvo == koko:
            print(f"{koko}!! Peli päättyi!")
            break

if __name__ == "__main__":
    noppa()