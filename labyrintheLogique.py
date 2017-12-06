# -*-coding:Latin-1 -*

import random

# On crée la matrice en faisant une liste (en abscisse) de liste (en ordonnée). 
# La matrice est composé de nombres qui valent:
# murs = -1
# passages = -2
# départ = -3
# arrivée = -4
# case par lequel le plus court chemin passe = -5


# création de la matrice

def generationBatiment(n,m):
	matrice = []
	for i in range (0,n):
		matrice.append([])
		for j in range (0,n):
			matrice[i].append(random.randint(0,100))
			if matrice[i][j]<=m:
				matrice[i][j]=-1 # murs
			else:
				matrice[i][j]=-2 # passages
		
	return matrice


# Résolution du labyrinthe par l'algorithme de Tarjan. On crée deux listes qui fonctionnent de manière simultanée et qui contiennent
# l'abscisse et l'ordonnée de la case visitée. On part du début donc à l'abscisse a et l'ordonnée b qui correspondent au départ. On regarde 
# d'abord le voisin de droite. S'il c'est un mur, on ne fait rien. Si c'est un passage, on lui affecte la valeur "1", on incrémente alors
# la liste "liste" de 1, il est à noter que l'important n'est pas la valeur mais la taille de "liste". On effectue la même opération avec
# le voisin de droite, puis du haut et enfin de gauche: on vient de finir la première génération (cases valant "1").  On enregistre à chaque fois
# fois l'abscisse et l'ordonnée du point où la valeur "1" y est affectée afin de le réutiliser.  
# Deuxième génération: on refait le même principe pour les cases qui valent "1" (donc de 0 à 4 cases suivant la taille de "liste"). Seul
# changement: si la case adjacente a déjà été visitée on ne fait rien.
# Il est important de noter que la boucle s'arrête au bout de 7*l opérations et non pas dès qu'il atteint l'arrivée. Pour un labyrinthe 
# 10 x 10, la boucle effectue 7*10 opérations soit 70 opérations. Ce point sera expliqué en soutenance (on peut encore l'optimiser mais
# on n'y est pas arrivé...)

def algorithmeTarjan(n,batiment,a,b,c,d):
	l=1
	coordAbs=[a]
	coordOrd=[b]
	liste=[1]

	while l!=n*n: #(c+1 not in coordAbs and d not in coordOrd) or (c-1 not in coordAbs and d not in coordOrd) or (c not in coordAbs and d+1 not in coordOrd) or (c not in coordAbs and d-1 not in coordOrd): 
		
		for m in range (0,len(liste)):
			a=coordAbs[m]
			b=coordOrd[m]
			if a+1<n and a+1>-1 and batiment[a+1][b]==-2:
				batiment[a+1][b]=l
				coordAbs.append(a+1)
				coordOrd.append(b)
				liste.append(1)
			else:
				1
		
			if b+1<n and b+1>-1 and batiment[a][b+1]==-2:
				batiment[a][b+1]=l
				coordAbs.append(a)
				coordOrd.append(b+1)
				liste.append(1)
			else:
				1
				
			if a-1>-1 and batiment[a-1][b]==-2:
				batiment[a-1][b]=l
				coordAbs.append(a-1)
				coordOrd.append(b)
				liste.append(1)
			else:			
				1
						
			if b-1>-1 and batiment[a][b-1]==-2:
				batiment[a][b-1]=l
				coordAbs.append(a)
				coordOrd.append(b-1)
				liste.append(1)
			else:
				1
		l=l+1
	
	return coordAbs
	
	
# la fonction solutionLabyrinthe permet de vérifier si le labyrinthe admet une solution. On regarde la case arrivée: s'il n'y a pas de
# solutions alors les 4 cases adjacentes sont soient des murs soit un passage (l'algorithme de Tarjan a tourné en boucle dans une zone
# fermée. S'il y a une solution alors au moins une des 4 adjacentes possèdent une valeur positive.

def solutionLabyrinthe(matrice,a,b,c,d,n):
	j=0
	if d+1>n-1 and c+1>n-1:
		if matrice[c-1][d]>0 or matrice[c][d-1]>0:
			j=1
		else:
			j=-1
			
	if c+1>n-1:
		if matrice[c-1][d]>0 or matrice[c][d+1]>0 or matrice[c][d-1]>0:
			j=1
		else:
			j=-1

	if d+1>n-1:
		if matrice[c-1][d]>0 or matrice[c][d-1]>0:
			j=1
		else:
			j=-1

		
	if c+1<n-1 and d+1<n-1:
		if matrice[c-1][d]>0 or matrice[c+1][d]>0 or matrice[c][d+1]>0 or matrice[c][d-1]>0:
			j=1
		else:
			j=-1
	return j
	
# fonction qui permet de retrouver le plus court chemin. On part de l'arrivée. S'il n'y a pas de solutions on ne fait rien. S'il y en a une,
# alors nécessairement au moins une des 4 cases adjacentes à l'arrivée a une valeur positive. En effet les 4 cases adjacentes ont pour
# valeur soit "-1" (murs) soit "-2" (passage) soit un nombre positif qui a été calculé par l'algorithme de Tarjan. On enregistre en mémoire
# la case dont la valeur est la plus petite ET qui est supérieure à 0 (car sinon c'est un mur). On refait de même jusqu'à arriver au départ.

def algorithmeTarjanRetour(matrice,a,b,c,d,n,coordAbs,j):
	if j==1:
		print()
		print("Le labyrinthe a une solution")
		print()
		l=0
		o=1
		retourAbs=[c]
		retourOrd=[d]
		liste=[]

		while 1 not in liste:
		
			for m in range(o-1,o):
				l=0
				c=retourAbs[m]
				d=retourOrd[m]
				if c+1>n-1 and d+1>n-1:
					test=[matrice[c-1][d],matrice[c][d-1]]
					e=min(el for el in test if el > 0)
			
				elif c+1>n-1:
					testdeux=[matrice[c-1][d],matrice[c][d-1],matrice[c][d+1]]
					e=min(el for el in testdeux if el > 0)
			
				elif d+1>n-1:
					testtrois=[matrice[c-1][d],matrice[c+1][d],matrice[c][d-1]]
					e=min(el for el in testtrois if el > 0)
			
				else:
					testquatre=[matrice[c-1][d],matrice[c+1][d],matrice[c][d-1],matrice[c][d+1]]
					e=min(el for el in testquatre if el > 0)
				liste.append(e)
				
				if c-1>-1 and e==matrice[c-1][d] and l!=1:
					retourAbs.append(c-1)
					retourOrd.append(d)
					matrice[c-1][d]=-5
					
					l=l+1
				else:
					l=l
					
				if c+1<n-1 and l!=1 and e==matrice[c+1][d]:
					retourAbs.append(c+1)
					retourOrd.append(d)
					matrice[c+1][d]=-5
					l=l+1
				else:
					l=l
					
				if d-1>-1 and l!=1 and e==matrice[c][d-1]:
					retourAbs.append(c)
					retourOrd.append(d-1)
					matrice[c][d-1]=-5
					l=l+1
				else:
					l=l
					
				if d+1<n-1 and l!=1 and e==matrice[c][d+1]:
					retourAbs.append(c)
					retourOrd.append(d+1)
					matrice[c][d+1]=-5
					l=l+1
				else:
					l=l
			o=o+1
		print("Le plus court chemin est de ",o-1,"coups")
		
	else:
		print()
		print("Le labyrinthe n'a pas de solution")
		print()
	
