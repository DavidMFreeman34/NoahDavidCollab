#-----------------------------------------

# Python + Matplotlib Penrose
# Taken from http://www.bubuko.com/infodetail-911894.html

#-----------------------------------------

import matplotlib.pyplot as plt
import matplotlib as mpl
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
q=n-m

mp.dps = 20
mp.pretty = True
f = lambda x: x**m-x**n-1
L=findroot(f,1)
l=L**(0.5)


def subdivide(triangles):
	result_final = []
	result_init1 = []
	for color,A,B,C in triangles:
		for i in xrange(m):
			if color == i:
				P = A + (C-A)*(1/l**(2*m))
				Q = B + (C-B)*(l**(n-m)/l**(n+m))
				R = A + (B-A)*(l**(-m)/l**m)
				result_init1 += [(i,A,R,P),(n+i,Q,B,R),(n+i,R,P,Q),(2*n+i,P,Q,C)]
		for color,A,B,C in result_init1:		
			for i in xrange(2*n+m):
				if color == i:
					result_init2 = [(0,A,B,C)]
					def subdivide_p(result_init2):
						result_init3 = []
						for color,A,B,C in result_init2:
							if color == m-1:
								P = A + (C-A)*(l**(0-2*m))
								result_init3 +=[(0,A,P,B),(n,B,P,C)]
							for k in xrange(m-1):
								if color == k:
									result_init3 +=[(k+1,A,B,C)]
						return result_init3
					for j in xrange(i):
						result_init2 = subdivide_p(result_init2)
					result_final += result_init2
	return result_final

cmap = mpl.cm.autumn

def DrawFigure(triangles):
    for color,A,B,C in triangles:
        vertices = [A,B,C,A]
        codes = [Path.MOVETO]+[Path.LINETO]*3
        tri = Path(vertices,codes)
        for i in xrange(m):
        	if color == i:
        		tri_patch=PathPatch(tri,facecolor=cmap(i / float(m)),edgecolor='#000000',linewidth=0.05)
        plt.gca().add_patch(tri_patch)
    plt.show()
    # plt.savefig("Pythag10-1.pdf", format='pdf')

triangles = []
A=np.array([0,0])
B=np.array([l**(-m),0])
C=np.array([l**(-m),l**q])
triangles.append([0,A,B,C])

a = input('Enter number of divisions: ')
for j in xrange(a):
	triangles=subdivide(triangles)

DrawFigure(triangles)