
print("por favor ingrese el valor total del prestamo solicitado ")
p=float(input())
print("por favor ingrese la tasa de interes anual en % ")
r=(float(input()))/100
print("por favor ingrese los años que quiere su prestamo ")
n=int(input())
print("por favor ingrese los años que quiere su prestamo ")
pe=int(input())
i=1

while p <=0:
    c=p*(r/12)*((1+(r/pe))**(n*pe))/(((1+(r/pe))**(n*pe))-1)
    
    print("cota  ",i,"  es ",a," su saldo ",p)

print("--------------------------------------------------------------")
print("el valor prestado es            ",p)
print("la tasa de interes anual es     ",r)
print("los años del credito            ",n)
print("el numero de pagos anueles son  ",pe)
print("--------------------------------------------------------------")
print("el valor de su cuota mensual es ",a)