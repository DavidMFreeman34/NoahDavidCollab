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
plt.axis([-0.6,0.6,-0.6,0.6])
plt.xticks([])
plt.yticks([])
plt.axis('off')

a = 0.5*(np.sqrt(5)-1)

def subdivide(triangles):
    result = []
    for color,A,B,C in triangles:
        if color == 0:
           P = A + (B-A)*a
           result += [(0,C,P,B),(1,P,C,A)]
        else:
           Q = B+(A-B)*a
           R = B+(C-B)*a
           result +=[(1,R,C,A),(1,Q,R,B),(0,R,Q,A)]
    return result

def DrawFigure(triangles):
    for color,A,B,C in triangles:
        vertices = [C,A,B]
        codes = [Path.MOVETO]+[Path.LINETO]*2
        tri = Path(vertices,codes)
        if color == 0:
            tri_patch=PathPatch(tri,facecolor='#FF0099',edgecolor='#666666',linewidth=0.8)
        else:
            tri_patch=PathPatch(tri,facecolor='#66CCFF',edgecolor='#666666',linewidth=0.8)
        plt.gca().add_patch(tri_patch)
    # plt.show()
    plt.savefig("exports/" + os.path.basename(__file__) + ".png", format='png')

triangles = []
A=np.array([0,0])

for i in range(10):
    B = np.array([np.cos(0.2*np.pi*i),np.sin(0.2*np.pi*i)])
    C = np.array([np.cos(0.2*np.pi*(i+1)),np.sin(0.2*np.pi*(i+1))])
    if i%2 == 0:
        B , C = C, B
    triangles.append([0,A,B,C])

m = input('Enter number of divisions: ')
for j in xrange(m):
    triangles=subdivide(triangles)

DrawFigure(triangles)