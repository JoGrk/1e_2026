# Zadanie 4 
# Napisz program, który wczyta tekst od użytkownika. Jeśli tekst jest pojedynczym znakiem (użyj funkcji len()), to sprawdź, czy jest to dokładnie znak 't' lub 'n'. Jeśli tekst ma inną długość, wypisz odpowiedni komunikat ostrzegawczy.

znak = input("podaj tekst: ")
if len(znak) == 1:
    if znak == "t" or znak == "n":
        print("znak to dokładnie t lub n")
    else:
        print("znak to nie t lub n")
else:
    print("tekst ma inną długość niż 1")