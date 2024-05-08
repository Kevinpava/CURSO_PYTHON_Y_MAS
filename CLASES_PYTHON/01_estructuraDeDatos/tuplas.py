# TUPLAS

tuplas = (1, 2, 3, 3)
tuplas2 = tuple()
print(str(type(tuplas)) + " <==ambos son una TUPLAS==> " + str(type(tuplas2)))


# FUNCIONAMIENTO DE LAS TUPLAS --------------------------------------------


print(tuplas.count(2))  # Nos devuelve el numero de elemento repetidos

print(
    tuplas.index(2)
)  # Nos devuleve el indice en el primer que elemento que encuentre con el valor que buscamos
