# 1.Używając tylko jednej instrukcji print wyświetl 100x nazwę ulubionego filmu lub bajki.
# print(100*"StarWar")
# 2. Używając instrukcji Pythona oblicz resztę z dzielenia 11 przez 7 i zapamiętaj wynik w zmiennej o nazwie Z.
# Następnie, pojedynczym poleceniem Pythona i bez użycia nawiasów, przemnóż zmienną Z przez Z+1.
z = 11 % 7 
z*=z+1 
print(z)
# 3. Napisz program, który pyta użytkownika o cenę jednego biletu do kina oraz o liczbę osób, które chcą kupić bilet. Program ma obliczyć i wyświetlić łączny koszt wyprawy do kina.

#x = int(input("liczba osób: "))
#y = int(input("kost biletu: "))
#print(f"kost wyczieczki: {x * y}")

# 4. Napisz program, który pobierze od kierowcy trzy informacje: długość trasy w kilometrach, średnie spalanie samochodu (w litrach na 100 km) oraz aktualną cenę paliwa za litr. Program ma obliczyć, ile litrów paliwa zużyje auto oraz jaki będzie całkowity koszt tej podróży.
# d = int(input("długość trasy:"))
# spalanie =  float(input("spalanie"))
# cena = float(input("podaj cene: "))
# litry = d * spalanie / 100 
# print(f"auto zużyje {litry} litrów i to będzie kosztować {litry * cena}zł")

# 5. Napisz program, który zamieni minuty na godziny i minuty. Program wczytuje liczbę minut, wyświetla w formacie takim jak w poniższym przykładzie: dla 220 będzie to 3h 40min
m = int(input("podaj liczbę minut"))
g = m // 60
print(f"{g}h {m % 60}min")
# ------------------------------------

# Do tych zadań na samym początku kodu dopisz import math. Pozwoli Ci to na użycie stałej math.pi oraz funkcji takich jak math.sqrt() (pierwiastek) czy math.sin().
 
# 6. Napisz program wczytujący promień (jako liczbę rzeczywistą, czyli float) i wypisujacy pole oraz obwód koła