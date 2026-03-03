import random
nopat = int(input("Noppien määrä: "))

summa=0

for i in range (nopat):
    heitto = random.randint(1,6)
    summa += heitto
    print("Noppa" , i+1, ":", heitto)
print("Tulos: ", summa)