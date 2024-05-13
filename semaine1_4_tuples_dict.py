#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  5 08:35:15 2024

@author: jean-baptisterenaux
"""

# les tuples ressemblent à des listes mais ils sont non-mutables.
point = (10,20)
print(point, type(point))
print(point[0])

# un tuple peut être dépilé
x, y = point
print("x = %s" %x)
print("y = %s" %y)

# un tuple est non mutable donc ce code lève une exception :
# point[0] = 5

# les dictionnaires (similaire à des Map en Java)
# attention un dictionnaire n'est pas trié / sorted
params = {"param1" : 1.0,
          "param2": 2.0,
          "param3": 3.0}
print(params)
# cette syntaxe est également possible :
params = dict(param1=1.0, param2=2.0, param3=3.0)
print(type(params))
print(params)

# accès aux éléments d'un dictionnaire (un diction)
print("param2 = %s" % params["param2"])

params["param1"] = "A"
params["param2"] = "B"
params["param4"] = "D"

print("param1 = %s" % params["param1"]) 

# suppression d'une clé
del params["param4"]
print(params)

# test la présence d'une clé dans un dictionnaire
print("Est-ce que param2 est présent dans le dictionnaire ? ", "param2" in params)
print("Est-ce que param6 est présent dans le dictionnaire ? ", "param6" in params)