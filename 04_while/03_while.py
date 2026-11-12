# 1. Obliczamy zebraną sumę do skarbonki
# A. opisz przeznaczenie programu, wczytaj liczby, wykorzystując funkcję, wypisz wynik
# B. napisz funkcję suma_liczb(), która wczytuje liczby całkowite aż do podania wartości 0. Funkcja ma zwrócić sumę wszystkich wprowadzonych liczb (bez zera).

#def suma_skarbonki():
#    x = int(input("podaj pieniądze: "))
#    suma = 0
#    while x != 0:
#        suma += x
#        x = int(input("podaj pieniądze: "))
#    return suma
#
#print("program liczy pieniadze z skarbonki")
#print(suma_skarbonki())



# 2. Wykonujemy kolejne zadania z naszej i liczymy je. Przygotuj:

# A. funkcję liczba_zadan(), która wczytuje kolejne zadanie (tekst) aż do podania wartości koniec  i zwraca liczbę wykonanych zadań.
# B. funkcję main(), która wyświetla liczbę zadań zwróconą przez funkcję


def liczba_pomiarow():
    liczba_zadan = 0
    pomiar = (input("Podaj tekst: "))
    while pomiar != "koniec" :
        liczba_zadan += 1
        pomiar = (input("Podaj tekst: "))
    return liczba_zadan

def main():
    print(liczba_pomiarow())

main()






# 3.Wczytujemy pomiary poziomu rzeki, umawiamy się, że -1 kończy podawanie liczb

# A. funkcje srednia_pomiarow() wczytuje wyniki pomiarów aż do podania wartości 0, oblicza średnią wszystkich pomiarów i zwraca obliczoną średnią
# B. funkcja main(), która wyświetla średnią pomiarów






# 4. Napisz funkcję maksimum(), która:

# wczytuje liczby całkowite aż do podania wartości 0,
# znajduje największą z podanych liczb,
# zwraca tę liczbę.
# Napisz funkcję main(), która wyświetla największą wartość.

 
 
# 5. Napisz funkcję policz_dodatnie(), która:
# wczytuje liczby aż do podania wartości 0,
# zlicza, ile z nich jest dodatnich,
# zwraca otrzymany wynik.
# Napisz funkcję main(), która wyświetla liczbę dodatnich wartości.


 
# 6.  Napisz funkcję suma_punktow(), która:
# wczytuje liczbę punktów zdobytych przez kolejnych uczniów,
# kończy wprowadzanie po wpisaniu wartości -1,
# zwraca sumę punktów wszystkich uczniów.
# Napisz funkcję main(), która wyświetla łączną liczbę punktów.



 
# 7.  Napisz funkcję logowanie(), która prosi użytkownika o podanie hasła.
# Wprowadzanie danych trwa do momentu wpisania hasła: Python123
# Funkcja ma zwrócić liczbę wykonanych prób logowania.
# Napisz funkcję main(), która wyświetla tę liczbę.



 
# 8.  Napisz funkcję minimalna_temperatura(), która:
# wczytuje temperatury,
# kończy działanie po podaniu wartości 999,
# zwraca najniższą temperaturę.
# Napisz funkcję main(), która wyświetla wynik.



 
# 7.  Napisz funkcję policz_parzyste(), która:
# wczytuje liczby całkowite aż do podania 0,
# zlicza liczby parzyste,
# zwraca ich liczbę.
# Napisz funkcję main(), która wyświetla wynik.



 
# 8.  Napisz funkcję licznik_ocen(), która:
# wczytuje oceny z przedziału 1–6,
# kończy działanie po podaniu 0,
# zlicza oceny pozytywne (2–6),
# zwraca ich liczbę.
# Napisz funkcję main(), która wyświetla wynik.



 
# 9. 
# Napisz funkcję srednia_dodatnich(), która wczytuje liczby aż do podania 0. Przy obliczaniu średniej należy uwzględnić wyłącznie liczby dodatnie.



 
# 10. 
# Napisz funkcję wadliwe_produkty(), która wczytuje wyniki kontroli jakości. Wartość:
# 1 oznacza produkt poprawny,
# 0 oznacza produkt wadliwy,
# -1 kończy wprowadzanie danych.
# Funkcja ma zwrócić liczbę wadliwych produktów.