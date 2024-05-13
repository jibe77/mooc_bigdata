#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  5 09:06:43 2024

@author: jean-baptisterenaux
"""

# conditions
condition1 = False
condition2 = False
if condition1:
    print("condition1 est vrai")
elif condition2:
    print("condition2 est vrai")
else:
    print("aucune condition n'est vraie.")
    
condition1 = condition2 = True
if condition1:
    if condition2:
        print("les conditions sont vraies")

# attention à bien respecter l'identation !

# les boucles
for x in [1,2,3]:
    print(x)

for x in range(4):
    print(x)
    
for word in ["big", "data", "en", "python"]:
    print(word)
    
for c in "calcul":
    print(c)
    
# enumeration permet de connaitre l'index et la valeur
s = "calcul"
for idx, c in enumerate(s):
    print(idx, c)
    
# pour itérer sur un dictionnaire
params = {"param1":3.0,
          "param2":"B",
          "param3":"A"}
for key, value in params.items():
    print("%s = %s" % (key, value))

# si on itère directement sur le dictionnaire, on récupère les clés.    
for key in params:
    print(key)
    
# syntaxe "list comprehension" permettant la création d'une liste avec for
l = [x ** 2 for x in range(0,5)]
print("liste l produite avec la syntaxe 'list comprehension':", l)

# c'est la version plus courte de cette syntaxe : 
l = list()
for x in range(0,5):
    l.append(x**2)
print("liste l produite avec la syntaxe longue:", l)  

# utilisation de la boucle while
i = 0
while i < 5:
    print(i)
    i = i + 1
    
print("OK")
    