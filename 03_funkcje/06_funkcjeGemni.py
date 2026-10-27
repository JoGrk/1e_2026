# ### 1. Funkcje bez parametrów, niezwracające wartości

# #### Zadanie 1.1
# Napisz funkcję `powitanie()`, która wypisuje tekst "Witaj w świecie Pythona!".
# * **Wywołanie:** `powitanie()`
# * **Oczekiwany wynik:** `Witaj w świecie Pythona!`

# #### Zadanie 1.2
# Napisz funkcję `linia()`, która wypisuje linię złożoną z 20 gwiazdek (`********************`).
# * **Wywołanie:** `linia()`
# * **Oczekiwany wynik:** `********************`

# #### Zadanie 1.3
# Napisz funkcję `autor()`, która pobiera od użytkownika jego imię za pomocą `input()`, a następnie wypisuje komunikat "Program napisał: [imię]".
# * **Wywołanie:** `autor()`
# * **Test (wpisano: Jan):** `Program napisał: Jan`

# #### Zadanie 1.4
# Napisz funkcję `menu()`, która wypisuje trzy opcje menu: "1. Start", "2. Opcje", "3. Koniec". Każda opcja powinna być w nowej linii.
# * **Wywołanie:** `menu()`
# * **Oczekiwany wynik:**
#   ```text
#   1. Start
#   2. Opcje
#   3. Koniec
#   ```

# ---

# ### 2. Funkcje z parametrami (1-3), niezwracające wartości

# #### Zadanie 2.1
# Napisz funkcję `kwadrat(bok)`, która przyjmuje długość boku i wypisuje pole kwadratu.
# * **Wywołanie:** `kwadrat(5)`
# * **Oczekiwany wynik:** `25`

# #### Zadanie 2.2
# Napisz funkcję `imie_wiek(imie, wiek)`, która przyjmuje tekst i liczbę, a następnie wypisuje komunikat: "[imie] ma [wiek] lat.".
# * **Wywołanie:** `imie_wiek("Anna", 16)`
# * **Oczekiwany wynik:** `Anna ma 16 lat.`

# #### Zadanie 2.3
# Napisz funkcję `cena_brutto(netto, vat)`, która przyjmuje cenę netto oraz wartość podatku VAT (np. 23 dla 23%). Funkcja ma obliczyć i wypisać cenę brutto.
# * **Wywołanie:** `cena_brutto(100, 23)`
# * **Oczekiwany wynik:** `123.0`

# #### Zadanie 2.4
# Napisz funkcję `srednia_trzech(a, b, c)`, która przyjmuje trzy liczby i wypisuje ich średnią arytmetyczną.
# * **Wywołanie:** `srednia_trzech(4, 5, 6)`
# * **Oczekiwany wynik:** `5.0`

# ---

# ### 3. Funkcje zwracające wartość (wypisywaną przy wywołaniu)

# #### Zadanie 3.1
# Napisz funkcję `pole_prostokata(a, b)`, która zwraca pole prostokąta o bokach `a` i `b`.
# * **Wywołanie:** `print(pole_prostokata(4, 5))`
# * **Oczekiwany wynik:** `20`

# #### Zadanie 3.2
# Napisz funkcję `sekundy(minuty)`, która przelicza podane minuty na sekundy i zwraca wynik.
# * **Wywołanie:** `print(sekundy(5))`
# * **Oczekiwany wynik:** `300`

# #### Zadanie 3.3
# Napisz funkcję `cal_na_cm(cale)`, która przelicza długość w calach na centymetry (1 cal = 2.54 cm) i zwraca wynik.
# * **Wywołanie:** `print(cal_na_cm(10))`
# * **Oczekiwany wynik:** `25.4`

# #### Zadanie 3.4
# Napisz funkcję `reszta_z_dzielenia(x, y)`, która zwraca resztę z dzielenia liczby `x` przez `y`.
# * **Wywołanie:** `print(reszta_z_dzielenia(10, 3))`
# * **Oczekiwany wynik:** `1`

# ---

# ### 4. Funkcje wykorzystujące warunki (if, ==, !=, or, and), niezwracające wartości

# #### Zadanie 4.1
# Napisz funkcję `czy_dodatnia(liczba)`, która wypisuje "Liczba jest dodatnia", jeśli parametr jest większy od zera, lub "Liczba nie jest dodatnia" w przeciwnym wypadku.
# * **Wywołanie:** `czy_dodatnia(-5)`
# * **Oczekiwany wynik:** `Liczba nie jest dodatnia`

# #### Zadanie 4.2
# Napisz funkcję `sprawdz_haslo(haslo)`, która wypisuje "Dostęp przyznany", jeśli podane hasło to "tajne123". W przeciwnym razie wypisuje "Błędne hasło".
# * **Wywołanie:** `sprawdz_haslo("admin")`
# * **Oczekiwany wynik:** `Błędne hasło`

