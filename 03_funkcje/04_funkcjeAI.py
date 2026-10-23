# . Funkcje bez parametrów, nie zwracające wartości
# Zadanie 1
# Napisz funkcję powitanie(), która wypisze tekst „Witaj w Pythonie!”.
# Wywołanie: powitanie()
# Oczekiwany wynik: Witaj w Pythonie!

# def powitanie():
#     print ("Witaj w pythonie!")

# powitanie()


# Zadanie 2
# Napisz funkcję linia(), która wypisze 20 znaków „-”.
# Wywołanie: linia()
# Oczekiwany wynik: --------------------

# def linia():
#     print("-"*20)

# linia()

# Zadanie 3
# Napisz funkcję autor(), która wypisze Twoje imię.
# Wywołanie: autor()
# Przykładowy wynik: Jan
# Zadanie 4
# Napisz funkcję oblicz(), która obliczy i wypisze wynik działania 5 * 8.
# Wywołanie: oblicz()
# Oczekiwany wynik: 40
# 2. Funkcje z parametrami, nie zwracające wartości
# Zadanie 1
# Napisz funkcję przywitaj(imie), która wypisze podane imię.
# Wywołania i wyniki:
# przywitaj("Anna") Wynik: Anna
# przywitaj("Piotr") Wynik: Piotr

def przywitaj(imie):
    print(imie)

# przywitaj('Marcel')

# Zadanie 2
# Napisz funkcję suma(a, b), która wypisze sumę dwóch liczb.
# Wywołania i wyniki:
# suma(4, 7) Wynik: 11
# suma(10, 2) Wynik: 12

#def suma(a , b):
#    print(a+b)

#suma(7 , 10)





# Zadanie 3
# Napisz funkcję pole_prostokata(a, b), która wypisze pole prostokąta.
# Wywołania i wyniki:
# pole_prostokata(5, 3) Wynik: 15
# pole_prostokata(7, 2) Wynik: 14
# Zadanie 4
# Napisz funkcję srednia(a, b, c), która wypisze średnią z trzech liczb.
# Wywołania i wyniki:
# srednia(2, 4, 6) Wynik: 4.0
# srednia(1, 2, 3) Wynik: 2.0

# def srednia(a, b, c):
#     print((a + b + c) / 3)

# srednia(2, 4 ,6)




# 3. Funkcje zwracające wartość
# Zadanie 1
# Napisz funkcję kwadrat(x), która zwraca kwadrat liczby.
# Wywołania i wyniki:
# print(kwadrat(4)) Wynik: 16
# print(kwadrat(7)) Wynik: 49

# def kwadrat(x):
#     return x**2

# print(kwadrat(5))

# Zadanie 2
# Napisz funkcję roznica(a, b), która zwraca różnicę liczb.
# Wywołania i wyniki:
# print(roznica(10, 3)) Wynik: 7
# print(roznica(8, 12)) Wynik: -4
# Zadanie 3
# Napisz funkcję reszta(a, b), która zwraca resztę z dzielenia.
# Wywołania i wyniki:
# print(reszta(17, 5)) Wynik: 2
# print(reszta(20, 3)) Wynik: 2

def reszta(a,b):
    return a % b

# print(reszta(17,5))

# Zadanie 4
# Napisz funkcję potega(a, b), która zwraca wynik potęgowania.
# Wywołania i wyniki:
# print(potega(2, 5)) Wynik: 32
# print(potega(3, 3)) Wynik: 27
def potega(a,b):
    return a**b

# print(potega(2,5)) 
    



