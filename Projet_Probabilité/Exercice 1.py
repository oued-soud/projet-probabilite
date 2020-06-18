# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 23:02:23 2020

@author: YODA ISMAEL
"""

import numpy as np
import matplotlib.pyplot as plt

# 1. Tirons les realisations des n variables suivant une loi uniforme [0,10]
yi= np.random.uniform(0,10,5)
yi

# 2. Realisation empirique de la moyenne
moyenne_yi=np.sum(yi)/5
moyenne_yi

# 3. Repetons 5000 fois les réalisations 1 et 2
N=5 # Nombre de tirage pour obtenir l'échantillon
M=5000 #Nombre de répetition
i=np.random.uniform(0,10,(N,M)) # Tirage de 5000 échantillons de taille 5 suivant une loi uniforme
i
moyenneEmp_i=np.sum(i,axis=0)*(1/N) #calcule pour chaque tirage m la moyenne empirique
moyenneEmp_i

#  4.Construisons les histogrammes des 5000 réalisations de la variable Y(barre)
plt.hist(moyenneEmp_i)
 
   
# 5.Répetons l'expérience pour les tailles d'échantillons suivantes:
    
                 ############### n=10 ####################
    
N=10 # Nombre de tirage pour obtenir l'échantillon
M=5000 #Nombre de répetition
i=np.random.uniform(0,10,(N,M)) # Tirage de 5000 échantillons de taille 5 suivant une loi uniforme
i
moyenneEmp_i=np.sum(i,axis=0)*(1/N) #calcule pour chaque tirage m la moyenne empirique
moyenneEmp_i
plt.hist(moyenneEmp_i) # histogramme des 5000 réalisations de la moyenne empirique


    
                ############### n=100 ####################
                
N=100 # Nombre de tirage pour obtenir l'échantillon
M=5000 #Nombre de répetition
i=np.random.uniform(0,10,(N,M)) # Tirage de 5000 échantillons de taille 5 suivant une loi uniforme
i
moyenneEmp_i=np.sum(i,axis=0)*(1/N) #calcule pour chaque tirage m la moyenne empirique
moyenneEmp_i
plt.hist(moyenneEmp_i) # histogramme des 5000 réalisations de la moyenne empirique


                ############### n=1000 ####################
                
N=1000 # Nombre de tirage pour obtenir l'échantillon
M=5000 #Nombre de répetition
i=np.random.uniform(0,10,(N,M)) # Tirage de 5000 échantillons de taille 5 suivant une loi uniforme
i
moyenneEmp_i=np.sum(i,axis=0)*(1/N) #calcule pour chaque tirage m la moyenne empirique
moyenneEmp_i
plt.hist(moyenneEmp_i) # histogramme des 5000 réalisations de la moyenne empirique
    

              ############### n=10000 ####################
                
N=10000 # Nombre de tirage pour obtenir l'échantillon
M=5000 #Nombre de répetition
i=np.random.uniform(0,10,(N,M)) # Tirage de 5000 échantillons de taille 5 suivant une loi uniforme
i
moyenneEmp_i=np.sum(i,axis=0)*(1/N) #calcule pour chaque tirage m la moyenne empirique
moyenneEmp_i
plt.hist(moyenneEmp_i) # histogramme des 5000 réalisations de la moyenne empirique


    
# 6. Tracer les histogrammes des 10000 réalisations de la moyenne empirique
#     obtenues pour les quatre valeurs de n

               ############### n=10 ####################
    
N=10 # Nombre de tirage pour obtenir l'échantillon
M=10000 #Nombre de répetition
i=np.random.uniform(0,10,(N,M)) # Tirage de 5000 échantillons de taille 5 suivant une loi uniforme
i
moyenneEmp_i=np.sum(i,axis=0)*(1/N) #calcule pour chaque tirage m la moyenne empirique
moyenneEmp_i
plt.hist(moyenneEmp_i) # histogramme des 5000 réalisations de la moyenne empirique


    
                ############### n=100 ####################
                
N=100 # Nombre de tirage pour obtenir l'échantillon
M=10000 #Nombre de répetition
i=np.random.uniform(0,10,(N,M)) # Tirage de 5000 échantillons de taille 5 suivant une loi uniforme
i
moyenneEmp_i=np.sum(i,axis=0)*(1/N) #calcule pour chaque tirage m la moyenne empirique
moyenneEmp_i
plt.hist(moyenneEmp_i) # histogramme des 5000 réalisations de la moyenne empirique


                ############### n=1000 ####################
                
N=1000 # Nombre de tirage pour obtenir l'échantillon
M=10000 #Nombre de répetition
i=np.random.uniform(0,10,(N,M)) # Tirage de 5000 échantillons de taille 5 suivant une loi uniforme
i
moyenneEmp_i=np.sum(i,axis=0)*(1/N) #calcule pour chaque tirage m la moyenne empirique
moyenneEmp_i
plt.hist(moyenneEmp_i) # histogramme des 5000 réalisations de la moyenne empirique
    

              ############### n=10000 ####################
                
N=10000 # Nombre de tirage pour obtenir l'échantillon
M=10000 #Nombre de répetition
i=np.random.uniform(0,10,(N,M)) # Tirage de 5000 échantillons de taille 5 suivant une loi uniforme
i
moyenneEmp_i=np.sum(i,axis=0)*(1/N) #calcule pour chaque tirage m la moyenne empirique
moyenneEmp_i
plt.hist(moyenneEmp_i) # histogramme des 5000 réalisations de la moyenne empirique


#### On remarque que plus on augmente la taille de l'échantillon et plus on augmente le nombre
# d'échantillon, alors on obtient une distribution de plus en plus proche de la loi normale.

