#-----------------------------------------

# Python + Matplotlib Penrose
# Taken from http://www.bubuko.com/infodetail-911894.html

#-----------------------------------------

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.path import Path
from matplotlib.patches import PathPatch

plt.figure(figsize=(1.5,1.5),dpi=500)
plt.subplot(aspect=1)
plt.axis([0,2,0,2])
plt.xticks([])
plt.yticks([])
plt.axis('off')

l = 1.09263860050852263
a = l**(0-5)
b = l**(0-3)

def subdivide(triangles):
	result = []
	for color,A,B,C in triangles:
		for i in range(4):
			if color == i:
				result +=[(i+1,A,B,C)]
		if color == 4:
			P = A + (C-A)*(l**(0-10))
			result +=[(0,A,P,B),(2,B,P,C)]
	return result

def DrawFigure(triangles):
    for color,A,B,C in triangles:
        vertices = [C,A,B,C]
        codes = [Path.MOVETO]+[Path.LINETO]*3
        tri = Path(vertices,codes)
        if color == 0:
            tri_patch=PathPatch(tri,facecolor='#222222',edgecolor='#000000',linewidth=0.1)
        if color == 1:
        	tri_patch=PathPatch(tri,facecolor='#444444',edgecolor='#000000',linewidth=0.1)
        if color == 2:
        	tri_patch=PathPatch(tri,facecolor='#666666',edgecolor='#000000',linewidth=0.1)
        if color == 3:
        	tri_patch=PathPatch(tri,facecolor='#888888',edgecolor='#000000',linewidth=0.1)
        if color == 4:
        	tri_patch=PathPatch(tri,facecolor='#AAAAAA',edgecolor='#000000',linewidth=0.1)
        plt.gca().add_patch(tri_patch)
    plt.show()

triangles = []
A=np.array([0,0])
B=np.array([2*l**(0-5),0])
C=np.array([2*l**(0-5),2*l**(0-3)])
triangles.append([0,A,B,C])

print "Pythagorean(5,2) Tiling"
m = input('Enter number of divisions: ')
for j in xrange(m):
	triangles=subdivide(triangles)

DrawFigure(triangles)