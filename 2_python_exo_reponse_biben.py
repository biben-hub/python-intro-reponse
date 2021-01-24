#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# COMMENTEZ CHAQUE LIGNE DE CE SCRIPT EN EXPLIQUANT CE QU'ELLE FAIT ET POURQUOI
'''
permet d'importer la bibliothèque de méthodes générant des nombres pseudo-aléatoires

déclaration et initialisation d'une variable de type string (x6)

déclaration est initialisation d'un tableau

déclaration et initialisation d'une variable de type integer


déclaration d'une variable qui stock le résultat de la division 
de la taille de la liste names par le nbre maximum d'éléments par groupe

déclaration d'une boucle for qui parcours l'interval du nombre de groupe

variable locale qui stock un echantillon parmis les noms dans la liste pour un tirage aléatoire

#affiche les groupes et les noms séléctionnés pour chaque groupe

#la boucle for ici va supprimer chaque noms qui auront été séléctionnés dans la liste names pour s'assurer que tous les noms de la liste auront bien été utilisés
'''


# In[ ]:


# EXPLIQUEZ CE QUE FAIT RANDOM.SAMPLE ET LES ALTERNATIVES QUI EXISTENT EN CHERCHANT SUR INTERNET
'''
random.sample choisit un échantillon dans un ensemble 
et renvoie une liste de k élément séléctionné de manière aléatoire

les alternatives sont :

random.shuffle

'''


# In[ ]:


# EXPLIQUEZ LE %S DU PRINT, QUELS SONT LES AUTRES POSSIBILITES
'''
%s est formatage des valeurs des variables
dans ce cas, il récupère la valeur de i et selected et affiche la valeur en string

les alternatives sont les suivantes :

print("GROUP #{} : {}".format(i, selected))
print("GROUP #{i} : {selected}})
print("GROUP #",{i} , " : ",{selected})
print("GROUP #", i, ":", selected)
'''


# In[ ]:


# EXPLIQUEZ LE BUT DE CE SCRIPT
'''
créer 3 binômes
'''


# In[15]:


import random

name1 = 'name1'
name2 = 'name2' 
name3 = 'name3'
name4 = 'name4'
name5 = 'name5'
name6 = 'name6'


names = [name1, name2, name3, name4, name5, name6] 
print(names, '\n')
nb_groups = 3

max_nb_groups = int(len(names) / nb_groups) 


for i in range(nb_groups):
    
    selected = random.sample(names, k=max_nb_groups)
    
    print("GROUP #%s : %s" % (i, selected), '\n')
    
    for sel in selected:
        names.remove(sel)


# In[ ]:


# MODIFIEZ LE SCRIPT POUR SELECTIONNER UN A UN LES MEMBRES DE LA LISTE "selected"


# In[17]:


import random

name1 = 'name1'
name2 = 'name2' 
name3 = 'name3'
name4 = 'name4'
name5 = 'name5'
name6 = 'name6'


names = [name1, name2, name3, name4, name5, name6] 
print(names, '\n')
nb_groups = 6

max_nb_groups = int(len(names) / nb_groups) 


for i in range(nb_groups):
    
    selected = random.sample(names, k=max_nb_groups)
    
    print("GROUP #%s : %s" % (i, selected), '\n')
    
    for sel in selected:
        names.remove(sel)


# In[ ]:


# MODIFIEZ LE SCRIPT PRECEDANT POUR OBTENIR LE MEME FONCTIONNEMENT SANS AVOIR A DETERMINER LE NOMBRE DE GROUPES
# INDICE: TOUT SE PASSE SUR LA LISTE NAMES
# INDICE: PENSER A WHILE


# In[53]:


import random

name1 = 'name1'
name2 = 'name2' 
name3 = 'name3'
name4 = 'name4'
name5 = 'name5'
name6 = 'name6'


names = [name1, name2, name3, name4, name5, name6] 
x = 3 #compteur

while (x < len(names)):
    selected = random.sample(names, k = 2)
    x = x + 1
    print(selected)

