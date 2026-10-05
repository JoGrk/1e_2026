# Zadanie 2: Zniżka na basen (or)

#  Bilet na basen kosztuje 20 zł. Jednak dzieci poniżej 7 lat LUB seniorzy powyżej 65 lat wchodzą za darmo. Program pyta o wiek i wyświetla informację: "Cena biletu: 0 zł" lub "Cena biletu: 20 zł".

# wiek = int(input("wiek: "))

# if wiek < 7 or wiek > 65:
#     print("cena biletu: 0zl")
# else:
#     print("cena biletu: 20zl")

isAutomaticMode = True
# is the level of day-lighr above 80%
is80PercentLight = True
# is the Sun ligthing directly into the driver's face
isDirectLight = False
# is it rainy, foggy or other weather conditions are present
isRainy = False

if isAutomaticMode==True:
    print("Tryb automatyczny")
    if is80PercentLight:
        if isDirectLight:
            print("Zapalamy")
        else:
            print("Gasimy")
    else:
        print("zapalamy")
else:
    print("tryb manualny")