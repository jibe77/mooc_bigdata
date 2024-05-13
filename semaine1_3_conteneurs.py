#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  4 21:17:30 2024

@author: jean-baptisterenaux
"""

# chaines de caractères avec "" ou ''
s = "Bonjour Université de Lorraine"
s = 'Bonjour Université de Lorraine'
print(s)
print(type(s))

# accès à un sous-élément
print('affichage du premier élément de la chaine de caractères:',s[0])
print('affichage du dernier élément de la chaine de caractères:',s[-1])

# extraction d'une sous-chaine
print('extraction d''une sous-chaine avec s[0:7] : ', s[0:7])
start, stop = 1, 7
print(s[start:stop])
print(len(s[start:stop]))
print(stop-start)

# on peut omettre start ou stop
print('affichage des 7 premiers caractères:', s[:7])
print('affichage à partir du 8ème caractères :', s[8:])
print('affichage des 8 derniers caractères : ', s[-8:])

# utilisation du slicing
s = "ababababa"
print('affichage des a:', s[0::2])
print('affichage des b:', s[1::2])

# mise en forme des chaines de caractères
print("Ici tout est converti en string:", "str1", 1.0, False, -1j)
print("Ici les chaines sont concaténées " + "str1" + "str2" + "str3")
print("Multiplication de la string" * 3)

# formatage
a = 1.0
print("val = %e" % a)
print("val = %f" % a)
print("val = %s" % a)
print("val1 = %.2f, val2 = %d" % (3.1415, 1.5))

# listes
l = [1,2,3,4]
print(l)
print(type(l))
print('affichage du premier élément:', l[0])
print('affichage de l\'avant dernier élément:', l[-2])
print('affichage de l\'élément 1 à 3:', l[1:3])
print('affichage d\'un élément sur 2:', l[::2])

# on peut mélanger les types
l = [1,'a',1.0,-1j]
print(l)

# on peut faire des listes de listes
liste_de_listes = [1, [2, [3, [4, [5]]]]]
print(liste_de_listes)

# la fonction range pour générer des listes d'entiers
start, stop, step = 10, 30, 2
print('la fonction range génère des listes d\'entiers:', 
      list(range(start, stop, step)))
print('gènère des entiers de -10 à 10:', list(range(-10, 10)))
n = 10
print(list(range(n-1, -1, -1)))

# pour convertir une chaine de caractères en liste
s = "zabcda"
l = list(s)
print('on convertit une string en chaine de caractères :', l)

# pour trier une liste
l_sorted = sorted(l)
print(l)
print(l_sorted)

# cette syntaxe appelle la méthode sort() 
# et modifie la liste en court de manipulation sans en créer un autre
l.sort()
print(l)

# ajouter, insérer, modifier et enlever des éléments dans une liste
# création d'une liste vide
l = []
l.append("A")
l.append("d")
l.append("d")
print(l)
print('compte le nombre de d dans la string:', l.count('d'))

# on peut modifier la liste par assignation
l[2] = 'c'
print(l)
l[1:3] = ["f", "f"]
print(l)

# insertion d'élément
l.insert(0,"i")
l.insert(1,"n")
l.insert(2,"s")
l.insert(3,"e")
l.insert(4,"r")
l.insert(5,"t")
print(l)

# suppression d'un élément
l.remove("A")
l.remove("f") # supprime uniquement le premier f
print(l)

# vérifier la présence d'une valeur dans la liste
print("Est-ce que A est présent dans la liste ?", "A" in l)
print("Index de i dans la liste : ", l.index("i"))

# suppression à un index précis
del l[0]
print(l)

# pour concatener des listes
l1 = [1,2,3]
l2 = [4,5,6]
print(l1 + l2)
print(l1 * 2)

# pour plus d'information :
help(list)