luku = int(input("Syötä luku: "))

if luku <= 1:
    print("Lukusi ei ole alkuluku!")
else:
    alkuluku = True

    for i in range (2, luku):
        if luku % i == 0:
            alkuluku = False

    if alkuluku:
        print("Lukusi on alkuluku!")
    else:
        print("Lukusi ei ole alkuluku!")