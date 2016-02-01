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
from decimal import Decimal

plt.figure(figsize=(1.4,1.4),dpi=500)
plt.subplot(aspect='equal')
plt.axis([0,1,0,0.8])
plt.xticks([])
plt.yticks([])
plt.axis('off')

print "Pinwheel(p,q) Tiling"
p = input('Enter the value of p: ')
q = input('Enter the value of q: ')
m = input('Enter number of divisions: ')
r = max(p,q)


# Now we calculate the proportions of the triangles based on (p,q). The number b provides
# the base of a triangle, and the number a provides the height. The hypotenuse equals 1.

mp.dps = 10
mp.pretty = True
f = lambda x: (0.5**p)*(1-x**2)**(0.5*p)-x**q
a=findroot(f,0.5)
b=(1-a**2)**(0.5)
# a=a0/((a0**2+b0**2)**(0.5))
# b=b0/((a0**2+b0**2)**(0.5))
c=b/2

# Now we insert the starting triangle into the list 'triangles'

A=np.array([0,0])
B=np.array([b,0])
C=np.array([b,a])
triangles = [(1,A,B,C)]

# Now we insert the size of the hypotenuse of the starting triangle into the list 'sizes'

sizes = [1]

# Now we define the subdivision rule.

def subdivide(largest):
	result = []
	for size,A,B,C in largest:
		P = A + (C-A)*(0.5*b**2)
		Q = A + (C-A)*(b**2)
		S = A + (B-A)*(0.5)
		R = A + (B-A)*(0.5) + (C-A)*(0.5*b**2)
		result += [(size*c,A,P,S),(size*c,Q,P,S),(size*c,S,R,Q),(size*c,S,R,B),(size*a,B,Q,C)]
	return result

# Now we apply the subdivision rule. Note the need for a bit of rounding!

for i in xrange(m):
	n = max(sizes)
	for size,A,B,C in triangles:
		if round(size,5) == round(n,5):
			largest = [(size,A,B,C)]
			triangles += subdivide(largest)
			sizes += [size*c,size*a]
	sizes = list(set(sizes))
	sizes = [x for x in sizes if round(x,5) != round(n,5)]

# Now we clean up the sizes list in order to color the tiling

sizes.sort()
final_sizes = []
for i in xrange(r):
	if sizes:
		final_sizes += [sizes[0]]
		sizes = [x for x in sizes if round(x,5) != round(sizes[0],5)]

# Now we set the color scheme and draw the triangles

cmap = mpl.cm.autumn

def DrawFigure(triangles):
    for size,A,B,C in triangles:
        vertices = [C,A,B,C]
        codes = [Path.MOVETO]+[Path.LINETO]*3
        tri = Path(vertices,codes)
        for i in xrange(len(final_sizes)):
        	if round(size,5) == round(final_sizes[i],5):
        		tri_patch=PathPatch(tri,facecolor=cmap(i/float(r)),edgecolor='#000000',joinstyle='round',linewidth=0.1)
        		plt.gca().add_patch(tri_patch)
    plt.show()

DrawFigure(triangles)
