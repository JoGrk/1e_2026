# 1. Przekazywanie argumentów.

# A. Utwórz funkcję, która ma dwa parametry: wiek oraz imie, funkcja wypisuje: "witaj imie, masz wiek lat

def powitanie(wiek, imie):
    print(f"witaj {imie}, masz {wiek} lat")

# powitanie(14, "Hubert")

# B. wywołaj funkcję podając nieprawidłową kolejność parametrów

# powitanie("Patryk", 15)

# C. popraw podając nazwy parametrów

# powitanie(imie='Marcel', wiek=5)
# Po co te nazwy argumentów? Oprócz tego, że może nie pamiętamy kolejności, ale znamy nazwy?

# 2. Funkcje mogą też przyjąć dowolną liczbę nienazwanych argumentów. Służy do tego  *args (nazwa args jest umowna i tradycyjna)

# A. Napisz funkcję, która będzie miała dwa parametry: powitanie, domyślnie "Witaj: " oraz listę argumentów pozycyjnych (*args)(nienazwanych, zmienna lista argumentów). Funkcja wypisuje najpierw powitanie, a potem swój drugi argument

def funkcja(*args, powitanie="witaj: "):
    print(powitanie, *args)




# B. wywołaj funkcję podając tylko imiona

funkcja("Jakub","Aleks","Patryk")

# C. wywołaj funkcję dopisując na końcu nowe powitanie (nie używaj nazw parametrów)
funkcja("Colin", "Aleks", "Pawełek", "Czesc")
# D. Wywołaj funkcję zmieniając powitanie

funkcja("Colin", "Aleks", "Pawełek", powitanie="Czesc")

# ----------------------------------

# 4.Dokąd sięga zmienna utworzona wewnątrz funkcji? (lokalna)

#def aa():
#    local = "test"
#    print(local)
#
#aa()
#print(local)

# 5. A zmienna utworzona poza funkcją?  (globalna)

# czy można wypisać jej wartość
# a jak zmienimy, czy zmieni się także po wykonaniu funkcji?

x = 10
def funkcja():
    x = 20
    print(x)

funkcja()   
print(x) 

# 6. A jeśli mamy zmienną lokalną i globalną o tej samej nazwie? która jest ważniejsza wewnątrz funkcji? czy zmienimy przy okazji też globalną?




# 7. Parametry funkcji są lokalne, czy globalne?


# 8. Lepiej jak funkcje wypisują wartość czy ją zwracają? - program obliczający pierwiastki równania kwadratowego


def delta()
    