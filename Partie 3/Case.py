import matplotlib.pyplot as plt
from random import*

class Case:
	#constructeur
	def __init__(self,px,py):
		#initialisation des attributs 
		self._topWall = choice([2,5,7,10,15])
		self._bottomWall =choice([1,3,6,10,15])
		self._leftWall =choice([1,3,6,10,15])
		self._rightWall =choice([1,3,6,10,15])
		self._posX=px
		self._posY=py
	#accesseur 
	def getX(self):
		return self._posX

	def getY(self):
		return self._posY

	#methode d'affichage
	def Affich(self):
		#tracé realié avec pyplot 
		plt.plot([self.getX(), self.getX()],[self.getY(), self.getY()+1],linewidth=self._leftWall,color ="skyblue")
		plt.plot([self.getX()+1, self.getX()+1],[self.getY(), self.getY()+1],linewidth=self._rightWall,color ="skyblue")
		plt.plot([self.getX(), self.getX()+1],[self.getY(), self.getY()],linewidth=self._bottomWall,color ="skyblue")
		plt.plot([self.getX(), self.getX()+1],[self.getY()+1, self.getY()+1],linewidth=self._topWall,color ="skyblue")

	

		



