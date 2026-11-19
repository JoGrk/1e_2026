# 1.Napisz program, który za pomocą pętli for obliczy sumę liczb znajdujących się na liście: [4, 7, 2, 9, 3]. Wyświetl obliczoną sumę.
suma = 0
for i in [4, 7, 2, 9, 3]:
    suma += i

print(suma)


# 2. Napisz program, który wyświetli tylko liczby parzyste z listy: [3, 8, 12, 5, 7, 16, 21, 4]

liczby = [3, 8, 12, 5, 7, 16, 21, 4]
for liczba in liczby:
    if liczba % 2 == 0 :
        print(liczba)

# 3. 

# Utwórz listę zawierającą 6 ocen ucznia. Następnie:
# wyświetl wszystkie oceny,
# oblicz sumę ocen,
# oblicz średnią ocen.
# Wykorzystaj pętlę for. 
oceny = [1, 2, 2, 3, 4, 5, 2, 6, 2, 3, 5]
suma = 0
for ocena in oceny:
    print(ocena, end=" ")
    
# 4. 
# Napisz program, który:
# wyświetli wszystkie temperatury,
# obliczy średnią temperaturę,
# policzy, ile temperatur było ujemnych,
# znajdzie najwyższą temperaturę.
# 5.  Utwórz listę zawierającą 10 liczb całkowitych.

# Pobierz od użytkownika liczbę i sprawdź, czy znajduje się ona na liście. Wyświetl odpowiedni komunikat.
 

# Lista może być argumentem funkcji. Dzięki temu funkcja może przetwarzać różne listy bez konieczności ich definiowania wewnątrz funkcji.
 
# 6. 
# Napisz funkcję suma(lista), która otrzymuje listę liczb i zwraca sumę jej elementów.
# Napisz funkcję main(), w której:
# utworzysz listę liczb,
# wywołasz funkcję suma(),
# wyświetlisz otrzymany wynik.
# 7. 

# Napisz funkcję maksimum(lista), która zwraca największy element przekazanej listy.
# Nie korzystaj z funkcji max().
# W funkcji main() utwórz listę, wywołaj funkcję i wyświetl wynik.

# 8. 

# Napisz funkcję policz_dodatnie(lista), która otrzymuje listę liczb całkowitych i zwraca liczbę elementów dodatnich.
# W funkcji main() utwórz listę, wywołaj funkcję i wyświetl wynik.
 
# 9. 
# Napisz funkcję analizuj_oceny(lista), która otrzymuje listę ocen i zwraca liczbę ocen pozytywnych (od 2 do 6).
# W funkcji main():
# utwórz listę ocen,
# wywołaj funkcję,
# wyświetl liczbę ocen pozytywnych.