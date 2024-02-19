from Case import*
import matplotlib.pyplot as plt

class Grille : 
	#constructeur 
	def __init__(self,longueur,largeur):
		#initialisation des attributs 
		self._long=longueur
		self._larg=largeur
		self._grille =[[Case(i,j) for j in range(self._long)] for i in range(self._larg)]
		self.Adjust()

	#accesseurs en lecture
	def getLongueur(self):
		return self._long

	def getLargeur(self):
		return self._larg

	# Methode d'affichage  de la grille avec pyplot  
	def Affich(self,L):
		plt.figure()
		# tracé de la grille avec pyplot
		for i in range(self._larg):
			for j in range(self._long):
				self._grille[i][j].Affich()

		# trace du chemin dans la grille avec pyplot 
		for i in range(len(L)-1):
			x1,y1=L[i]
			x2,y2=L[i+1]
			plt.plot([x1+0.5, x2+0.5],[y1+0.5, y2+0.5],linewidth=3, color ="red")
		plt.show()

	# methode pour recuperer une case de la grille en donnant ses coordonnées en parametre
	def getCase(self,x,y):
		if x>=0 and x<self.getLongueur() and y>=0 and y<self.getLargeur():
			return self._grille[x][y]

	# Methode d'ajustement des murs de chaque cellule
	def Adjust(self):
		for i in range(self._larg):
			for j in range(self._long):
				
				if i>0 and j==0 :
					self._grille[i][j]._bottomWall=self._grille[i-1][j]._topWall
				elif i>0 and j>0:
					self._grille[i][j]._bottomWall=self._grille[i-1][j]._topWall
					self._grille[i][j]._leftWall=self._grille[i][j-1]._rightWall
				elif i==0 and j>0:
					self._grille[i][j]._leftWall=self._grille[i][j-1]._rightWall

		







	
