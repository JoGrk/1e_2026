# 1.

# Używając jednego z operatorów porównania w Pythonie, napisz prosty, dwuwierszowy program, który przyjmuje parametr n jako dane wejściowe (będący liczbą całkowitą) i wyświetla False, jeśli n jest mniejsze niż 100 i True, jeśli n jest większe lub równe 100.

# Nie twórz żadnych bloków if

#n = int(input("podaj liczbe: "))
#print(n>=100)

# 2. Sprawdź, czy wczytana liczba jest większa od zera. Wypisz: dodatnia lub nie jest dodatnia

#n = int(input("podaj liczbe: "))
#if n > 0:
#    print("liczba jest dodatnia")
#else:
#    print("liczba nie jest dodatnia")

# 3. Sprawdź, czy wczytana liczba jest równa zero, wypisz zero lub nie zero

#wczytywana = int(input('Twoja wczytywana: '))

#if wczytywana == 0:
 #   print('Zero')
#else:
  #  print('Nie zero')

# 4. Wczytaj dwie liczby i wypisz ich iloraz (wynik dzielenia). Upewnij się, że możesz dzielić, jeśli nie - wypisz komunikat "nigdy... nie dziel przez zero"

# a =int(input("podaj liczbe 1:"))
# b =int(input("podaj liczbe 2:"))
# if b == 0:
#     print("nigdy nie dziel przez 0")
# else:
#     print(f"wynik dzielenia:{a/b}")





# 5.  Napisz program, który wczytuje dwie liczby i wypisuje większą z nich

# a =int(input("podaj liczbe 1:"))
# b =int(input("podaj liczbe 2:"))
# if a > b:
#     print(f"większa liczba {a}")
# else:
#     print(f"wienksa liczba {b}")

# 6. Napisz program, który wczytuje trzy liczby i wypisuje największą 

# a = int(input("Podaj liczbe: "))
# b = int(input("Podaj liczbe: "))
# c = int(input("Podaj liczbe: "))
# if a>b :
#     if a>c :
#         print(f'Największa liczbą jest {a}')
#     else :
#         print(f'Największą liczbą jest {c}')
# else:
#     if b>c:
#         print(f"Największą liczbą jest {b}")
#     else:
#         print(f"Największą liczbą jest {c}")

 
# 7. Sprawdź, czy wczytana liczba jest parzysta (podzielna przez 2), czy nieparzysta

# a = int(input("podaj liczbę"))
# if a%2 == 0:
#     print("liczba jest parzysta")
# else:
#     print("liczba nie jest parzysta")


# 8. Od czasu wprowadzenia kalendarza gregoriańskiego (w 1582 r.), poniższa reguła jest używana do określania rodzaju roku:



# jeśli numeru roku nie jest podzielny przez cztery, jest to rok zwykły;
# w przeciwnym razie, jeśli numer roku nie jest podzielny przez 100, jest to rok przestępny;
# w przeciwnym razie, jeśli numer roku nie jest podzielny przez 400, będzie to rok zwykły;
# w przeciwnym razie jest to rok przestępny.
# wczytaj rok i korzystając z elif wypisz czy jest przestępny, czy zwykły

print("Sprawdzam czy rok jest przestępny")

rok =int(input("Podaj rok"))

if rok > 1582:

    if(rok % 4 != 0):
        print("rok zwykły")
    elif rok % 100 != 0:
        print("rok przestępny")
    elif rok % 400 != 0:
        print("rok zwykły")
    else:
        print("rok przestępny")
else:
    print("rok nie jest gregoriański")


