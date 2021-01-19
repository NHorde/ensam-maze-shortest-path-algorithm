

# -*-coding:Latin-1 -*

from labyrintheLogique import *
from labyrintheInterfaceUtilisateur import *

def main():
	print("              Résolution d'un labyrinthe par le plus court chemin             ")
	print()
	print()
	t=tailleLabyrinthe()
	l=densiteLabyrinthe()
	
	batiment = generationBatiment(t,l) # création du labyrinthe
	
	affichageBatiment(batiment,t) # affichage du labyrinthe
	
	a,b,c,d = programmeUtilisateur(batiment) 
	
# fonction de déboggage
#	affichageBatimentAmeliore(batiment,a,b,c,d,t)
	
	algorithmeTarjan(t,batiment,a,b,c,d) # algorithme de Tarjan (résolution du labyrinthe)
	
	k=algorithmeTarjan(t,batiment,a,b,c,d)
	
#fonction de déboggage
#	affichageTarjan(batiment,k,t)
	
	solutionLabyrinthe(batiment,a,b,c,d,t) # on vérifie si le labyrinthe a une solution
	h=solutionLabyrinthe(batiment,a,b,c,d,t)
	
	algorithmeTarjanRetour(batiment,a,b,c,d,t,k,h) # calcul du retour s'il y a une solution
	
	affichageResolution(batiment,a,b,c,d,t,k) # affichage du plus court chemin
	
main() # appel de tout le programme


