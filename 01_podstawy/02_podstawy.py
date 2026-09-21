# 1.  Napisz program, który pyta użytkownika o podstawę i wysokość trójkąta i oblicza jego pole (0.5×podstawa×wysokosc).
# A. wypisz tekst "program oblicza pole trójkąta "
# B wczytaj wartosc zmiennej a - prompt  "podaj podstawe: "
# C. wczytaj wartosc zmiennej h - prompt "podaj wysokosc: ".
# D. wypisz tekst "pole trojkata wynosi: ", a następnie wartość wyrażenia 0.5*a*h

#print("program oblicza pole trójkąta")
#a = int(input("podaj podstawe "))
#h = int(input("podaj wysokosc "))
#print("pole trójkąta wynosi:", 0.5*a*h)

# 2. Napisz program pozwalający przeliczyć cale na centymetry (1 cal = 2,54 centymetra).
# A. Wypisz tekst "program przelicza cale na centymetry. "
# B. wczytaj zmienną cale - prompt "Podaj ile cali: "
# C. Wypisz tekst "Centymetry: "
# D. Wypisz wyrażenie cale*2.54

# print("program przelicza cale na centymetry.")
# cale = int(input("Podaj ile cali: "))
# print("Centymery" , cale * 2.5)

# 3.  Napisz program, który wczytuje Twoją masę (podaną w kg) i wzrost (podany w cm) i na tej podstawie wylicza i wypisuje BMI. Wzór poniżej:
# masa / (wzrost*wzrost) 
# a = int(input("podaj wage:"))
# b = int(input("podaj wzrost w centymetrach:"))
# b = b/100
# c = int(a/(b*b))
# print("b wynik wynoś", c )




# 4. Napisz program, który zapyta się o nazwę budynku i rok budowy. Nazwę budynku wczytaj do zmiennej. W wyniku zwróci nazwę i wiek budynku tak, jak na przykładzie poniżej:
# Podaj nazwę budynku; 
# Podaj rok budowy:
# Budynek nazywa się .... został wybudowany w .... i ma teraz .... lat
# (w miejsce ... program powinien wypisać właściwe wartości, np. dla ratusza wybudowanego w 1921 będzie to :

# Budynek nazywa się ratusz, został wybudowany w 1921 i ma teraz 100 lat

nazwa = input("podaj nazwe budynku: ")
rok = int(input("podaj rok budowy: "))
print(f"Budynek nazywa się {nazwa} został wybudowany w {rok} i ma teraz {2026-rok} lat")


# 5. Napisz program, który z pomocą jednej instrukcji print napisze na ekranie następujący tekst: 

# witamy 
# na
# p
# o
# kladzie

# print("witamy\nna\np\no\nkladzie")