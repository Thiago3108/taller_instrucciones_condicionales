# programa para dar como resultado la cara inversa de un dado 

print("-------------------------------------")
print("------------CARA INVERSA-------------")
print("-------------------------------------")

# input

dado = int(input("ingrese una cara del dado: "))

# procesing

if dado == 1:
    rta=6
elif dado == 2:
    rta=4
elif dado == 3:
    rta=5
elif dado == 4:
    rta=2
elif dado == 5:
    rta=3
elif dado == 6:
    rta=1
else:
    rta= "Valor invalido"

# output
print(rta)
