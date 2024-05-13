#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  5 15:47:57 2024

@author: jean-baptisterenaux
"""

# les fonctions
# Remarque : pour tout ':' l'interpréteur Python attend une identation.
def fonction0():
    print("Bonjour")
    
fonction0()

# la documentation de la fonction
def fonction1(s):
    """
    Affichage d'une chaine et de sa longueur

    Parameters
    ----------
    s : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    """
    print("%s est de longueur %d" % (s, len(s)))
    
fonction1("Bonjour Université de Lorraine !")
help(fonction1)

# la valeur de retour est précisée par le mot clé return
def square (x):
    """
    Retourne le carré de x
    """
    return x ** 2
print("la fonction square retourne le carré du paramètre spécifié:", square(2))

# on peut retourne plusieurs valeurs
def powers(x):
    """
    Retourne les premières puissances de x
    """
    return x**2,x**3,x**4
out = powers(3)
print(type(out))
print(len(out))
print(out[1])
print(out)

# il est possible de dépiler les éléments par assignation
x1, x2, x3 = powers(3)
print(x1)

# arguments par défaut
def ma_fonction(x, p=2, debug=False):
    if debug:
        print("evaluation ma_fonction avec x = %s et l'exposant p = %s"
              % (x, p))
    return x ** p
ma_fonction(5)
ma_fonction(5, debug=True)
ma_fonction(5, 4, True)

# les paramètres sont passés par référence, donc il faut faire attention
# aux effets de bord
def fonction(l):
    l += l
a = [1, 2]
fonction(a)
print(a)

# pour éviter ce problème, on doit faire une copie
def fonction1(l):
    l = list(l)
    l += l
a = [1, 2]
fonction1(a)
print("dans ce cas, on a fait une copie du tableau passé en argument, donc a " 
      + "n\'est pas modifié : ",a)