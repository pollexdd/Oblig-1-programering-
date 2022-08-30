# Jeg fikk veldig mye hjelp på denne oppgaven av en youtube video får å skjønne hvordan det skulle gjøres
# link : https://www.youtube.com/watch?v=5_CAo_C523g
# fikk også hjelp av en venn som går andreåret


#print av alle valgene
print("1 får å gange")
print("2 får å dele")
print("3 får pluss")
print("4 får minus")
print("5 får modulo")
print("6 får opphøyne")
print("7 får dele med nedrunding")

valg = input("velg modus: ") #variabel får valg av modus

nummer1 = float(input("skriv tall 1: "))  #variabel får input av tall 1
nummer2 = float(input("skriv tall 2: "))  #variabel får input av tall 2

if valg == "1":  #gange utregning
    print(nummer1*nummer2)

if valg == "2": #dele utregning
    print(nummer1/nummer2)

if valg == "3": #pluss utregning
    print(nummer1+nummer2)

if valg == "4": #minus utregning
    print(nummer1-nummer2)

if valg == "5": #modulo utregning
    print(nummer1%nummer2)

if valg == "6": #opphøye utregning
    print(nummer1**nummer2)

if valg == "7": #dele med nedrunding utregning
    print(nummer1//nummer2)

