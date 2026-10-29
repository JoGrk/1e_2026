# Please write a function named line, which takes two arguments: an integer and a string. The function prints out a line of text, the length of which is specified by the first argument. The character used to draw the line should be the first character in the second argument. If the second argument is an empty string, the line should consist of stars.
# def line(tekst, liczba):
#     print(tekst*liczba)

# line("Marysieklubijabłuszko", 9)

# def line(liczba, tekst = "*"):
#     print(tekst * liczba)

# line(3,"Oleklubibanany")
# line(10)




# Rozbuduj tę funkcję tak, aby w przypadku, jeśli nie został podany znak, był wyświetlony znak '-', a jeśli dodatkowo nie podamy ilości, to będzie wypisane 20 znaków. Wypróbuj.

# def line(liczba = 10, tekst = "*"):
#     print(tekst * liczba)

# line(3,"Oleklubibanany")
# line(20)
# line()

# 2. Napisz funkcję, która będzie miała cztery parametry: szerokość, długość, wysokość, koszt). Funkcja oblicza koszt pomalowania pokoju. Zakładamy domyślną wartość wysokości 2.7, a koszt będzie wynosił 40zł z metr kwadratowy. wywołaj dla różnych argumentów,

# def painting_price(width, length, height = 2.7, cost = 40):
#     print(width*length*height*cost)

# painting_price(5, 8)

# 3, funkcję, która generuje pełne imię i nazwisko, przyjmując jako argumenty imię, drugie imię (opcjonalnie) oraz nazwisko. Chcemy, aby drugie imię było parametrem opcjonalnym, który w przypadku niepodania przyjmie wartość domyślną None.  Wywołaj dla róznych argumentów.

# def nameandother(name, surname, secondname = None):
#     return name + " " + secondname + " " + surname
# print(nameandother('Imie', 'Nazwisko'))

def nameandother(name, surname, secondname = None):
    if secondname:
        return name + " " + secondname + " " + surname
    else:
        return name + " " + surname
print(nameandother('Imie', 'Nazwisko'))