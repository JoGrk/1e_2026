# 1. wczytuje liczbę i sprawdza czy jest dodatnia, ujemna lub równa 0

# a = int(input("podaj liczbę: "))
# if a>0:
#     print("liczba jest dodatnia")
# elif a==0:
#     print("liczba jest 0")
# else:
#     print("liczba jest ujemna")

# 2. Zadeklaruj zmienną całkowitą miesiac oraz zmienna dzien. Wczytaj wartości tych zmiennych. Upewnij się, że są prawidłowe (miesiąc mieści się w zakresie od 1do 12, a dzień w zakresie od 1 do 31)

# #iesiac = int(input("Wczytaj miesiąc (od 1 do 12): "))
# #dzien = int(input("Wczytaj dzień (od 1 do 31)"))

# #if miesiac > 12 or miesiac < 1:
#     print("Miesiąc nieprawidłowy")
# else:
#     print("Miesiąc prawidłowy")

# if miesiac == 2:
#     max=29
# elif miesiac == 4 or miesiac == 6 or miesiac == 9 or miesiac == 11:
#     max=30
# else:
#     max=31

# if dzien > max or dzien < 1:
#     print("dzien nieprawidłowy")
# else:
#     print("dzien prawidłowy")

# * upewnij się, że dzień odpowiada wybranemu miesiącu: tzn. dla stycznia <=31, dla lutego <=29, dla marca <=31 itd.

# 3. Wczytaj zmienną całkowitą a, upewnij się, że jest:
a = int(input('Podaj liczbe: '))
# A. dodatnią liczbą parzystą
# if a % 2 == 0 and a > 0:
#     print('Jest parzysta i jest większa od zera')
# else:
#     print('Nie spełniony warunek')
# B. podzielną przez 2 lub podzielną przez 3, ale jednocześnie nie jest podzielna przez 6
# if (a % 2 == 0 or a % 3 == 0) and a % 6 != 0:
#     print("Warunek jest spełniony.")
# else:
#     print("Warunek nie zostal spełniony.")

# C. mniejsza od -10, większa od 10 lub równa zero
if a < -10 or a > 10 or a == 0 :
    print("warunek jest spełniony")


# D. należy do przedziału (1,100>, ale jest różna od 10 i różna od 20
if a > 1 and a <= 100 and a != 10 and a != 20:
    print("warunek jest spełniony")
# 4. Wczyta znak. Upewni się, że jest on:

# A. wielką literą

# B. cyfrą

# C. małą lub wielką literą

# D. 't', 'T', 'n' lub 'N'