from Case import*
from Grille import*



 ############################################################################  
 #  VEUILLEZ    DECOMMENTER DANS LA PARTIE TEST POUR UNE VUEEN CONSOLE      #
 ############################################################################


 ###############################################  
 #   PARTIE 2                                  #
 ###############################################

 ###############################################  
 #  QUESTION B                                #
 ###############################################

def Graphe(G):
    D = {}
    for x in range(G.getLongueur())  :
        for y in range(G.getLargeur()) :
            if x>0 and x<(G.getLongueur()-1) and y>0 and y<G.getLargeur() or (x==0 and y>0):
                D[(x,y)]=[[G.getCase(x,y)._rightWall,G.getCase(x+1, y)],[G.getCase(x,y)._bottomWall,G.getCase(x, y-1)]]
            elif y==0  and x<(G.getLongueur()-1)  :
                D[(x,y)]=[[G.getCase(x,y)._rightWall,G.getCase(x+1, y)]]  
            elif x==(G.getLongueur()-1) and y>0 :
                D[(x,y)]=[[G.getCase(x,y)._bottomWall,G.getCase(x, y-1)]]
            elif x==(G.getLongueur()-1) and y==0:
                D[(x,y)]=[]
    return D       



    

 ###############################################  
 #  PARTIE 2 QUESTION C                        #
 ###############################################

def minimum(dico):
    m=float('inf')
    for k in dico: #parcours des clés
        if dico[k] < m:
            m=dico[k]
            i=k
    return i


def dijkstra(G,s):
    D={} #tableau final des distances minimales
    d={k: float('inf') for k in G} #distances initiales infinies
    d[s]=0 #sommet de départ
    while len(d)>0: #fin quand d est vide
        k=minimum(d) #sommet de distance minimale pour démarrer une étape
        for i in range(len(G[k])): #on parcourt les voisins de k
            v, c = G[k][i][1],G[k][i][0] #v voisin de k, c la distance à k
            x,y=v.getX(),v.getY()
            cord=(x,y)
            if cord not in D: #si v n'a pas été déjà traité
                d[cord]=min(d[cord], d[k]+c) #est-ce plus court en passant par k ?
        D[k]=d[k] #copie du sommet et de la distance dans D
        del(d[k]) #suppression du sommet de d
    return D




 ###############################################  
 #  PARTIE 2 QUESTION D ET E                   #
 ###############################################

def dijkstra_pred(G,s):
    D={} #tableau final des distances minimales
    d={k: float('inf') for k in G} #distances initiales infinies
    d[s]=0 #sommet de départ
    P={} #liste des prédécesseurs
    while len(d)>0: #fin quand d est vide
        k=minimum(d) #sommet de distance minimale pour démarrer une étape
        for i in range(len(G[k])): #on parcourt les voisins de k
            v, c = G[k][i][1],G[k][i][0] #v voisin de k, c la distance à k
            x,y=v.getX(),v.getY()
            cord=(x,y)
            if cord not in D: #si v n'a pas été déjà traité
                if d[cord]>d[k]+c:  #est-ce plus court en passant par k ?
                    d[cord]=d[k]+c
                    P[cord]=k  #stockage du prédécesseur de v
        D[k]=d[k] #copie du sommet et de la distance dans D
        del(d[k]) #suppression du sommet de d
    #return D,P

    chemin=[] # chemin final
    fin=(grille.getLongueur()-1,0)
    temp=fin
    while temp!=s: # tant qu'on a pas encore trouve le debut 
        chemin.append(P[temp])
        temp=P[temp]
    chemin=[fin]+chemin
    return chemin

    
 ###############################################  
 #   PARTIE TEST DU PROGRAMME                  #
 ###############################################

grille=Grille(6,6)
Q=Graphe(grille)
deb=(0,grille.getLargeur()-1)
A=dijkstra_pred(Q,deb)
grille.Affich(A)   # Affichage avec le chemin demandé dans la partie 3 avec pyplot


            

