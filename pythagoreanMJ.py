#-----------------------------------------

# Python + Matplotlib Penrose
# Taken from http://www.bubuko.com/infodetail-911894.html

#-----------------------------------------

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.path import Path
from matplotlib.patches import PathPatch
from mpmath import *

plt.figure(figsize=(1.5,1.5),dpi=500)
plt.subplot(aspect=1)
plt.axis([0,1,0,1])
plt.xticks([])
plt.yticks([])
plt.axis('off')

print "Pythagorean(m,j) Tiling"
m = input('Enter the value of m (an integer at least 3): ')
n = input('Enter the value of j (less than m): ')
p=m-1
q=n-m

mp.dps = 20
mp.pretty = True
f = lambda x: x**m-x**n-1
L=findroot(f,1)
l=L**(0.5)

def subdivide(triangles):
	result = []
	for color,A,B,C in triangles:
		if color == p:
			P = A + (C-A)*(l**(0-2*m))
			result +=[(0,A,P,B),(n,B,P,C)]
		for i in xrange(p):
			if color == i:
				result +=[(i+1,A,B,C)]
	return result

def DrawFigure(triangles):
    for color,A,B,C in triangles:
        vertices = [A,B,C,A]
        codes = [Path.MOVETO]+[Path.LINETO]*3
        tri = Path(vertices,codes)
        tri_patch=PathPatch(tri,facecolor='#AAAAAA',edgecolor='#000000',linewidth=0.1)
        plt.gca().add_patch(tri_patch)
    plt.show()

triangles = []
A=np.array([0,0])
B=np.array([l**(-m),0])
C=np.array([l**(-m),l**q])
triangles.append([0,A,B,C])

a = input('Enter number of divisions: ')
for j in xrange(a):
	triangles=subdivide(triangles)

DrawFigure(triangles)