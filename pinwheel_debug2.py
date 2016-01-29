#-----------------------------------------

# Python + matplotlib + numpy + mpmath
# Modified from http://www.bubuko.com/infodetail-911894.html

#-----------------------------------------

import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
from matplotlib.path import Path
from matplotlib.patches import PathPatch
from mpmath import *

plt.figure(figsize=(2,1.4),dpi=500)
plt.subplot(aspect='equal')
plt.axis([0,5,0,5])
plt.xticks([])
plt.yticks([])
plt.axis('off')

print "Pinwheel(p,q) Tiling"
p = input('Enter the value of p: ')
q = input('Enter the value of q: ')
m = input('Enter number of divisions: ')


# Now we calculate the proportions of the triangles based on (p,q). The number b provides
# the base of a triangle, and the number a provides the height. The hypotenuse equals 1.

mp.dps = 20
mp.pretty = True
f = lambda x: (0.5*(1-x**2))**(p/2)-x**q
a0=findroot(f,0.5)
b0=(1-a0**2)**(0.5)
a=a0/((a0**2+b0**2)**(0.5))
b=b0/((a0**2+b0**2)**(0.5))
c=b/2

# Now we insert the starting triangle into the list 'triangles'

A=np.array([0,0])
B=np.array([b,0])
C=np.array([b,a])
triangles = []
triangles.append([1,A,B,C])


# Now we define the subdivision rule.

def subdivide(largest):
	result = []
	for S,A,B,C in largest:
		P = A + (C-A)*(0.5*b**2)
		Q = A + (C-A)*(b**2)
		S = A + (B-A)*(0.5)
		R = A + (B-A)*(0.5) + (C-A)*(0.5*b**2)
		result += [(S*c,A,P,S),(S*c,Q,P,S),(S*c,S,R,Q),(S*c,S,R,B),(S*a,B,Q,C)]
	return result

def measure(triangles):
	labels = []
	for S,A,B,C in triangles:
		labels.append(S)
	return labels

# Now we apply the subdivision rule, in which we want to divide only the largest 
# triangles in each step

for i in xrange(m):
	sizes = measure(triangles)
	for S,A,B,C in triangles:
		if S == max(sizes):
			largest = [(S,A,B,C)]
			triangles += subdivide(largest)

# Now we draw the triangles

def DrawFigure(triangles):
    for color,A,B,C in triangles:
        vertices = [C,A,B,C]
        codes = [Path.MOVETO]+[Path.LINETO]*3
        tri = Path(vertices,codes)
        tri_patch=PathPatch(tri,facecolor='#AAAAAA',edgecolor='#000000',linewidth=0.05)
        plt.gca().add_patch(tri_patch)
    plt.show()
	
DrawFigure(triangles)