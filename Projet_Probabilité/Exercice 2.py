# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 04:56:26 2020

@author: YODA ISMAEL
"""

import numpy as np
import matplotlib.pyplot as plt


# 1. Tirons les realisations de 10 variables aléatoires suivant 
# une loi de Khi-deux à deux dégré de liberté

N=10 # Taille de l'échantillon
y= np.random.chisquare(2,N)
y

# 2. Realisation empirique de la moyenne
y_barre=np.sum(y)/N
y_barre

# 3. Considérons la variable transformée Z(n) et calculons la réalisation de cette variable

Z= np.sqrt(N)*((y_barre-2)/2)
Z


# 4. Répetons la procédure de (1 à 3) 5000 fois
                ################### Etape 1 #####################
## Tirage de 5000 échantillons de taille 10 suivant une loi du Khi-deux à 2 dégré de liberté
N=1000 # Taille de l'échantillon
M=5000 # Nombre de réplications
yn= np.random.chisquare(2,(N,M))
yn
                ################### Etape 2 #######################
# Realisation empirique des 5000 la moyenne
yn_barre=np.sum(yn,axis=0)/N
yn_barre
# Realisation des 5000 variables aléatoires transformées Z(n)
Zn= np.sqrt(N)*((yn_barre-2)/2) 
Zn        

# 5. Tracons l'histogramme de ces 5000 réalisations de la variable transformée Z
plt.hist(Zn,20)

### densité de 5000 réalisations d'une variable aléatoire suivant une loi normale
import matplotlib.pyplot as plt
import numpy as np
mu, sigma = 0, 1
s = np.random.normal(mu, sigma, 5000)
count, bins, ignored = plt.hist(s, 20, normed=True)
plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) *
    np.exp( - (bins - mu)**2 / (2 * sigma**2) ), linewidth=3, color='y')
plt.show()

#### CONCLUSION: Nous pouvons dire que l'histogramme des 5000 réalisations 
##### de la variable transformée Z est celui de la densité d'une loi normale centrée réduite



import matplotlib.pyplot as plt
import numpy as np
mu, sigma = 0,1
# Create the bins and histogram
count, bins, ignored = plt.hist(Zn, 20, normed=True)
# Plot the distribution curve
plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) *
    np.exp( - (bins - mu)**2 / (2 * sigma**2) ), linewidth=3, color='y')
plt.show()


