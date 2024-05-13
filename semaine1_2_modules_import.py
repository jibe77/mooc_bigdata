#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  4 20:31:51 2024

@author: jean-baptisterenaux
"""

# documentation officielle sur Python :
#   https://docs.python.org/3/reference/index.html
#   https://docs.python.org/3/library/

import math

x = math.cos(2*math.pi)
print(x)

# syntaxe alternative plus rapide
from math import cos, pi

x = cos(2*pi)
print(x)

# syntaxe alternative non recommandée
from math import *
print(tanh(1))

# import avec alias
import math as m
print(m.cos(1.))

# affiche le contenu d'un module
print(dir(math))

# en mode intéractif, la fonction help est très utile
help(math)
help(math.log)

# fractions
import fractions
a = fractions.Fraction(2,3)
b = fractions.Fraction(1,2)
print(a + b)
print(type(a))

# la fonction isinstance permet de vérifier le type référencé par une variable
print(isinstance(a, fractions.Fraction))

a = fractions.Fraction(1,1)
print(isinstance(a,int))

# on peut convertir de float vers int ou encore complexe ...
x = 1.5
print(x, type(x))
x = int(x)
print(x, type(x))
z = complex(x)
print(z, type(z))

# ... mais pas l'inverse car risque de perte d'information
# x = float(z)
# print(x, type(x))
# TypeError: can't convert complex to float

# opérateurs
print(True and False)

# comparaisons
print(2 > 1)
print(2 > 2)
print(2 >= 2)
print(2 == 2)
print(2 != 3)