# #### Zadanie 4.3
# Napisz funkcję `znizka(wiek, status)`, która przyjmuje wiek (liczba) oraz status studenta (tekst "tak" lub "nie"). Jeśli wiek jest mniejszy niż 26 AND status to "tak", wypisuje "Zniżka przysługuje". W innym wypadku wypisuje "Brak zniżki".
# * **Wywołanie:** `znizka(20, "tak")`
# * **Oczekiwany wynik:** `Zniżka przysługuje`

# #### Zadanie 4.4
# Napisz funkcję `bilet(wiek)`, która wypisuje "Darmowy" dla dzieci do lat 7 (włącznie) OR seniorów od 65 lat (włącznie). Dla pozostałych wypisuje "Płatny".
# * **Wywołanie:** `bilet(70)`
# * **Oczekiwany wynik:** `Darmowy`

# ---

# ### 5. Funkcje z warunkami, zwracające wartość (bez użycia if przy wywołaniu)

# #### Zadanie 5.1
# Napisz funkcję `wieksza(a, b)`, która porównuje dwie liczby i zwraca tę, która jest większa.
# * **Wywołanie:** `print(wieksza(12, 17))`
# * **Oczekiwany wynik:** `17`

# #### Zadanie 5.2
# Napisz funkcję `koszt_wysylki(wartosc_zamowienia)`, która zwraca 0, jeśli wartość zamówienia wynosi 200 lub więcej. W przeciwnym wypadku zwraca 15.
# * **Wywołanie:** `print(koszt_wysylki(150))`
# * **Oczekiwany wynik:** `15`

# #### Zadanie 5.3
# Napisz funkcję `zdany_egzamin(punkty)`, która zwraca tekst "Zdałeś", jeśli punkty są równe lub większe od 50. W przeciwnym razie zwraca "Spróbuj ponownie".
# * **Wywołanie:** `print(zdany_egzamin(55))`
# * **Oczekiwany wynik:** `Zdałeś`

# #### Zadanie 5.4
# Napisz funkcję `cena_promocyjna(kod, cena)`, która zwraca cenę obniżoną o 20%, jeśli kod to "START20". Jeśli kod jest inny, zwraca niezmienioną cenę.
# * **Wywołanie:** `print(cena_promocyjna("START20", 100))`
# * **Oczekiwany wynik:** `80.0`

# ---

# ### 6. Funkcje z warunkami, zwracające wartość (wymagające użycia if przy wywołaniu)

# #### Zadanie 6.1
# Napisz funkcję `czy_parzysta(liczba)`, która zwraca `True`, jeśli liczba jest parzysta, lub `False`, jeśli jest nieparzysta. Wywołaj funkcję i za pomocą `if` wypisz komunikat "Liczba jest parzysta" lub "Liczba jest nieparzysta".
# * **Wywołanie:**
#   ```python
#   if czy_parzysta(7):
#       print("Liczba jest parzysta")
#   else:
#       print("Liczba jest nieparzysta")
#   ```
# * **Oczekiwany wynik:** `Liczba jest nieparzysta`

# #### Zadanie 6.2
# Napisz funkcję `walidacja_loginu(login)`, która zwraca `True`, jeśli login NIE jest pustym tekstem `""`, oraz `False`, jeśli jest pusty. Użyj `if` przy wywołaniu, aby wypisać "Poprawny login" lub "Błąd: pusty login".
# * **Wywołanie:**
#   ```python
#   if walidacja_loginu(""):
#       print("Poprawny login")
#   else:
#       print("Błąd: pusty login")
#   ```
# * **Oczekiwany wynik:** `Błąd: pusty login`

# #### Zadanie 6.3
# Napisz funkcję `pelnoletni(wiek)`, która zwraca `True`, jeśli wiek wynosi minimum 18 lat, w innym wypadku `False`. Wywołaj funkcję w instrukcji `if`, wypisując odpowiednio "Możesz wejść" lub "Wstęp wzbroniony".
# * **Wywołanie:**
#   ```python
#   if pelnoletni(16):
#       print("Możesz wejść")
#   else:
#       print("Wstęp wzbroniony")
#   ```
# * **Oczekiwany wynik:** `Wstęp wzbroniony`
def pelnoletni(wiek):
    if wiek>= 18:
        return True
    else:
        return False

wiek = int(input("podaj swój wiek: "))
if pelnoletni(wiek):
    print("możesz wejść")
else:
    print("wstęp wzbroniony")

kolega = int(input("Podaj wiek kolegi: "))
if pelnoletni(kolega):
    print("Mozesz wejsc")
else:
    print("Wstęp wzbroniony")


