from math import sqrt

#Calcolo distanza euclidea tra due punti
def distanza_euclidea(p1,p2):
    x1,y1 = p1
    x2,y2 = p2
    return sqrt((x2-x1)**2+(y2-y1)**2)

    
