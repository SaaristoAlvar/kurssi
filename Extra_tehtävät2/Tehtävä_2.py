main = []

while True:

    lista = int(input("Syötä luku:"))
    if lista == 0 :
        print("Ohejlma päättynyt")
        break

    main.append(lista)
    print("Luvut: ", main)

    print("Lista järjestyksessä: ", sorted(main))