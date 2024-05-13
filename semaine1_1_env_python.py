#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  4 18:29:13 2024

@author: jean-baptisterenaux
"""

# ceci est un commentaire

# ceci lance une commande Unix affichant la liste des fichier à la racine
# du système de fichier
!ls /

# affichage le contenu du fichier
!cat semaine1_1_env_python.py

# affiche un message
print("bonjour tout le monde !")

# affiche un entier
print (5)

# les nombres
print (2+1)
print (3*4)

# calcul de puissance, ici 2 à la puissance 3
print (2**3)

# la fonction type permet de savoir de quel type est une variable,  ici <class 'int'>
a = 3
print(type(a))

c = 2.1
print(type(c))

# un nombre complexe est une expression mathématique qui combine une partie 
# réelle et une partie imaginaire.
a = 1.5 + 1j
print(a.real)
print(a.imag)
print(type(a))

print (2 > 1)
print (type(2>1))

# les nombres et changements de type
print(7*3.) # int * float produit un float
print(type(7*3.))

print(3/2) # int / int -> int en python 2, mais float en python 3
print(3/2.) # int / float -> float
a = 2
print(3/float(2))
# division entière
print(3//2)