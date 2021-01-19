

# -*-coding:Latin-1 -*

from labyrintheLogique import *
from labyrintheInterfaceUtilisateur import *

def main():
	print("              RÃ©solution d'un labyrinthe par le plus court chemin             ")
	print()
	print()
	t=tailleLabyrinthe()
	l=densiteLabyrinthe()
	
	batiment = generationBatiment(t,l) # crÃ©ation du labyrinthe
	
	affichageBatiment(batiment,t) # affichage du labyrinthe
	
	a,b,c,d = programmeUtilisateur(batiment) 
	
# fonction de dÃ©boggage
#	affichageBatimentAmeliore(batiment,a,b,c,d,t)
	
	algorithmeTarjan(t,batiment,a,b,c,d) # algorithme de Tarjan (rÃ©solution du labyrinthe)
	
	k=algorithmeTarjan(t,batiment,a,b,c,d)
	
#fonction de dÃ©boggage
#	affichageTarjan(batiment,k,t)
	
	solutionLabyrinthe(batiment,a,b,c,d,t) # on vÃ©rifie si le labyrinthe a une solution
	h=solutionLabyrinthe(batiment,a,b,c,d,t)
	
	algorithmeTarjanRetour(batiment,a,b,c,d,t,k,h) # calcul du retour s'il y a une solution
	
	affichageResolution(batiment,a,b,c,d,t,k) # affichage du plus court chemin
	
main() # appel de tout le programme


