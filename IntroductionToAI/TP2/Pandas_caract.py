###############################################################################
#######################  Class 5: Lineal Regression  ##########################
###############################################################################
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

''' Ex. of Regression
    ·················
    Se quiere determinar la relación entre la concentración de cierto fármaco en
    el torrente sanguíneo y el tiempo transcurrido desde que se administró el 
    fármaco. Se recopila datos sobre la concentración de la droga en el torrente
    sanguíneo en diferentes intervalos de tiempo después de la administración.
'''

dataset = pd.read_csv("datases/drugs.csv")
dataset.head(10) #->Mostramos los cabeceros de 10 filas

dataset.describe()  #->Tenemos las caracteristicas principales y los cuartiles.

# Panda nos dá algunas herramientas de graficado
#################################################
#(1)
plt.figure(figsize=(7,5))
dataset["Time"].hist()
plt.show()

#(2) Podemos ver cuál es la relación entre ambas variables....
plt.figure(figsize=(7, 5))
correlacion_drug = np.corrcoef(dataset["Time"], dataset["Concentration"])
sns.heatmap(data=correlacion_drug, annot=True, annot_kws={"size": 16})
plt.show()

#(3) Graficamos el dataset
plt.figure(figsize=(7,5))
plt.scatter(dataset['Time'],dataset['Concentration'], color='r', makker='x', s=60)
plt.grid(True,linewidth=0.5)
plt.xlabel('Timepo[h]',fontsize=14)
plt.ylabel('concentration [mg/L]',fontsize=14)
plt.tick_params(axis='x',labelsize=12)
plt.tick_params(axis='y',labelsize=12)
plt.title('Dataset de concentración de droga vs tiempo',fontsize=16)
plt.show()
'''
    Ya tenemos los datos y de hecho vemos que hay una relación lineal entre las
    dos variables, por lo tanto, asumimos que podemos usar REGRSIÖN LINEAL SIMPLE
                                                           ----------------------
    
    El siguiente paso es armar el modelo, para ello vamos a utilizar el preceso
    que vimo de Macjine Learning. '''
                                                       