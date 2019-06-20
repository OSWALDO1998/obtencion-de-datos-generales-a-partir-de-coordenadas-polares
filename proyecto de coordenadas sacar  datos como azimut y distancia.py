#SE IMPORTAN LAS BIBLIOTECAS QUE SE OCUPARAN PARA REALIZAR EL PROYECTO
import numpy as np
from numpy.random import rand
import csv
import math
import matplotlib.pyplot as plt

#SE DEFINE CADA COLUMNA QUE SE QUE VENDRA EN EL ARCHIVO CSV:V,X,Y(VERTICE,COORDENADAS X,Y,AL IGUAL QUE BANDERA Y CANTIDAD PARA PODER HACER OTRAS OPERACIONES 
V=[]
X=[]
Y=[]
bandera= 0
cantidad= 0

#se habre el archivo csv y saca cada uno de los datos
print('¿COMO SE LLAMA EL ARCHIVO CSV EN LA QUE VIENEN LAS COORDENADAS X,Y?')
nombre= input()
nombre=nombre+'.csv'
#LEE EL ARCHIVO Y LO MUESTRA EN LA PANTALLA
with open (nombre) as f:
    reader=csv.reader(f)
    print('LOS DATOS DENTRO DEL ARCHIVO CSV SE MOSTRARAN AL SIGUIENTE:')
    print('                                   ')
    for row in reader:
        print(row)
    print('                                   ')
    
with open (nombre) as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        V.append(float(row['V']))
        X.append(float(row['X']))
        Y.append(float(row['Y']))
#EVALUA LA FUNCION V, YA QUE NO SE OCUPARA MAS ADELANTE
while (bandera==0):
    print ('¿CUANTAS COORDENADAS DESEA QUE CALCULE LA DISTANCIA Y EL AZIMUT ?')
    print ('NOTA:recuerde que se calcula a partir de la coordenada 1 hasta n numeros. ')
    cantidad = eval(input())
    h = len(V)
    if (cantidad<=h):
#SE LE DA UNA CONDICION A LAS COORDENADAS X,Y PARA QUE PUEDA LEER LA SIGUIENTE COORDENADA COMO X2 Y A LA PRIMERA COMO X1 AL IGUAL EN LAS Y1,Y2
        for i in range (cantidad):
            if i==cantidad:
                x1=X[0]
                x2=X[i]
                y1=Y[0]
                y2=Y[i]
            else:
                x1=X[i]
                x2=X[i+1]
                y1=Y[i]
                y2=Y[i+1]
 #SE REALIZAN AQUI LOS CALCULOS DE LAS COORDENADAS Y SE IMPRIME               
            distancia = (math.sqrt((( x2- x1) **2)+(y2 - y1) **2))
            RBO1 = (math.atan((x2 - x1) / (y2 - y1)))
            RBO2= (math.degrees((RBO1)*400) / 360)
            
            print('LA DISTANCIA CALCULADO DE LA COORDENADA ES:',distancia)
            print('EL RUMBO  CALCULADO DE COORDENADA ES:',RBO2)
            print('                                           ')
            print('                                           ')
 #AQUI CUANDO ANTERIORMENTE TE PIDE LAS COORDENADAS , SÍ LE PIDES MAS COORDENADAS SE REGRESARA PARA QUE VUELVAS A INTRODUCIR DE NUEVO CUANTAS COORDENADAS SE DESEAN CALCULAR           
        bandera=1
    else:
        print("ME PIDES MAS COORDENADAS DE LAS QUE EXISTE, REPITA DE NUEVO CUANTAS SE DESEAN CALCULAR.")
        bandera=0
        
#AQUI SE PLOTEA LAS COORDENADAS QUE SE CALCULARON , EN OTRAS PALABRAS SE HACE UNA MOSTRACION GRAFICA
plt.plot(X,Y, label='poligono'),('ro')
plt.xlabel('EJES DE LAS X')
plt.ylabel('EJES DE LAS Y')
plt.title('PLANO DEL POLIGONO')
plt.legend()
plt.show()
print('SE GENERARA UN GRAFICO DE  LAS COORDENADAS CALCULADAS')

