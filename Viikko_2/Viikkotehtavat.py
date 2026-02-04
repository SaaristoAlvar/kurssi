print("Hei Maailma")
print('"Hei" sanoi Alvar')
print("hyvää")
print("huomenta")
print("Hyvää\nhuomenta")
käyttäjä=input("Kerro nimesi:")
print("hauska tavata "+ käyttäjä + "!")


eka = -9
toka = 12_456_123_180
kolmas = 4.973
neljäs = -4 + 2j

print(eka)
print(toka)
print(kolmas)
print(neljäs)
print(neljäs.real)
print(neljäs.imag)



fahrenheit_str = input("Anna lämpötila Fahrenheit-asteina: ")
fahrenheit = float(fahrenheit_str)
celsius = (fahrenheit-32)*5/9
print("Lämpötila Celsius-asteina: " + str(celsius))
print(f"Lämpötila Celsius-asteina: {celsius:6.2f}")

import math

print(f"{'Pii':12s}:{math.pi:10.5f}")
print(f"{'Neperin luku':12s}:{math.e:10.5f}")