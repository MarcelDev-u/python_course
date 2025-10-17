import math

# zad1
print("zad1")
x = 3
y = -4
product = x * y
if product > 0:
    print("iloczyn dodatni")
elif product < 0:
    print("iloczyn ujemny")
else:
    print("iloczyn rowny zero")

# zad2
print("zad2")
a = 4
b = -5
c = 1
delta = b**2 - 4 * a * c
if delta > 0:
    sqrt_delta = math.sqrt(delta)
    x1 = (-b - sqrt_delta) / (2 * a)
    x2 = (-b + sqrt_delta) / (2 * a)
    print("dwa miejsca zerowe:", x1, x2)
elif delta == 0:
    x0 = -b / (2 * a)
    print("jedno miejsce zerowe:", x0)
else:
    print("brak miejsc zerowych")

# zad3
print("zad3")
not_divisible_by_three = []
for number in range(1, 26):
    if number % 3 != 0:
        not_divisible_by_three.append(number)
print(not_divisible_by_three)

# zad4
print("zad4")
sequence = [1, 2, 3]
while len(sequence) < 8:
    next_value = sequence[-1] * sequence[-2] * sequence[-3]
    sequence.append(next_value)
print(sequence)

# zad5
print("zad5")
x = [1, 2, -2, 0, -6, 7, -11, 12, 12]
positive_numbers = []
for element in x:
    if element > 0:
        positive_numbers.append(element)
print(positive_numbers)

# zad6
print("zad6")
x = [4, 1, -1, 2, 4, 4, 6, 12, -2, -13, 1]
y = []
for element in x:
    if element > 0 and element not in y:
        y.append(element)
print(y)

# zad7
print("zad7")
cubes = [number**3 for number in range(1, 7)]
print(cubes)

# zad8
print("zad8")


def czy_dodatnia(number):
    if number > 0:
        return "dodatnia"
    if number < 0:
        return "ujemna"
    return "zero"


print(czy_dodatnia(3))
print(czy_dodatnia(-2))
print(czy_dodatnia(0))

# zad9
print("zad9")


def rozwiaz_rownanie_liniowe(a, b):
    if a == 0:
        if b == 0:
            return "nieskonczenie wiele rozwiazan"
        return "brak rozwiazan"
    return -b / a


print(rozwiaz_rownanie_liniowe(2, -4))
print(rozwiaz_rownanie_liniowe(0, 0))
print(rozwiaz_rownanie_liniowe(0, 3))

# zad10
print("zad10")


def czy_pierwsza(number):
    if number < 2:
        return "nie pierwsza"
    if number == 2:
        return "pierwsza"
    if number % 2 == 0:
        return "nie pierwsza"
    limit = int(number**0.5) + 1
    for divisor in range(3, limit, 2):
        if number % divisor == 0:
            return "nie pierwsza"
    return "pierwsza"


print(czy_pierwsza(5))
print(czy_pierwsza(12))
