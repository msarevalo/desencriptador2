import numpy as np

#file='encrip.txt'
file=open('Encriptado.txt', 'r')

archivo = file.read()

abc = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "_"]

base =  614656
desa = int(input("\nIngresa el valor encontrado para a-1: "))
desb = int(input("\nIngresa el valor encontrado para b: "))
acumulado = 0
valor = 0
encriptado = ""
primeraLinea =""

for z in range(0, len(archivo)-1, 1):
    primeraLinea = primeraLinea + archivo[z]
primeraLinea = primeraLinea.replace(" ", "_")
print(primeraLinea)

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
#       e = 0
#        e = acumulado - 601367
#       e = e * 376919
#        e = e % base
        e = 0
        e = acumulado - desb
        e = e * desa
        e = e % base

        #print(e)

        letra1 = (int)(e / 28**3)
        letra2 = (int)((e % 28**3) / 28**2)
        letra3 = (int)(((e % 28**3) % 28**2) / 28**1)
        letra4 = (int)(e % 28)

        encriptado = encriptado + abc[letra1] + "" + abc[letra2] + "" + abc[letra3] + "" + abc[letra4]
        encriptado = encriptado.replace("_", " ")

f = open('desncriptado1.txt', 'w')
f.write(encriptado)
f.close