# 4. Funkcje wykorzystujące warunki, nie zwracające wartości
# Zadanie 1
# Napisz funkcję sprawdz_zero(x). Jeśli liczba jest równa 0, wypisz „zero”.
# Wywołania i wyniki:
# sprawdz_zero(0) Wynik: zero
# sprawdz_zero(5) Wynik: brak komunikatu
# Zadanie 2
# Napisz funkcję pelnoletni(wiek). Jeśli wiek jest większy lub równy 18, wypisz „TAK”.
# Wywołania i wyniki:
# pelnoletni(20) Wynik: TAK
# pelnoletni(15) Wynik: brak komunikatu
# Zadanie 3
# Napisz funkcję haslo(tekst). Jeśli tekst jest równy "python", wypisz „Poprawne”.
# Wywołania i wyniki:
# haslo("python") Wynik: Poprawne
# haslo("java") Wynik: brak komunikatu
# Zadanie 4
# Napisz funkcję sprawdz(a, b). Jeśli liczby są równe lub jedna z nich jest równa 0, wypisz „OK”.
# Wywołania i wyniki:
# sprawdz(5, 5) Wynik: OK
# sprawdz(0, 8) Wynik: OK
# sprawdz(3, 7) Wynik: brak komunikatu
# 5. Funkcje wykorzystujące warunki i zwracające wartość logiczną
# Zadanie 1
# Napisz funkcję czy_zero(x), która zwraca wynik porównania x == 0.
# Wywołania i wyniki:
# print(czy_zero(0)) Wynik: True
# print(czy_zero(5)) Wynik: False
# Zadanie 2
# Napisz funkcję czy_rowne(a, b), która zwraca wynik porównania liczb.
# Wywołania i wyniki:
# print(czy_rowne(4, 4)) Wynik: True
# print(czy_rowne(4, 7)) Wynik: False
# Zadanie 3
# Napisz funkcję czy_haslo(tekst), która zwraca informację, czy tekst jest równy "python".
# Wywołania i wyniki:
# print(czy_haslo("python")) Wynik: True
# print(czy_haslo("abc")) Wynik: False
# Zadanie 4
# Napisz funkcję czy_poprawne(a, b), która zwraca wartość True, gdy liczby są równe lub druga liczba jest równa 10.
# Wywołania i wyniki:
# print(czy_poprawne(5, 5)) Wynik: True
# print(czy_poprawne(2, 10)) Wynik: True
# print(czy_poprawne(2, 3)) Wynik: False
# 6. Funkcje zwracające wartość logiczną wykorzystywaną w instrukcji if
# Zadanie 1
# Napisz funkcję czy_dodatnia(x), która zwraca True, jeśli liczba jest większa od 0.
# Przykład użycia:
# if czy_dodatnia(5): print("dodatnia")
# Wynik: dodatnia
# Zadanie 2
# Napisz funkcję czy_pelnoletni(wiek), która zwraca True, jeśli wiek jest większy lub równy 18.
# Przykład użycia:
# if czy_pelnoletni(20): print("może głosować")
# Wynik: może głosować
# Zadanie 3
# Napisz funkcję czy_parzysta(x), która zwraca True, jeśli liczba jest parzysta.
# Przykład użycia:
# if czy_parzysta(8): print("parzysta")
# Wynik: parzysta
# Zadanie 4
# Napisz funkcję czy_poprawny_login(login), która zwraca True, jeśli login jest równy "admin".
# Przykład użycia:
# if czy_poprawny_login("admin"): print("zalogowano")
# Wynik: zalogowano
# 7. Funkcje złożone (łączenie poznanych elementów)
# Zadanie 1
# Napisz funkcję ocena(punkty), która zwraca:
# "Zaliczone", gdy liczba punktów jest większa lub równa 50,
# "Nie zaliczone" w przeciwnym przypadku.
# Wywołania i wyniki:
# print(ocena(75)) Wynik: Zaliczone
# print(ocena(30)) Wynik: Nie zaliczone
# Zadanie 2
# Napisz funkcję wieksza(a, b), która zwraca większą z dwóch liczb.
# Wywołania i wyniki:
# print(wieksza(8, 3)) Wynik: 8
# print(wieksza(4, 11)) Wynik: 11
# Zadanie 3
# Napisz funkcję czy_podzielne(a, b), która zwraca informację, czy liczba a jest podzielna przez liczbę b.
# Wywołania i wyniki:
# print(czy_podzielne(12, 3)) Wynik: True
# print(czy_podzielne(14, 5)) Wynik: False
# Zadanie 4
# Napisz funkcję rabat(cena, klient_staly), która zwraca cenę po rabacie:
# jeśli klient_staly == "tak", udziel 10% rabatu,
# w przeciwnym przypadku nie zmieniaj ceny.
# Wywołania i wyniki:
# print(rabat(100, "tak")) Wynik: 90.0
# print(rabat(100, "nie")) Wynik: 100
# Zadanie 5
# Napisz funkcję logowanie(login, haslo), która zwraca True, gdy:
# login jest równy "admin",
# hasło jest równe "python".
# Wywołania i wyniki:
# print(logowanie("admin", "python")) Wynik: True
# print(logowanie("admin", "1234")) Wynik: False
# Zadanie 6
# Napisz funkcję srednia3(a, b, c), która zwraca średnią trzech liczb.
# Następnie sprawdź za pomocą instrukcji if, czy średnia jest większa lub równa 3.
# Przykład użycia:
# if srednia3(4, 3, 5) >= 3: print("zdane")
# Wynik: zdane
# Zadanie 7
# Napisz funkcję pensja(godziny, stawka), która zwraca wysokość wynagrodzenia.
# Wywołania i wyniki:
# print(pensja(40, 30)) Wynik: 1200
# print(pensja(15, 25)) Wynik: 375
# Zadanie 8
# Napisz funkcję czy_mozna_glosowac(wiek, obywatel), która zwraca True, gdy:
# wiek jest większy lub równy 18,
# obywatel ma wartość "tak".
# Wywołania i wyniki:
# print(czy_mozna_glosowac(20, "tak")) Wynik: True
# print(czy_mozna_glosowac(20, "nie")) Wynik: False
# Zadanie 9
# Napisz funkcję ostatnia_cyfra(liczba), która zwraca ostatnią cyfrę liczby.
# Wywołania i wyniki:
# print(ostatnia_cyfra(123)) Wynik: 3
# print(ostatnia_cyfra(908)) Wynik: 8
# Zadanie 10
# Napisz funkcję ile_dziesiatek(liczba), która zwraca liczbę pełnych dziesiątek.
# Wywołania i wyniki:
# print(ile_dziesiatek(57)) Wynik: 5
# print(ile_dziesiatek(123)) Wynik: 12

def ile_dziesiatek(liczba):
    return liczba // 10

# print(ile_dziesiatek(123))