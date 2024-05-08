# SET | CONJUNTO

set1 = {1, 2, 3, 5, 5, "hola", "hola"}
set2 = set()
print(str(type(set1)) + " <==ambos son SET==> " + str(type(set2)))


# FUNCIONAMIENTO DE LOS SET'S / CONJUNTOS --------------------------------------------

print(set1)  # {1, 2, 3, 5, 'hola'} elimina los elementos repetidos


set1.add(98)  # añadir elementos con el meotodo Add()
print(set1)  #  {1, 2, 3, 98, 5, 'hola'}


set1.remove(5)  # eliminar elementos con el meotodo remove()
print(set1)  # {1, 2, 3, 98, 'hola'}


# EJEMPLO  ------------------------------------------------------

conjunto = {5, 6, 7}
conjunto2 = {7, 9, 10}
conjunto3 = {5, 7, 6}
print(conjunto, conjunto2, conjunto3)

print(conjunto.intersection(conjunto2))  # elementos que aparecen en ambos conjuntos
print(
    conjunto & conjunto2
)  # esto es lo mismo que como si estuvieramos utilizando el metodo intersection()


print(
    conjunto3.issubset(conjunto)
)  # Comprobar si los elementos de un conjunto estan incluidos en otro
print(conjunto3.issubset(conjunto2))
