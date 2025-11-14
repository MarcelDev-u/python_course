"""
Rozwiązanie zadania 6
"""

# silnia
def factorial(x: int):
    a = 1
    for i in range(x):
        a *= i + 1

    return a

# zad 6 funkcja
def calc(a:int, b:float):
    return factorial(a) / (b**2 + abs(b) + 1)

a = int(input('a<int>: '))
b = float(input('b<float>: '))
print(calc(a, b))

"""
Rozwiązanie zadania 7
"""

# funkcja
def tymin_to_uracil():
    with open('sekwencje', 'r') as f:
        lines = f.readlines()
        seq = ""
        c = 0
        for l in lines:
            if l[0] == ">":
                seq += l
                continue
            seq += l.replace('T', 'U')
            c += 1

    with open('sekwencje2', 'w') as f:
        f.write(seq)

    return c

# test
print(tymin_to_uracil())