#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  5 16:23:28 2024

@author: jean-baptisterenaux
"""

class Point(object):
    """
    Classe pour représenter un point
    """
    def __init__(self, x, y):
        """
        Création d'un nouveau point en position x et y
        """
        self.x = x
        self.y = y
        
    def translate(self, dx, dy):
        """
        Translate le point de dx et dy
        """
        self.x += dx
        self.y += dy
        
    def __str__(self):
        return "Point: [%f, %f]" % (self.x, self.y)
    
p = Point(x=0, y=0)
print(p.x)
print(p.y)
print("%s" % p)

p = Point(1,1)
p.translate(0.25, 1.5)
print(p)

# les exceptions
def ma_fonction(arg):
    if not isinstance(arg, list):
        raise Exception("arg doit être de type list")
    print("tout s'est bien passé:",arg)
ma_fonction([1,2])

# ma_fonction(1)
# 
#  File ~/Documents/Developer/mooc_bigdata/semaine1_7_classes_objets.py:42 in ma_fonction
#    raise Exception("arg doit être de type list")
#
#   Exception: arg doit être de type list

# pour gérer une exception, on utilise le mot clé "except"
try:
    ma_fonction(1)
    print('OK')
except:
    print("Exception interceptée !")
    
# pour obtenir des informations sur l'exception, on peut utiliser cette syntaxe
try:
    print(var)
except Exception as e:
    print("Exception interceptée : %s" % e)