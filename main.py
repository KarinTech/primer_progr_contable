x=input("ingrese ACTIVOS")
y=input("ingrese PASIVOS")

def bal(x,y):
    x=int(input("ingrese ACTIVOS"))
    y=int(input("ingrese PASIVOS"))
    if x>y:
        print('Vamos bien.')
    elif y==x:
        print('Hay que mejorar.')
    elif x<y:
        print('alerta roja')
    else:
        print('nada a declarar') 
  
bal(x,y) 






