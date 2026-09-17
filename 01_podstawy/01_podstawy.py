# 1. Zmodyfikuj pierwszą linię kodu w edytorze, używając słów kluczowych sep i end, 

print("Programming","Essentials","in", sep="***", end="...")
print("Python")

# 2.Napisz jednolinijkowy fragment kodu, korzystając z funkcji print(), a także znaku nowego wiersza i znaku zmiany znaczenia, aby dopasować oczekiwany wynik w trzech wierszach.

print("\"I'm\"",'""learning""','"""python"""', sep="\n")

# 3. Pamiętając o tym, że 1 mila jest równa w przybliżeniu 1,61 kilometra, należy wypełnić program w edytorze, tak aby konwertował:

kilometers = 12.25
miles = 7.38

miles_to_kilometers = miles * 1.61
kilometers_to_miles = kilometers / 1.61

print(miles, "miles is", round(miles_to_kilometers, 2), "kilometers")
print(kilometers, "kilometers is", round(kilometers_to_miles, 2), "miles")

# 4. Twoim zadaniem jest uzupełnienie kodu w celu obliczenia następującego wyrażenia:
#x = float(input("Enter value for x: "))

# Write your code here.
#y=1/(x + 1/(x + 1/(x + 1/x)))
#print("y =", y)

print("Program przelicza bity na bajty.")

b = int(input("Podaj bity: "))

print("Bajty: ",b/8)