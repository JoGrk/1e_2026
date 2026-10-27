# Zadanie 1.1
# Napisz funkcję powitanie(), która wypisuje: Witaj w technikum!
# Wywołanie: powitanie()
# Wynik: Witaj w technikum!
def powitanie():
    print("Witaj w technikum")

powitanie()
# Zadanie 1.2
def schodki():
    print("*\n**\n***")

schodki()


# Napisz funkcję schodki(), która wypisuje trzy linie: *, **, ***
# Wywołanie: schodki()
# Wynik:
# *
# **

# Zadanie 1.3
# Napisz funkcję potega(), która wypisuje wartość wyrażenia 2**10 + 7//2.
# Wywołanie: potega()
# Wynik: 1027

# Zadanie 1.4
# Napisz funkcję suma_dwoch(), która wczytuje (input) dwie liczby całkowite i wypisuje ich sumę.
# Wywołanie: suma_dwoch()
# Dane wejściowe → wynik:
# 4 i 9 → 13
# -2 i 2 → 0
# 100 i 250 → 350

# KATEGORIA 2. Funkcje z jednym, dwoma lub trzema parametrami, nie zwracające wartości

# Zadanie 2.1
# Napisz funkcję pozdrow(imie), która wypisuje: Czesc, imie!
# Wywołania → wyniki:
# pozdrow(“Ola”) → Czesc, Ola!
# pozdrow(“Marek”) → Czesc, Marek!

# Zadanie 2.2
# Napisz funkcję pole_prostokata(a, b), która wypisuje: Pole: wynik
# Wywołania → wyniki:
# pole_prostokata(4, 5) → Pole: 20
# pole_prostokata(2.5, 4) → Pole: 10.0
# pole_prostokata(7, 7) → Pole: 49

# Zadanie 2.3
# Napisz funkcję powtorz(tekst, n), która wypisuje tekst powtórzony n razy w jednej linii.
# Wywołania → wyniki:
# powtorz(“ha”, 3) → hahaha
# powtorz(“-”, 10) → ----------
# powtorz(“ab”, 1) → ab

# def powtorz(tekst, n):
#     print(tekst*n)

# powtorz("colin", 10)

# Zadanie 2.4
# Napisz funkcję srednia(a, b, c), która wypisuje średnią arytmetyczną trzech liczb.
# Wywołania → wyniki:
# srednia(2, 4, 6) → 4.0
# srednia(3, 4, 8) → 5.0
# srednia(0, 0, 6) → 2.0

# KATEGORIA 3. Funkcje zwracające wartość, którą trzeba wypisać

# Zadanie 3.1
# Napisz funkcję kwadrat(x), która zwraca x do kwadratu.
# Wywołania → wyniki:
# print(kwadrat(5)) → 25
# print(kwadrat(-3)) → 9
# print(kwadrat(0.5)) → 0.25

# Zadanie 3.2
# Napisz funkcję na_fahrenheity(c), która zamienia stopnie Celsjusza na Fahrenheita według wzoru c*9/5 + 32 i zwraca wynik.
# Wywołania → wyniki:
# print(na_fahrenheity(10)) → 50.0
# print(na_fahrenheity(100)) → 212.0
# print(na_fahrenheity(-40)) → -40.0

def na_fahrenheity(c):
    return c*9/5 + 32

print(na_fahrenheity(10))




# Zadanie 3.3
# Napisz funkcję ile_razy(a, b), która zwraca, ile pełnych razy b mieści się w a.
# Wywołania → wyniki:
# print(ile_razy(17, 5)) → 3
# print(ile_razy(20, 4)) → 5
# print(ile_razy(3, 7)) → 0
# def ile_razy(a, b) :
#     return a // b
# 
# print(ile_razy(17, 5)) 
# print(ile_razy(20, 4)) 

# Zadanie 3.4
# Napisz funkcję pole_trapezu(a, b, h), która zwraca pole trapezu o podstawach a, b i wysokości h.
# Wywołania → wyniki:
# print(pole_trapezu(3, 5, 4)) → 16.0
# print(pole_trapezu(2, 4, 5)) → 15.0
# print(pole_trapezu(10, 10, 1)) → 10.0
def pole_trapezu(a, b, h):
    return (a+b)*h/2
print(pole_trapezu(3, 5, 4))

# KATEGORIA 4. Funkcje z warunkami, nie zwracające wartości

# Zadanie 4.1
# Napisz funkcję parzystoscNie, która wypisuje “parzysta”, gdy n jest parzyste, a “nieparzysta”, gdy n jest nieparzyste.
# Wywołania → wyniki:
# parzystosc(4) → parzysta
# parzystosc(7) → nieparzysta
# parzystosc(0) → parzysta

