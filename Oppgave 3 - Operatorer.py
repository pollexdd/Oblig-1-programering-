# Jeg fikk veldig mye hjelp på denne oppgaven av en youtube video får å skjønne hvordan det skulle gjøres
# link : https://www.youtube.com/watch?v=5_CAo_C523g


print("1 får å gange")
print("2 får å dele")
print("3 får pluss")
print("4 får minus")
print("5 får modulo")
print("6 får opphøyne")
print("7 får dele med nedrunding")

valg = input("velg modus ")

nummer1 = float(input("skriv tall 1 "))
nummer2 = float(input("skriv tall 2 "))

if valg == "1":
    print(nummer1*nummer2)

if valg == "2":
    print(nummer1/nummer2)

if valg == "3":
    print(nummer1+nummer2)

if valg == "4":
    print(nummer1-nummer2)

if valg == "5":
    print(nummer1%nummer2)

if valg == "6":
    print(nummer1**nummer2)

if valg == "7":
    print(nummer1//nummer2)

