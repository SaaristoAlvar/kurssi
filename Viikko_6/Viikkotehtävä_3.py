def gallonat(gal):
    return gal * 3.785
def main():
    while True:
        arvo = float(input("Anna bensanmäärä gallonoina:"))
        if arvo < 0:
            break

        litrat = gallonat(arvo)
        print(f"{arvo} gallonaa on {litrat:.3f} litraa")

main()