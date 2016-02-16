#-----------------------------------------

# Python + matplotlib + numpy + mpmath
# Created by David Freeman (2016) with consultation from Noah Weaver
# Modified from http://www.bubuko.com/infodetail-911894.html

#-----------------------------------------

import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
from matplotlib.path import Path
from matplotlib.collections import PolyCollection
from mpmath import *

plt.figure(figsize=(1,0.6),dpi=800)
plt.subplot(aspect='equal')
plt.axis([0,1,0,1])
plt.xticks([])
plt.yticks([])
plt.axis('off')

print "Pinwheel(p,q) Tiling"
p = input('Enter the value of p: ')
q = input('Enter the value of q: ')
m = input('Enter number of divisions: ')
r = max(p,q)
filename = 'pinwheel(%s,%s,%s)_summer.png' %(p,q,m)

# Now we calculate the proportions of the triangles based on (p,q). The number b provides
# the base of a triangle, and the number a provides the height. The hypotenuse equals 1.

mp.dps = 10
mp.pretty = True
f = lambda x: (0.5**p)*(1-x**2)**(0.5*p)-x**q
a=findroot(f,0.5)
b=(1-a**2)**(0.5)
c=b/2

# Now we insert the starting triangle into the list 'triangles'
print('insert the starting triangle into the list of triangles')
A=np.array([0,0])
B=np.array([b,0])
C=np.array([b,a])
D=np.array([0,a])
triangles = [(1,A,B,C),(1,C,D,A)]

# Now we insert the size of the hypotenuse of the starting triangle into the list 'sizes'

sizes = [1]

# Now we define the subdivision rule.

def subdivide(largest):
	result=[]
	for size,A,B,C in largest:
		P = A + (C-A)*(0.5*b**2)
		Q = A + (C-A)*(b**2)
		S = A + (B-A)*(0.5)
		R = A + (B-A)*(0.5) + (C-A)*(0.5*b**2)
		result.extend([(size*c,A,P,S),(size*c,Q,P,S),(size*c,S,R,Q),(size*c,S,R,B),(size*a,B,Q,C)])
	return result

# Now we apply the subdivision rule. Note the need for a bit of rounding!

for i in xrange(m):
	n = max(sizes)
	largest = [(size,A,B,C) for (size,A,B,C) in triangles if round(size,5) == round(n,5)]
	triangles.extend(subdivide(largest))
	triangles = [(size,A,B,C) for (size,A,B,C) in triangles if round(size,5) != round(n,5)]
	sizes.extend([n*c,n*a])
	sizes = [x for x in sizes if round(x,5) != round(n,5)]

# Now we clean up the sizes list in order to color the tiling

sizes.sort()
final_sizes = []
for i in xrange(r):
	if sizes:
		final_sizes.extend([sizes[0]])
		sizes = [x for x in sizes if round(x,5) != round(sizes[0],5)]

# Now we set the color scheme and draw the triangles

cmap = mpl.cm.summer

def approx_equal(a, b):
     return abs(a - b) <= max(abs(a),abs(b))*(1e-5)

def DrawFigure(triangles):
	for i in xrange(len(final_sizes)):
		print('current ' + str(i))
		current = [(A,B,C) for (size,A,B,C) in triangles if approx_equal(size,final_sizes[i])]
		plt.gca().add_collection(PolyCollection(current,facecolor=cmap(i/float(r)),edgecolor='none'))
	plt.savefig(filename, dpi=3600, format='png')
	#plt.show()

DrawFigure(triangles)
