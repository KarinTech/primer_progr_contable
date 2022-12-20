mercadoria = input("Enter the amount of "Mercadoria" )
                   print("Mercadoria =  ", mercadoria)
pasivos ={
"mercadoria",
"ICMS a Recuperar",
"fornecedor"

}
suma_pas=int(82000+18000+35000)

activos = {
    "caixa":50000,
    "ventas":10000,
    "flujo_capital":100000
}
suma_act=(50000+100000+10000)
for pasivo in pasivos:
    print(pasivo, pasivos[pasivo], sep="=")
   

for activo in activos:
    print(activo, activos[activo], sep="="), 


print("Total Activos = ",suma_act)
print("Total Pasivos = ",suma_pas)
balance_simple= (suma_act- suma_pas)   
print("El balance es de ", balance_simple )
