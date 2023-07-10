while(True):
    i=1
    a=0
    r=0
    e=0
    A=0
    R=0
    B=0
    N=0
    Voto=""
    detalle=""
    try:
        n= int(input("ingrese la cantidad de universidades: "))
        while(i<=n):
            universidad=str(input("ingrese nombre de la univeridad: "))
            detalle=detalle+"\n"+"Universidad: "+universidad
            while(Voto!="X"):
                Voto=input("ingrese el voto: ").upper()
                while(Voto!="A"and Voto!="R" and Voto!="B" and Voto!="N" and Voto!="X"):
                    print("Error, entrada invalida, intente nuevamente")
                    Voto=input("ingrese el voto: ").upper()
                else:
                    if Voto=="A":
                        A=A+1
                    elif Voto=="R":
                        R=R+1
                    elif Voto=="B":
                        B=B+1
                    elif Voto=="B":
                        N=N+1
                    detalle=detalle+"\n Voto:"+Voto
                    A_STR=str(A)
                    B_STR=str(B)
                    R_STR=str(R)
                    N_STR=str(N)
            if(A>R):
                a=a+1
            elif(A<R):
                r=r+1
            elif(A==R):
                e=e+1
            A=0
            B=0
            R=0
            N=0
            detalle=detalle+"\n"+universidad+": "+A_STR+" aceptan, "+R_STR+" rechazan, "+B_STR+" blanco, "+N_STR+" nulos."+"\n"
            Voto=""
            i=i+1
        print("-------------------------\n")
        print("Número de universidaddes: ",n)
        print(detalle)
        print("Universidades que aceptan: ",a,"\nUniversidades que rechazan:",r,"\nUniversidades con empate: ",e)
        print("-------------------------")
        break
    except:
        print("Error, vuelva a intentar")