# 1. wczytuje liczbę i sprawdza czy jest dodatnia, ujemna lub równa 0

a = int(input("podaj liczbę: "))
if a>0:
    print("liczba jest dodatnia")
elif a==0:
    print("liczba jest 0")
else:
    print("liczba jest ujemna")

# 2. Zadeklaruj zmienną całkowitą miesiac oraz zmienna dzien. Wczytaj wartości tych zmiennych. Upewnij się, że są prawidłowe (miesiąc mieści się w zakresie od 1do 12, a dzień w zakresie od 1 do 31)

# * upewnij się, że dzień odpowiada wybranemu miesiącu: tzn. dla stycznia <=31, dla lutego <=29, dla marca <=31 itd.
# 3. Wczytaj zmienną całkowitą a, upewnij się, że jest:

# A. dodatnią liczbą parzystą

# B. podzielną przez 2 lub podzielną przez 3, ale jednocześnie nie jest podzielna przez 6

# C. mniejsza od -10, większa od 10 lub równa zero

# D. należy do przedziału (1,100>, ale jest różna od 10 i różna od 20

# 4. Wczyta znak. Upewni się, że jest on:

# A. wielką literą

# B. cyfrą

# C. małą lub wielką literą

# D. 't', 'T', 'n' lub 'N'