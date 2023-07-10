i=1
inversion = int(input("ingrese inversion inicial "))
tasa= int(input("ingrese tasa de descuento mensual "))
VAN = -1*inversion
print("inversión inicial: ",inversion,"\n % tasa de descuento: ",tasa)
while(True):
    if VAN>0:
        break
    else:
        flujo= int(input(f"Flujo el mes {i}: "))
        VAN=VAN+flujo/(1+tasa*0.01)**i
        i=1+i
        VAN=round(VAN)
        print("VAN: ",VAN)
if VAN>0:
    print("El proyecto es rentable")
else:
    print("El proyecto no es rentable")