'''
Reto #0
EL FAMOSO FIZZ BUZZ
Dificultad: Fácil
Enunciado: Escribe un programa que muestre por consola en un print los números
del 1 al 100 (ambos incluidos y con un salto de línea entre cada impresión),
sustituyendo los siguientes:
- Múltiplos de 3 por la palabra "fizz".
- Múltiplos de 5 por la palabra "buzz".
- Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
'''

from timeit import default_timer

# 12:44:30
# 12:51:00
# 7 min
inicio = default_timer()
for i in range(1, 101):
    if i % 3 == 0:
        if i % 5 == 0:
            print("fizzbuzz")
        else:
            print("fizz")
    elif i % 5 == 0:
        print("buzz")
    else:
        print(i)
fin = default_timer()
print("if-else", fin - inicio,"\n")

# 1:00
# 1:17
'''
Proceso para poder hacer álgebra de bool
inicio = default_timer()
for i in range(1, 101):
    tres = not(i % 3)
    tresn = not(tres)
    cinco = not(i % 5)
    cincon = not(cinco)
    #print ("tres =", tres, "tresn =", tresn, "cinco =", cinco, "cincon =", cincon)
    i2 = tresn and cincon
    f = tres and cincon
    b = tresn and cinco
    fb = tres and cinco
    print(str(i) * i2, "fizz" * f, "buzz" * b, "fizzbuzz" * fb)
fin = default_timer()
print("bool", fin - inicio,"\n")
'''

# 1:17
# 1:45
inicio = default_timer()
for i in range(1,101):
    tupla0 = (i, "fizz", "buzz", "fizzbuzz")
    tupla1 = (not(i % 3), not(not(i % 3)), not(i % 5), not(not(i % 5)))
    # j = 0*(tupla1[1] and tupla1[3]) + 1*(tupla1[0] and tupla1[3]) + 2*(tupla1[1] and tupla1[2]) + 3*(tupla1[0] and tupla1[2])
    j = 1*(tupla1[0] and tupla1[3]) + 2*(tupla1[1] and tupla1[2]) + 3*(tupla1[0] and tupla1[2])
    print(tupla0[j])
fin = default_timer()
print("tupla", fin - inicio,"\n")

