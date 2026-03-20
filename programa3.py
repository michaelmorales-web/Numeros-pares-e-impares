# Programa en Python para leer una frase, y que indique cuántas veces está cada vocal en dicha frase.

print("----------------------------------------------------")
print("------------------------BIENVENIDO---------------------")
print("----------------------------------------------------")

a = e = i = o = u = 0
A = E = I = O = U = 0

frase = input("Digite la frase: ")

for letra in frase:
    if letra in "a":
        a = a + 1
    elif letra in "e":
        e = e + 1
    elif letra in "i":
        i = i + 1
    elif letra in "o":
        o = o + 1
    elif letra in "u":
        u = u  + 1
    elif letra in "A":
        A = A + 1
    elif letra in "E":
        E = E + 1
    elif letra in "I":
        I = I + 1
    elif letra in "O":
        O = O + 1
    elif letra in "U":
        U = U + 1

print()
print("Su oración tiene " + str (a) + " a minusculas")
print("Su oración tiene " + str (e) + " e minusculas")
print("Su oración tiene " + str (i) + " i minusculas")
print("Su oración tiene " + str (o) + " o minusculas")
print("Su oración tiene " + str (u) + " u minusculas")
print("Su oración tiene " + str (A) + " A mayusculas")
print("Su oración tiene " + str (E) + " E mayusculas")
print("Su oración tiene " + str (I) + " I mayusculas")
print("Su oración tiene " + str (O) + " O mayusculas")
print("Su oración tiene " + str (U) + " U mayusculas")
print()