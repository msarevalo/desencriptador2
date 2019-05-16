import numpy as np

file='primos.txt'

primos = np.loadtxt(file, delimiter=',', skiprows=0)

abc = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "_"]

base =  614656
acumulado = 0
valor = 0
encriptado = ""

primeraLinea = "kzzwdyy ñkbs uyawekwtblwhñyaeinañeuwdvya"

primeraLinea = primeraLinea.replace(" ", "_")

continua=1

while continua==1:
    for z in range(len(primos)-1, 0, -1):
        for aa in range((int)(base/2), (int)(base), 1):
            encriptado=""
            if aa%1000 == 0:
                print(aa)
            if z%1000 == 0:
                print(primos[z], " ", aa)
            menosa = (int)(primos[z])
            b = aa
            for x in range(0, len(primeraLinea), 4):
                palabra = ""
                palabra = palabra + primeraLinea[x]
                palabra = palabra + primeraLinea[x+1]
                palabra = palabra + primeraLinea[x+2]
                palabra = palabra + primeraLinea[x+3]

                acumulado = 0

                for y in range(0, len(palabra)):
                    if y==0:
                        valor = (int)(abc.index(palabra[y])*(28**3))
                    if y==1:
                        valor = (int)(abc.index(palabra[y])*(28**2))
                    if y==2:
                        valor = (int)(abc.index(palabra[y])*(28**1))
                    if y==3:
                        valor = (int)(abc.index(palabra[y])*(28**0))

                    acumulado = acumulado + valor
                #print(acumulado)
#                b= 601367
#                menosa=376919
#                e = 0
#                e = acumulado - 601367
#                e = e * 376919
#                e = e % base
                e = 0
                e = acumulado - b
                e = e * b
                e = e % base

                #print(e)

                letra1 = (int)(e / 28**3)
                letra2 = (int)((e % 28**3) / 28**2)
                letra3 = (int)(((e % 28**3) % 28**2) / 28**1)
                letra4 = (int)(e % 28)

                encriptado = encriptado + abc[letra1] + "" + abc[letra2] + "" + abc[letra3] + "" + abc[letra4]
                encriptado = encriptado.replace("_", " ")

                if encriptado.find("teoria")>=0:
                    print(encriptado)
                    conti = int(input("\nSi te sirve la desencripcion: "))
                    if(conti==1):
                        continua=0
                        print("Las claves son a-1: ", menosa, " y b ", b, " texto final: ")
                        print(encriptado)
                        break
                        break
                        break
