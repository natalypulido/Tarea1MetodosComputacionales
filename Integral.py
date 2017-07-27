import numpy as np
import matplotlib.pyplot as plt

#Defino funcion 10D
def mi_funcion(x1,x2,x3,x4,x5,x6,x7,x8,x9,x10):
    return (x1+x2+x3+x4+x5+x6+x7+x8+x9+x10)**3

#Defino mi funcion mi_integral
def mi_integral(n):
    
    x1=np.random.rand(n)*2
    x2=np.random.rand(n)*2
    x3=np.random.rand(n)*2
    x4=np.random.rand(n)*2
    x5=np.random.rand(n)*2
    x6=np.random.rand(n)*2
    x7=np.random.rand(n)*2
    x8=np.random.rand(n)*2
    x9=np.random.rand(n)*2
    x10=np.random.rand(n)*2
    y=np.random.rand(n)*(20)**3    
    
#Area total es igual a base*10 ya que estoy en 10D por la altura    
    area_total=((2**10)*((20)**3))
    
#Iniciare mi contador en 0    
    contador=0.0
    for i in range (n):
        valor_funcion=mi_funcion(x1[i],x2[i],x3[i],x4[i],x5[i],x6[i],x7[i],x8[i],x9[i],x10[i])
        valor_aleatorio=y[i]
        if (valor_aleatorio<valor_funcion):
            contador+=1
    #print contador
    
#area_total=n & area_bajo_funcion=contador y mi area total seria el area bajo la curva que es igual a mi integral
    integral=(contador*area_total)/n
    return(integral) 
#print mi_integral(10000)

#Repetir el metodo 20 veces y sacar el promedio de esas 20
def promedio_int(n):
    valores = []
    for i in range(20):
        valores.append((mi_integral(n)))
    val = np.mean(valores)   
    return val

#Variando el numero de puntos n. Donde n=2,4,8,...,8192
puntos = []
respuesta = []
for i in range(1,14):
    respuesta.append((promedio_int(2**i)))
    n_p=2**i    
    puntos.append(n_p)
#print respuesta

#Convierto mi lista en un array para poder determinar el valor del error 
valor_integral = np.asarray(respuesta)
#print valor_integral

plt.plot(puntos, respuesta)
plt.title('Integral Monte-Carlo')
plt.savefig('num_integral.pdf')
plt.close()

#Para la estimacion del error 
analitico=1126400
error=abs(analitico-valor_integral)/analitico
#print error 

plt.title('Error')
ejex=(1/np.sqrt(puntos))
ejey=error
plt.scatter(ejex, error)
plt.savefig('err_integral.pdf')
