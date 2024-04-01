###############################################################################
#######################  Class 5: Lineal Regression  ###########################
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
plt.figure(figsize=(7,5))
dataset["Time"].hist()
plt.show()
