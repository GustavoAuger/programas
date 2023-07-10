while(True):
    i=1
    j=0
    TOTAL=0
    detalle=""
    t=9
    try:
        C= int(input("ingrese la capacidad de la batería: "))
        V= int(input("ingrese el voltaje de la batería: "))
        H= int(input("ingrese base de tiempo indicada por el fabricante: "))
        while(8<=t):
            A= int(input(f"ingrese la potencia de la ampolleta número {i}: "))
            TOTAL=TOTAL+A
            I=TOTAL/V
            t=H/(((I*H)/C)**1.15) #Según el ejercicio la constante de Peukert es 1.15. Sin embargo, me percate que en el ejemplo del ejercicio se consideró 1.05 (por eso me dan valores distintos de autonomía al tomar los valores ejemplo).
            STR_A=str(A)
            STR_TOTAL=str(TOTAL)
            STR_t=str(t)
            if(8<=t):
                detalle=detalle+f"Potencia ampolleta {i} (Watt): "+STR_A+"\nAutonomía: "+STR_t+"[Horas]. "+f"Ampolletas {i}. "+"Potencia Total: "+STR_TOTAL+" [Watt]\n"
                i=i+1
                j=j+1
        print("-------------------------\n")
        print("Capacidad de la batería (AH): ",C,"\nVoltaje de la batería (Volt): ",V,"\nBase de tiempo (Horas):",H)
        print(detalle, end="")
        print(f"Potencia ampolleta {i} (Watt):",A)
        print("\nTotal ampolletas: ",j)
        print("-------------------------")
        break
    except:
        print("Error, vuelva a intentar")