'''
 * Reto #1
 * ¿ES UN ANAGRAMA?
 * Fecha publicación enunciado: 03/01/22
 * Fecha publicación resolución: 10/01/22
 * Dificultad: MEDIA
 *
 * Enunciado: Escribe una función que reciba dos palabras (String) y
 * retorne verdadero o falso (Boolean) según sean o no anagramas.
 * Un Anagrama consiste en formar una palabra reordenando TODAS
 * las letras de otra palabra inicial.
 * NO hace falta comprobar que ambas palabras existan.
 * Dos palabras exactamente iguales no son anagrama.
 *
 * Información adicional:
 * - Usa el canal de nuestro discord (https://mouredev.com/discord) "🔁reto-semanal" para preguntas, dudas o prestar ayuda a la acomunidad.
 * - Puedes hacer un Fork del repo y una Pull Request al repo original para que veamos tu solución aportada.
 * - Revisaré el ejercicio en directo desde Twitch el lunes siguiente al de su publicación.
 * - Subiré una posible solución al ejercicio el lunes siguiente al de su publicación.
 *
'''

# 10:18
# 10:44
# 26 min

from timeit import default_timer

def es_anagrama(palabra1, palabra2):
    if len(palabra1) == len(palabra2):
        if palabra1 != palabra2:
            for c in palabra1:
                i = palabra2.find(c)
                if i == -1:
                    return False
                palabra2.replace(c,"",1)
            return True
        else:
            return False
    else:
        return False

inicio = default_timer()
print(es_anagrama("hola","hola"))
print(es_anagrama("holas","hola"))
print(es_anagrama("hola","olah"))
print(es_anagrama("hola","olas"))
print(es_anagrama("amor","roma"))
fin = default_timer()
print("es_anagrama", fin - inicio,"\n")

def es_anagrama2(palabra1, palabra2):
    if len(palabra1) == len(palabra2):
        if palabra1 != palabra2:
            return sorted(palabra1.lower()) == sorted(palabra2.lower())
        else:
            return False
    else:
        return False

inicio = default_timer()
print(es_anagrama2("hola","hola"))
print(es_anagrama2("holas","hola"))
print(es_anagrama2("hola","olah"))
print(es_anagrama2("hola","olas"))
print(es_anagrama2("amor","roma"))
fin = default_timer()
print("es_anagrama2", fin - inicio,"\n")