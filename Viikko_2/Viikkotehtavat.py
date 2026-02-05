#1. tehtävä
nimi=input("Mikä on nimesi: ")
print("Hello "+ nimi)

#2. tehtävä
sade=float(input("Mika on ympyran sade cm:"))
import math
pinta_ala=math.pi*sade**2
print("Ympyrän pinta-ala on: " , pinta_ala , "cm2")

#3. tehtävä
kanta=float(input("Kannan mitta sentteina: "))
korkeus=float(input("korkeuden mitta sentteina: "))
pinta_ala2=kanta*korkeus
print("suorakulmion pinta-ala on: " , pinta_ala2 , "cm2")
piiri=(kanta*2) + (korkeus*2)
print("Suorakulmion piiri taas on : " ,piiri , "cm")

# 4. tehtävä
luku1=float(input("anna numero: "))
luku2=float(input("anna toinen numero: "))
luku3=float(input("anna kolmas numero: "))
plus=luku1+luku2+luku3
print("Antamiesi lukujen summa on: " , plus)
tulo=luku1*luku2*luku3
print("Antamiesi lukujen tulo on: " , tulo)
keskiarvo=(luku1+luku2+luku3)/2
print("Antamiesi lukujen keskiarvo on: " , keskiarvo)

# 5. tehtävä
luoti=(13.3)
naula=luoti*32
leiviska=naula*20
leiviska1=float(input("leviskojen määrä:"))
naula1=float(input("naulojen määrä:"))
luoti1=float(input("luotien määrä:"))

gr=(leiviska*leiviska1+naula*naula1+luoti*luoti1)
kilo = (float(gr // 1000))
g=gr%1000
print(f"\npainaa yhteensä: {kilo} kg ja {g:.2f} g!")

