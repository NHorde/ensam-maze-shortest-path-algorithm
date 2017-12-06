# -*-coding:Latin-1 -*

# fonction qui demande �  l'utilisateur de rentrer la taille du labyrinthe

def tailleLabyrinthe():
	k=0
	while k!=1:
		n=input("Quelle est la taille du labyrinthe? Entrez un entier naturel: ")
		if n.isdigit():
			n=int(n)
			k+=1
		else:
			print("Entrez un entier naturel")
	return n

# fonction qui demande �  l'utilisateur la densité du labyrinthe

def densiteLabyrinthe():
	k=0
	while k!=1:
		m=input("Quelle est la densité du labyrinthe? Entrez un nombre entre 0 et 100 (pourcentage): ")
		if m.isdigit():
			m=int(m)
			k+=1
		else:
			print("Entrez un entier naturel")
	return m
	
# affichage des murs et des passages du labyrinthe

def affichageBatiment(matrice,n):
	print ()
	print ("Voici votre labyrinthe :")
	print ()
	l=0
	for i in range(0,n):
		print(l,end="")
		l=l+1
		if l<=10:
			print("  |",end="")
		else:
			print(" |",end="")
		for j in range(0,n):
			if matrice[i][j]==-2:
				print(" ", end=" ")
			else:
				print(" X",end="")
			print(" |",end="")
		print()
		print()
	if n>10:
		l=0
		for k in range (0,1):
			print("    ",k,end=" |")
		for k in range (1,10):
			print("",k,end="  ")
		for k in range(10,n):
			print("",k,end=" ")
	else:
		for k in range (0,1):
			print("    ",k,end=" |")
		for k in range (1,n):
			print("",k,end="  ")	
		
# fonction qui demande �  l'utilisateur de rentrer le départ et l'arrivée
def programmeUtilisateur(batiment):
	k=0
	l=0
	# boucle pour vérifier que l'utilisateur ne rentre pas des murs
	while l!=1:
		# boucle pour vérifier que l'utilisateur rentre bien des nombres
		while k !=1:
			print ()
			print ("Quelles sont les coordonnées de votre point de départ ?")
			ordonnee_depart=input("   Ordonnée de votre point de départ :")
			abscisse_depart=input("   Abscisse de votre point de départ :")
			if not ordonnee_depart.isdigit() or not abscisse_depart.isdigit():
				print("Entrez des entiers naturels")
			else:
				abscisse_depart=int(abscisse_depart)
				ordonnee_depart=int(ordonnee_depart)
				k+=1
				if batiment[abscisse_depart][ordonnee_depart]==-1: 
					print("Le point de départ ne peut pas être confondu avec un mur,")
					k-=1
				else: 
					a=int(ordonnee_depart)
					b=int(abscisse_depart)
					batiment[a][b]= -3
					l+=1
	# même chose pour l'arrivée
	k=0
	l=0
	while l!=1:
		while k !=1:
			print ()
			print ("Quelles sont les coordonnées de votre point d'arrivée ?")
			ordonnee_arrivee=input("   Ordonnée de votre point d'arrivée :")
			abscisse_arrivee=input("   Abscisse de votre point d'arrivée :")
			if not ordonnee_arrivee.isdigit() or not abscisse_arrivee.isdigit():
				print()
				print("Entrez des entiers naturels")
			else:
				abscisse_arrivee=int(abscisse_arrivee)
				ordonnee_arrivee=int(ordonnee_arrivee)
				k+=1
				if batiment[abscisse_arrivee][ordonnee_arrivee]==-1: 
					print("Le point d'arrivée ne peut pas être confondu avec un mur,")
					k-=1
				else: 
					c=int(ordonnee_arrivee)
					d=int(abscisse_arrivee)
					batiment[c][d]= -4
					l+=1
	return a,b,c,d
 
# affichage des murs, passages, départ et arrivée

def affichageBatimentAmeliore(matrice,a,b,c,d,n):
	print("")
	print("Voici votre labyrinthe :")
	print("")
	l=0
	for i in range(0,n):
		print(l,end="")
		l=l+1
		if l<=10:
			print("  |",end="")
		else:
			print(" |",end="")
		for j in range(0,n):
			if matrice[i][j]==-2:
				print("  ", end=" ")
			elif matrice[i][j]==-3:
				print(" D", end=" ")
			elif matrice[i][j]==-4:
				print(" A",end=" ")
			elif matrice[i][j]==1:
				print(" 1",end=" ")
			else:
				print(" X",end=" ")
			print("|",end="")
		print()
		print()
	l=0
	for k in range (0,1):
		print("    ",k,end=" |")
	for k in range (1,10):
		print("",k,end="  ")
	for k in range(10,n):
		print("",k,end=" ")
		
# fonction de déboggage qui n'a aucun intérêt pour la résolution du labyrinthe, on s'en est servi pour vérifier que le programme marchait 
# correctement

def affichageTarjan(matrice,coordAbs,n):
	l=0
	for i in range(0,n):
		print(l,end="")
		l=l+1
		if l<=10:
			print("  |",end="")
		else:
			print(" |",end="")
		for j in range(0,n):
			if matrice[i][j]==-2:
				print(" ", end=" ")
			elif matrice[i][j]==-3:
				print(" D", end=" ")
			elif matrice[i][j]==-4:
				print(" A",end="")
			elif matrice[i][j]==1:
				print(" 1",end=" ")
			elif matrice[i][j]==2:
				print(" 2",end=" ")
			elif matrice[i][j]==3:
				print(" 3",end=" ")
			elif matrice[i][j]==4:
				print(" 4",end=" ")
			elif matrice[i][j]==5:
				print(" 5",end=" ")
			elif matrice[i][j]==6:
				print(" 6",end=" ")
			elif matrice[i][j]==7:
				print(" 7",end=" ")
			elif matrice[i][j]==8:
				print(" 8",end=" ")
			elif matrice[i][j]==9:
				print(" 9",end=" ")
			else:
				print("X",end=" ")
			print("|",end="")
		print()	
		print()
	if n>10:
		l=0
		for k in range (0,1):
			print("    ",k,end=" |")
		for k in range (1,10):
			print("",k,end="  ")
		for k in range(10,n):
			print("",k,end=" ")
	else:
		for k in range (0,1):
			print("    ",k,end=" |")
		for k in range (1,n):
			print("",k,end="  ")	

# affichage du plus court chemin

def affichageResolution(matrice,a,b,c,d,n,coordAbs):

	l=0
	for i in range(0,n):
		print(l,end="")
		l=l+1
		if l<=10:
			print("  |",end="")
		else:
			print(" |",end="")
		for j in range(0,n):
			if matrice[i][j]==-3:
				print(" D",end=" ")
			elif matrice[i][j]==-4:
				print(" A",end=" ")
			elif matrice[i][j]==-5:
				print(" .",end=" ")
			elif matrice[i][j]==-1:
				print(" X",end=" ")
			else:
				print("  ",end=" ")
			print("|",end="")
		print()		
		print()
	if n>10:
		l=0
		for k in range (0,1):
			print("    ",k,end=" |")
		for k in range (1,10):
			print("",k,end="  ")
		for k in range(10,n):
			print("",k,end=" ")
	else:
		for k in range (0,1):
			print("    ",k,end=" |")
		for k in range (1,n):
			print("",k,end="  ")	
	# Les deux print qui suivent permettent que le "Appuyez sur une touche pour continuer" soit situé tout en bas de la console
	# et non au niveau des abscisses
	print()
	print()
