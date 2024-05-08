
def calcularIVA(p): 
     IVA =  p * 0.19
     return IVA 




precioCompra =  float(input("ïngrese el precio de su compra: "))
IVA = calcularIVA(precioCompra)
print(f"el precio de la compra sin IVA  es de : {precioCompra}\nprecio con IVA es de: {precioCompra+IVA}")
