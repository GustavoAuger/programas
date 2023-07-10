opCierre=""
while(opCierre!="S"):
    i=1
    j=1
    subtotal=0
    total=0
    detalle=""
    descuentoACUM=0
    try:
        p= int(input("ingrese la cantidad de producto "))
        n= int(input("ingrese cada cuantos productos se aplicar descuento: "))
        veces=p//n # Para determinar las veces efectivas que se debe aplicar el descuento
        op=input("Si el medio de pago es con tarjeta Raw Input presione la tecla 'S', de lo contrario presione cualquier tecla ").upper()
        if(op=="S"):
            descuento=0.2
        else:
            descuento=0
        while(i<=p):
            producto= int(input(f"ingrese producto número {i}: "))
            if(j<=veces):
                productoDESC= producto*descuento
                productoDESC= round(productoDESC)
            else:
                productoDESC= 0
            descuentoACUM= descuentoACUM+productoDESC
            productoSTR= str(producto)
            detalle=detalle+f"Precio producto {i}: "+productoSTR+"\n "
            subtotal=producto+subtotal
            total=subtotal-descuentoACUM
            if(i%n==0):
                descuento=descuento/2
                j=1+j
            i=1+i
        print("-------------------------\n")
        print(" n:",n,"\n Cantidad de productos:",p,"\n",detalle,"Total: ",subtotal,"\n  Descuento:",descuentoACUM,"\n  Por pagar: ",total)
        print("\n-------------------------")
        opCierre=input("Para cerrar caja presione la tecla 'S', de lo contrario presione cualquier tecla: ").upper()
    except:
        print("Error, vuelva a intentar")