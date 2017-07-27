import numpy as np
import matplotlib.pyplot as plt


class carga:
    'Cuadrupolo electrico conformado por cuatro cargas'
    
#Defino mis condiciones usando clases y objetos para inicializar y solucionar el problema  
    def __init__(self, x0, y0, q0):
        #e = 1.602176*10**(-19) #Tengo en cuenta las unidades
        self.x=x0
        self.y=y0
        self.q=q0
        
#Funcion para el potencial
    def dar_potencial(self, xa, ya):  
        k = 0.2306 #((kg/s**2)(nm**3)(C**2))
        xa = (xa+0.01)
        ya = (ya+0.01)
        
#R es la distancia entre la carga y el punto donde medimos el potencial
        R = (((xa-self.x)**2.0)+((ya-self.y)**2.0))**1/2
        return (k*self.q/R)
      
#Defino la matriz del potencial. Area: cuadrado de lado 2 nm
    def dar_matriz_pot(self, divisiones):
        #Creo la matriz
        global delta
        delta= 2.0/divisiones
        potencial = np.zeros((divisiones, divisiones))
        #Recorro la matriz
        for i in range (divisiones):
            for j in range(divisiones):
                potencial [i, j] = self.dar_potencial((delta*(i-divisiones/2.)), (delta*(j-divisiones/2.)))
        return (potencial) 

#Agrego cada carga en cargas    
cargas = []
cargas.append(carga((0.5),(0.5), 1))
cargas.append(carga((-0.5),(-0.5),1))
cargas.append(carga((-0.5),(0.5), -1))
cargas.append(carga((0.5), (-0.5), -1))
#print cargas[0].x deme x de la posicion 1
#print cargas[3].dar_potencial(2,2)

#Obtengo el potencial total sumando las matrices de cada carga 
potencial_total=(cargas[0].dar_matriz_pot(100)+cargas[1].dar_matriz_pot(100)+cargas[2].dar_matriz_pot(100)+cargas[3].dar_matriz_pot(100))
#print potencial_total

#Monito
fig,axes = plt.subplots(1)
plt.setp(axes,xticks=[0,25,50,75,99],xticklabels=[-1.00,-0.50,0.00,0.50,1.00],yticks=[0,25,50,75,99],yticklabels=[1.00,0.50,0.00,-0.50,-1.00])
plt.title('Potencial electrico/Campo electrico')
plt.xlabel('$x$(nm)')
plt.ylabel('$y$(nm)')
plt.imshow(potencial_total, extent=(-1,1,-1,1))
cbar = plt.colorbar()
cbar.ax.set_ylabel(r'[$\frac{kg nm^2}{s^2 e}$]',rotation=0)
plt.savefig('cargas.pdf')
       

#Para determinar el campo electrico 

campox =-(np.roll(potencial_total,1,axis=1)-np.roll(potencial_total, -1, axis=1))/2*delta
campoy =-(np.roll(potencial_total,1,axis=0)-np.roll(potencial_total, -1, axis=0))/2*delta

x,y=np.meshgrid(np.linspace(-1,1,100),np.linspace(-1,1,100))
plt.streamplot(x,y,campox,campoy)
plt.imshow(potencial_total)
plt.ylim(-1,1)
plt.xlim(-1,1)
#Grafica: usar vectores o lineas de campo 
plt.savefig('cargas.pdf') 
