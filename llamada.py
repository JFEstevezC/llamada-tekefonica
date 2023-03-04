print("----------------------------------")
print("------- LLAMADA TELEFÓNICA -------")
print("----------------------------------")
print("")

m = int(input("Escriba cuántos minutos duró la llamada: "))

if m <= 3:
    precio = 300
else: 
    precio = 300 + ((m-3)*50)

print("-----------------------------------")
print("------- COSTO DE LA LLAMADA -------")
print("-----------------------------------")
print("")
print("El valor total a pagar es de: ")
print("$", str(precio))
print("")