# Zadanie 4.2
# Napisz funkcję porownaj(a, b), która wypisuje “rowne”, gdy a i b są takie same, a “rozne”, gdy są różne.
# Wywołania → wyniki:
# porownaj(3, 3) → rowne
# porownaj(3, 5) → rozne
# porownaj(“kot”, “kot”) → rowne

# Zadanie 4.3
# Napisz funkcję haslo(tekst), która wypisuje “Dostep przyznany”, gdy tekst to python, a w przeciwnym razie “Bledne haslo”.
# Wywołania → wyniki:
# haslo(“python”) → Dostep przyznany
# haslo(“Python”) → Bledne haslo
# haslo(“java”) → Bledne haslo

# Zadanie 4.4
# Napisz funkcję podzielnaNie, która wypisuje “TAK”, gdy n jest podzielne przez 2 lub przez 3, a w przeciwnym razie “NIE”.
# Wywołania → wyniki:
# podzielna(4) → TAK
# podzielna(9) → TAK
# podzielna(6) → TAK
# podzielna(7) → NIE

def podzielnaNie(n):
    if n%2==0 or n%3==0:
        print("TAK")
    else:
        print("NIE")

podzielnaNie(9)


# KATEGORIA 5. Funkcje z warunkami, zwracające wartość (przy wywołaniu if nie jest potrzebny)

# Zadanie 5.1
# Napisz funkcję krokNie, która zwraca n//2, gdy n jest parzyste, a 3*n+1, gdy n jest nieparzyste.
# Wywołania → wyniki:
# print(krok(6)) → 3
# print(krok(7)) → 22
# print(krok(10)) → 5
# print(krok(1)) → 4
def krokNie(n):
    if n%2 ==0:
        return n//2
    else:
        return 3*n+1

print(krokNie(6)) #3

def rownoboczny(a,b,c):
    if a == b and a == c and b == c:
        return 1
    else:
        return 0

if rownoboczny(5,7,5):
    print("Trojkat rownoboczny")
else:
    print("To nie jest trojkat rownoboczny")

        
    
    
    


# Zadanie 5.2
# Napisz funkcję czy_dzielnik(a, b), która zwraca “TAK”, gdy a dzieli się przez b bez reszty, a w przeciwnym razie “NIE”.
# Wywołania → wyniki:
# print(czy_dzielnik(10, 5)) → TAK
# print(czy_dzielnik(10, 3)) → NIE
# print(czy_dzielnik(7, 7)) → TAK

# Zadanie 5.3
# Napisz funkcję typ_dnia(nr), która dla numeru dnia tygodnia (1 to poniedziałek, 7 to niedziela) zwraca “weekend” dla 6 lub 7, a w pozostałych przypadkach “roboczy”.
# Wywołania → wyniki:
# print(typ_dnia(3)) → roboczy
# print(typ_dnia(6)) → weekend
# print(typ_dnia(7)) → weekend
# print(typ_dnia(1)) → roboczy

# Zadanie 5.4
# Napisz funkcję znizka(cena, kod), która zwraca połowę ceny (dzielenie całkowite przez 2), gdy kod to “ULGA”, a w przeciwnym razie zwraca niezmienioną cenę.
# Wywołania → wyniki:
# print(znizka(100, “ULGA”)) → 50
# print(znizka(100, “abc”)) → 100
# print(znizka(81, “ULGA”)) → 40

# KATEGORIA 6. Funkcje z warunkami, zwracające wartość (przy wywołaniu if jest potrzebny)

# Zadanie 6.1
# Napisz funkcję czy_parzystaNie, która zwraca 1, gdy n jest parzyste, a 0, gdy nieparzyste.
# Wywołanie:
# n = 8
# if czy_parzystaNie == 1: print(“Liczba parzysta”)
# Wyniki:
# n = 8 → Liczba parzysta
# n = 5 → (nic nie zostaje wypisane)
# n = 0 → Liczba parzysta

# Zadanie 6.2
# Napisz funkcję poprawne_hasloserce, która zwraca 1, gdy h to “python” lub “Python”, a w przeciwnym razie 0.
# Wywołanie:
# h = “python”
# if poprawne_hasloserce == 1: print(“Witaj”)
# if poprawne_hasloserce == 0: print(“Odmowa”)
# Wyniki:
# h = “python” → Witaj
# h = “Python” → Witaj
# h = “abc” → Odmowa

# Zadanie 6.3
# Napisz funkcję rownoboczny(a, b, c), która zwraca 1, gdy wszystkie trzy boki są równe, a w przeciwnym razie 0.
# Wywołanie:
# a = 4
# b = 4
# c = 4
# if rownoboczny(a, b, c) == 1: print(“Trojkat rownoboczny”)
# if rownoboczny(a, b, c) == 0: print(“To nie jest trojkat rownoboczny”)
# Wyniki:
# a = 4, b = 4, c = 4 → Trojkat rownoboczny
# a = 4, b = 4, c = 5 → To nie jest trojkat rownoboczny
# a = 7, b = 7, c = 7 → Trojkat rownoboczny

