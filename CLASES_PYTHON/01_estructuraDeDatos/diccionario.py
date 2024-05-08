# DICCCIONARIO

diccionario = dict()
diccionario2 = {
    "nombre": "kevin",
    "vivo": True,
    "edad": 21,
    "lenguanjes": ["python", "JS", "PHP"],
}
print(
    str(type(diccionario)) + " <==ambos son DICCIONARIO==> " + str(type(diccionario2))
)


# FUNCIONAMIENTO DE LOS  DICCIONARIOS --------------------------------------------

diccionario_ejemplo = {1: "uno", 2: "dos"}
diccionario_ejemplo[3] = "tres"  # añadir o cambiar el valor de un/a (KEY  ó CLAVE)
print(diccionario_ejemplo[1])  # UNO


print(
    diccionario_ejemplo,
    diccionario_ejemplo.keys(),
    diccionario_ejemplo.values(),
    diccionario_ejemplo.items(),
)


print(
    diccionario_ejemplo.pop(2)
)  # este metodo POP() elimina la clave/key junto a su valor del diccionario