# #### Zadanie 6.4
# Napisz funkcję `czy_podzielna_przez_3Nie`, która zwraca `True`, jeśli liczba dzieli się bez reszty przez 3, w innym wypadku `False`. Przy wywołaniu użyj `if`, aby wypisać "Podzielna" lub "Niepodzielna".
# * **Wywołanie:**
#   ```python
#   if czy_podzielna_przez_3(9):
#       print("Podzielna")
#   else:
#       print("Niepodzielna")
#   ```
# * **Oczekiwany wynik:** `Podzielna`

# ---

# ### 7. Zadania trudniejsze (tylko dozwolone instrukcje i operatory)

# #### Zadanie 7.1
# Napisz funkcję `rok_przestepny(rok)`, która zwraca `True`, jeśli rok jest podzielny przez 4 AND nie jest podzielny przez 100, LUB jest podzielny przez 400. W przeciwnym wypadku zwraca `False`.
# * **Wywołanie:** `print(rok_przestepny(2000))`
# * **Oczekiwany wynik:** `True`

# #### Zadanie 7.2
# Napisz funkcję `najwieksza_z_trzech(a, b, c)`, która za pomocą instrukcji `if`, `and` oraz `or` znajduje i zwraca największą z trzech podanych liczb.
# * **Wywołanie:** `print(najwieksza_z_trzech(15, 42, 23))`
# * **Oczekiwany wynik:** `42`

# #### Zadanie 7.3
# Napisz funkcję `kalkulator(a, b, znak)`, która przyjmuje dwie liczby oraz znak operacji (`"+"`, `"-"`, `*`, `"/""`). Funkcja ma wykonać odpowiednie obliczenie i zwrócić wynik.
# * **Wywołanie:** `print(kalkulator(10, 5, "*"))`
# * **Oczekiwany wynik:** `50`

# def kalkulator(a,b,znak):        
    
#     if znak == "+" :
#         return a + b 
#     elif znak == "-":
#         return a - b 
#     elif znak == "*" :
#         return a * b 
#     elif znak == "/" :
#         return a / b 
#     else:
#         return "Nieprawidłowy znak!"

# print(kalkulator(5,10,"*"))


# #### Zadanie 7.4
# Napisz funkcję `kwadrant(x, y)`, która przyjmuje współrzędne punktu i wypisuje, w której ćwiartce układu współrzędnych się znajduje (np. "Ćwiartka 1", "Ćwiartka 2" itd.), lub "Punkt na osi", jeśli `x == 0` lub `y == 0`.
# * **Wywołanie:** `kwadrant(-3, 4)`
# * **Oczekiwany wynik:** `Ćwiartka 2`

# #### Zadanie 7.5
# Napisz funkcję `czy_trojkat(a, b, c)`, która sprawdza warunek trójkąta (suma dwóch dowolnych boków musi być większa od trzeciego). Funkcja zwraca `True` lub `False`.
# * **Wywołanie:** `print(czy_trojkat(3, 4, 8))`
# * **Oczekiwany wynik:** `False`

# #### Zadanie 7.6
# Napisz funkcję `bmi(waga, wzrost_m)`, która oblicza wskaźnik BMI ze wzoru `waga / wzrost_m**2`. Jeśli wynik wynosi mniej niż 18.5, funkcja wypisuje "Niedowaga". Jeśli od 18.5 do 25 (bez 25), wypisuje "Norma". Dla 25 i więcej wypisuje "Nadwaga".
# * **Wywołanie:** `bmi(70, 1.75)`
# * **Oczekiwany wynik:** `Norma`

def bmi(waga, wzrost_m):
    return waga / wzrost_m**2

if bmi(70, 1.75) < 18.5:
    print("Niedowaga")
elif bmi(70, 1.75) < 25:
    print("norma")
else:
    print("nadwaga")





# #### Zadanie 7.7
# Napisz funkcję `bilet_wielokrotny(wiek, znizka_karta)`, która oblicza cenę biletu (cena bazowa to 20 zł). Jeśli użytkownik ma mniej niż 18 lat OR ma kartę zniżkową (status `"tak"`), bilet kosztuje 10 zł. Jeśli spełnia oba warunki naraz, bilet kosztuje 5 zł. W pozostałych przypadkach cena to 20 zł. Funkcja zwraca cenę.
# * **Wywołanie:** `print(bilet_wielokrotny(15, "tak"))`
# * **Oczekiwany wynik:** `5`

# #### Zadanie 7.8
# Napisz funkcję `formatuj_czas(sekundy)`, która przyjmuje całkowitą liczbę sekund i oblicza, ile to pełnych godzin i minut pozostałych z tych sekund. Wypisuje wynik w formacie: "[godziny]h [minuty]m". Użyj operatorów `//` oraz `%`.
# * **Wywołanie:** `formatuj_czas(10000)`
# * **Oczekiwany wynik:** `2h 46m`