import os
import numpy as np

# Class for each point
class point():
    def __init__(self, x_coord, y_coord):
        self.x = x_coord
        self.y = y_coord

# Main Program of relative convex hull
print('The Program start here')

# Path management issues
infile_inner = 'data2_inner.txt'
infile_outer = 'data2_outer.txt'
path2folder = os.path.dirname(__file__)
path2infile_inner = os.path.join(path2folder, 'data', infile_inner)
path2infile_outer = os.path.join(path2folder, 'data', infile_outer)
points_inner = np.genfromtxt(path2infile_inner, delimiter=" ")
points_outer = np.genfromtxt(path2infile_outer, delimiter=" ")

A = list()
B = list()
for i in range(len(points_inner)):
    A.append(point(points_inner[i, 0], points_inner[i, 1]))
for i in range(len(points_outer)):
    B.append(point(points_outer[i, 0], points_outer[i, 1]))

I = list()
I0 = list()
O = list()
I00 = list()
O00 = list()
l = len(A)
t = len(B)
k = 1
j = 1
numIter = 0


def calMLP(A, B, m, n, I, O):



def RCH(A, B, I00, O00, I0, l, t, k, j, numIter):
    print('Call RCH function')
    calMLP()

















