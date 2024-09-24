def leggSammen():
    tall1 = input("Skriv inn det første tallet: ")
    tall2 = input("Skriv inn det andre tallet: ")
    sum = int(tall1) + int(tall2)
    print(f'{tall2} + {tall2} = {sum}')


def trekkFra():
    tall1 = input("Skriv inn det første tallet: ")
    tall2 = input("Skriv inn det andre tallet: ")
    diff = int(tall1) - int(tall2)
    print(f'{tall2} - {tall2} = {diff}')

def gange():
    tall1 = input("Skriv inn det første tallet: ")
    tall2 = input("Skriv inn det andre tallet: ")
    produkt = tall1 * tall2
    print(f"{tall1} + {tall2} = {produkt}")


def skibidi():
    print("skibdi toilet")

def dele():
    tall1 = input("Skriv inn det første tallet: ")
    tall2 = input("Skriv inn det andre tallet: ")
    diff = int(tall1) / int(tall2)
    print(f'{tall2} / {tall2} = {diff}')

def gjennomsnitt():
    tall1 = input("Skriv inn det første tallet: ")
    tall2 = input("sSriv inn det andre tallet: ")
    sum = tall1 + tall2
    gjs = sum / 2
    print(f"gjennomsnittet mellom {tall1} og {tall2} er {gjs}")
