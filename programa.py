# Programa que lea 20 numeros enteros y imprima cuantos son pares y cuantos son impares

print("-------------------------------------------")
print("-------------BIENVENIDO--------------")
print("-------------------------------------------")

cant_par = 0
cant_imp = 0
lista_numeros = "estos: "

for i in range(1, 21):
    n = int(input("Digite el número " + str (i) + ":"))
    lista_numeros = lista_numeros + str (n) +  " "
    m = n%2
    if (m == 0):
        cant_par = cant_par + 1
    else:
        cant_imp = cant_imp + 1

# output
print()
print("Los números que usted digito fueron " + str (lista_numeros))
print("Tiene " + str (cant_par) + (" números pares"))
print("Tiene " + str (cant_imp) + (" números impares"))
