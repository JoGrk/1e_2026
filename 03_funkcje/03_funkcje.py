# 1. Napisz funkcję greet z dwoma parametrami: pora dnia i imię. Funkcja wypisuje w konsoli "Good [pora dnia], [imię]"
#def greet(time_of_day, name):
#    print(f"Good {time_of_day}, {name}")
#
#greet("evening", "Kacper")


# 2. funkcje średnia, z dwoma parametrami, zwraca wartość średniej  ze swoich parametrów, wywołaj funkcję dla obliczenia i wypisania wartości średniej z dowolnych dwóch liczb 

#def srednia(x,y):
#    return (x+y)/2
#
#print(srednia(5,10))

# 3. Napisz funkcję triple, która zwraca potrojoną wartość swojego parametru (użyta suma)  Wywołaj dla liczby i dla tekstu
# def triple(x):
#     return x *3

# print(triple (10))


# 4. funkcje isOdd z jednym parametrem liczbowym, zwraca true, gdy jest nieparzysty i false w przeciwnym wypadku. Wywołaj dla -8 i 15


# def isOdd(a):
#     if a %2 == 1:
#         return True
#     else:
#         return False

#def isOdd(a):
 #   return  a % 2 == 1
          

#print(f"liczba {10} jest nieparzysta:{isOdd(10)}")
#print(f"liczba {-8} jest nieparzysta:{isOdd(-8)}")
#print(f"liczba {15} jest nieparzysta:{isOdd(15)}")



# 5. funkcja isDivided  zwraca prawdę, gdy pierwszy parametr dzieli się przez drugi i fałsz w przeciwnym wypadku. Sprawdź wywołując funkcję.

def isDivided(a,b):
    return a % b == 0

a = 4
b = 2
if isDivided(4, 2):
    print(f"{a} dzieli się przez {b}")
else:
    print(f"{a}nie dzieli się przez{b}")

    

# 6. napisz funkcję isLeapYear, zwraca wartość prawdy, gdy rok jest
# przestępny i false w przeciwnym wypadku. Wykorzystaj funkcję isDivided. Wywołaj

# 7. napisz funkcję halfOf, zwraca połowę swojego argumentu. Wywołaj

# 8. is longerThan , pierwszy parametr to tekst, drugie liczba, zwraca true jeśli długość pierwszego parametru jest większa od drugiego parametru

# 9. Napisz funkcję obliczającą cenę sprzedaży na podstawie dwóch swoich parametrów: oryginalnej ceny i rabatu podanego w procentach (np. 10 gdy jest to 10%) (salePrice, originalPrice, discountPercent)