# Zadanie 6.4
# Napisz funkcję loteria(los), która zwraca 1, gdy numer losu jest podzielny przez 5 lub kończy się cyfrą 7, a w przeciwnym razie 0.
# Wywołanie:
# los = 15
# if loteria(los) == 1: print(“Wygrana!”)
# if loteria(los) == 0: print(“Brak wygranej”)
# Wyniki:
# los = 15 → Wygrana!
# los = 27 → Wygrana!
# los = 100 → Wygrana!
# los = 12 → Brak wygranej

# KATEGORIA 7. Zadania trudniejsze

# Zadanie 7.1
# Napisz funkcję rok_przestepny(r), która zwraca “TAK”, gdy rok jest przestępny (podzielny przez 4 i niepodzielny przez 100, albo podzielny przez 400), a w przeciwnym razie “NIE”.
# Podpowiedź: ustaw na początku wynik = “NIE”, a w if zmień go na “TAK”.
# Wywołania → wyniki:
# print(rok_przestepny(2024)) → TAK
# print(rok_przestepny(1900)) → NIE
# print(rok_przestepny(2000)) → TAK
# print(rok_przestepny(2023)) → NIE

# Zadanie 7.2
# Napisz funkcję suma_cyfrNie, która zwraca sumę cyfr liczby trzycyfrowej n.
# Wywołania → wyniki:
# print(suma_cyfr(123)) → 6
# print(suma_cyfr(405)) → 9
# print(suma_cyfr(999)) → 27
# print(suma_cyfr(100)) → 1

# Zadanie 7.3
# Napisz funkcję odwrocNie, która zwraca liczbę trzycyfrową n z cyframi w odwrotnej kolejności (jako liczbę).
# Wywołania → wyniki:
# print(odwroc(123)) → 321
# print(odwroc(405)) → 504
# print(odwroc(780)) → 87
# print(odwroc(100)) → 1

# Zadanie 7.4
# Napisz funkcję czas(s), która zamienia liczbę sekund na godziny, minuty i sekundy i wypisuje w formacie: g h m min s s
# Wywołania → wyniki:
# czas(3725) → 1 h 2 min 5 s
# czas(59) → 0 h 0 min 59 s
# czas(7200) → 2 h 0 min 0 s
# czas(86399) → 23 h 59 min 59 s

# Zadanie 7.5
# Napisz funkcję monety(kwota), która wypisuje, ile minimalnie monet 5 zł, 2 zł i 1 zł potrzeba do wydania kwoty (całkowitej). Wynik wypisz w jednej linii jako trzy liczby oddzielone spacją: liczba monet 5 zł, 2 zł, 1 zł.
# Wywołania → wyniki:
# monety(17) → 3 1 0
# monety(9) → 1 2 0
# monety(4) → 0 2 0
# monety(23) → 4 1 1

# Zadanie 7.6
# Napisz funkcję rozwiaz(a, b), która rozwiązuje równanie a*x + b = 0 i zwraca:

# “nieskonczenie wiele”, gdy a == 0 i b == 0
# “brak rozwiazan”, gdy a == 0 i b != 0
# w pozostałych przypadkach wartość x
# Wywołania → wyniki:
# print(rozwiaz(2, -6)) → 3.0
# print(rozwiaz(4, 2)) → -0.5
# print(rozwiaz(0, 0)) → nieskonczenie wiele
# print(rozwiaz(0, 5)) → brak rozwiazan
# Zadanie 7.7
# Napisz funkcję kalkulator(a, dzialanie, b), gdzie działanie to tekst: “+”, “-”, “” lub “/”. Funkcja zwraca wynik działania. Dla dzielenia przez zero zwraca “dzielenie przez 0”, a dla nieznanego działania zwraca “blad”.
# Wywołania → wyniki:
# print(kalkulator(6, “+”, 3)) → 9
# print(kalkulator(6, “-”, 3)) → 3
# print(kalkulator(6, “”, 3)) → 18
# print(kalkulator(6, “/”, 3)) → 2.0
# print(kalkulator(6, “/”, 0)) → dzielenie przez 0
# print(kalkulator(6, “^”, 3)) → blad

# Zadanie 7.8
# Napisz funkcję fizzbuzzNie, która zwraca:

# “FizzBuzz”, gdy n jest podzielne przez 3 i przez 5
# “Fizz”, gdy n jest podzielne tylko przez 3
# “Buzz”, gdy n jest podzielne tylko przez 5
# samo n w pozostałych przypadkach
# Wywołania → wyniki:
# print(fizzbuzz(15)) → FizzBuzz
# print(fizzbuzz(9)) → Fizz
# print(fizzbuzz(10)) → Buzz
# print(fizzbuzz(7)) → 7
# print(fizzbuzz(30)) → FizzBuzz