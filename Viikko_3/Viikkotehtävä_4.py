karkaus = int(input("Anna vuosiluku:"))

if karkaus % 400 == 0:
    print("Vuosi on karkausvuosi!")
elif karkaus % 100 == 0:
    print("Vuosi ei ole karkausvuosi!")
elif karkaus % 4 == 0:
    print("Vuosi on karkausvuosi!")
else:
    print("Vuosi ei ole karkausvuosi!")