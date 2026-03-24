def parittomat(jono):

    return[luku for luku in jono if luku % 2 == 0]

def main():

    kaikki = [13,23,55,66,78,89]

    poistettu = parittomat(kaikki)

    print(kaikki)
    print(poistettu)

main()
