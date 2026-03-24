import random

def heitto():
    return random.randint(1,6)

def noppa():
    while True:
        arvo = heitto()
        print(f"Sait luvun: {arvo}")
        if arvo == 6:
            print("6!! Peli päättyi!")
            break

if __name__ == "__main__":
    noppa()