# LISTAS | ARRAYS | VECTORES | MATRICES

listas = list()
listas2 = [22, True, "una lista", [1, 2]]
print(str(type(listas)) + " <==ambos son una LISTAS==> " + str(type(listas2)))

# FUNCIONAMIENTO DE LAS LISTAS --------------------------------------------
print(listas2[0])  # trae el valor 22
print(listas2[-1])  # trae el valor [1,2]
print(listas2[0:2])  # trae un rango de valores de la lista [22, True]


listas2[3] = "ACTULIZAR"  # Modificar un valor de un array | lista


listas2.append(22)  # Añadir valores a la lista con el metodo de APPEND()
print(listas2)

print(listas2.count(22))  # Nos devuelve el numero de elemento repetidos

print(
    listas2.index(True)
)  # Nos devuleve el indice en el primer que elemento que encuentre con el valor que buscamos

print(listas2.remove(22))
