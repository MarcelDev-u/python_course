import math

# zad1
print("zad1")
print(4 * 5 - (8 / 2) +5**3)

# zad2
print("zad2")
sqrt2_exact = math.sqrt(2)
sqrt2_approx = round(sqrt2_exact, 3)
relative_error = abs(sqrt2_exact - sqrt2_approx) / sqrt2_exact
print(f"{relative_error:.6f}")

# zad3
print("zad3")
m = 70
h = 1.72
bmi = m / h**2
print(bmi)

# zad4
print("zad4")
seq = "AGGTCTCAGGCGCTATCA"
seq_rna = seq.replace("T", "U")
print(seq_rna)

# zad5
print("zad5")
x = 2
print(x**7+8*x+1 > x**8-3*x**2)

# zad6
print("zad6")
A={1,2,3,4}
B={3,4,5}
C=A & B
print(C)

# zad7
print("zad7")
l1 =['ATGCGCG', 'TCCCGAG', 'TACCTAGTTT']
l2 = [seq.count('T') for seq in l1]
print(l2)