
# Utwórz funkcję w pionie, która wypisuje w pionie tekst, który dostanie jako swój parametr
def pion(tekst) :
    for znak in tekst:
        print(znak)



# Utwórz funkcje powtarzaj, która wypisuje każdy znak z tekstu podanego jako jej parametr tekst, tyle razy, ile wynosi jej drugi parametr. Na przykład powtarzaj('sos', 3) da efekt sssooosss
def powtarzaj(tekst, ilosc):
    for znak in tekst: 
        print(znak * ilosc, end="")





# Utwórz funkcję policz_a, z jednym parametrem, który jest jej tekstem, która policzy ile w tym tekście jest liter a. Funkcja zwraca tę wartość. Wywołaj funkcję dla tekstu wczytanego i wypisz jej efekt w postaci: "tekst {tekst} ma ilość znaków a : {wynikfunkcji}". Na przykład: policz_a('koty za płoty') -> tekst koty za płoty ma ilość znaków a: 1

def policz_a(tekst):
    ilosc = 0
    for znak in tekst:
        if znak == "a":
            ilosc+=1
    return ilosc



# Utwórz funkcję policz_znak(tekst, znak), która policzy ile w tym tekście jest znaków podanych jako jej drugi parametr. Funkcja zwraca tę ilość. Wywołaj funkcję dla tekstu wczytanego i wypisz jej efekt w postaci: "tekst {tekst} ma ilość znaków {znak} : {wynikfunkcji}". Wywołaj funkcję dla tekstu i znaku wczytanego z klawiatury.

def policz_znak(tekst, literka):
    liczenie = 0
    for znak in tekst:
        if znak == literka:
            liczenie += 1
    return liczenie
# Utwórz funkcję szyfruj, której argumentem będzie tekst. Funkcja szyfruje go, przesuwając każdą małą literę alfabetu o 4 pozycje w prawo. Wykorzystaj funkcję do zaszyfrowania tekstu
# A. funkcja iteruje po tekście (pobiera kolejny znak)
# B. zamienia znak na kod, dodaje 4, zamienia z powrotem na znak
# C. dokleja znak do tekstu
# D. zwraca gotowy, zaszyfrowany tekst

def szyfruj(tekst):
    szyfrowany = ""
    for znak in tekst:
        kod = ord(znak)
        kod += 4
        znak2 = chr(kod)
        szyfrowany += znak2
    return szyfrowany


# -----------

napis = input("podaj tekst: ") 
pion(napis)
powtarzaj(napis, 3)
print(f"\ntekst, {napis} ma {policz_a(napis)} znaków a")
z = input("Podaj znak : ")
print(f'Tekst, {napis} ma {policz_znak(napis, z)} znaków jest : {z}')
print(f"tekst po polsku: {napis}")
print("tekst po szyfrowaniu ", szyfruj(napis))

