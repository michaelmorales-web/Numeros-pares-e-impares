# Programa para calcular cuantos multiplos de 7, y cuantos multiplos de 9 hay en los números comprendidos entre 1000 y 5000

print("---------------------------------------------")
print("---------------BIENVENIDO--------------------")
print("---------------------------------------------")

multiplos_7 = 0
multiplos_9 = 0
no_multiplos = 0

for i in range(1000, 5001):
    if i % 7 == 0:
        multiplos_7 = multiplos_7 + 1
    if i % 9 == 0:
        multiplos_9 = multiplos_9 + 1
    if i % 7 != 0 and i % 9 != 0:
        no_multiplos = no_multiplos + 1

print()
print("Entre el número 1000 y el núermo 5000 hay " + str (multiplos_7) + " multiplos del 7")
print("Entre el número 1000 y el número 5000 hay " + str (multiplos_9) + " multiplos del 9")
print("Entre el número 1000 y el número 5000 hay " + str (no_multiplos) + " números que no son multiplos ni de el 7 ni de el 9")
print()