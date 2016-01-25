#-----------------------------------------

# Python + Matplotlib Penrose
# Taken from http://www.bubuko.com/infodetail-911894.html

#-----------------------------------------

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.path import Path
from matplotlib.patches import PathPatch

plt.figure(figsize=(8,6),dpi=100)
plt.subplot(aspect=1)
plt.axis([-5,5,-5,5])
plt.xticks([])
plt.yticks([])
plt.axis('off')

a = np.sqrt(2*(np.sqrt(17)-1))
b = np.sqrt(17)-1
c = 4

def subdivide(triangles):
	result = []
	for color,A,B,C in triangles:
		P = A+(C-A)*(b**2/c**2)
		Q = A+(B-A)*(0.5)
		R = A+(C-A)*(b**2/(2*c**2))
		S = A+(B-A)*0.5+(C-A)*(b**2/(2*c**2))
		result += [(1,A,R,Q),(1,P,R,Q),(1,Q,S,P),(1,Q,S,B),(0,B,P,C)]
	return result

def DrawFigure(triangles):
    for color,A,B,C in triangles:
        vertices = [C,A,B,C]
        codes = [Path.MOVETO]+[Path.LINETO]*3
        tri = Path(vertices,codes)
        if color == 0:
            tri_patch=PathPatch(tri,facecolor='#333333',edgecolor='#666666',linewidth=0.8)
        else:
            tri_patch=PathPatch(tri,facecolor='#AAAAAA',edgecolor='#666666',linewidth=0.8)
        plt.gca().add_patch(tri_patch)
    plt.show()

A=np.array([0,0])
B=np.array([b,0])
C=np.array([b,c])
triangles = []
triangles.append([0,A,B,C])

m = input('Enter number of divisions: ')
for j in xrange(m):
    triangles=subdivide(triangles)
	
DrawFigure(triangles)