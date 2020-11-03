import numpy as np
import matplotlib.pyplot as plt
import os

check_output = False

# Path management issues
infile_inner = 'data2_inner.txt'
infile_outer = 'data2_outer.txt'
path2folder = os.path.dirname(__file__)
path2infile_inner = os.path.join(path2folder, 'data', infile_inner)
path2infile_outer = os.path.join(path2folder, 'data', infile_outer)
points_inner = np.genfromtxt(path2infile_inner, delimiter=" ")
points_outer = np.genfromtxt(path2infile_outer, delimiter=" ")
if check_output:
    outfile = 'data8_output2.txt'
    path2outfile = os.path.join(path2folder, 'output', outfile)
    points_output = np.genfromtxt(path2outfile, delimiter=" ")

########################################################################################################################
plot_array1 = points_inner
plot_array2 = points_outer
# Plot the race track in real coordinate
fig = plt.figure(figsize=(50, 50))
ax5 = fig.add_subplot(111)
ax5.axis('equal')
# Plot Race Track boundaries
ax5.plot(plot_array1[:, 0], plot_array1[:, 1], color='r', marker='*', linewidth=10)
ax5.plot(plot_array2[:, 0], plot_array2[:, 1], color='r', marker='*', linewidth=10)
ax5.scatter(plot_array1[:, 0], plot_array1[:, 1], color='r', marker='*', linewidth=20)
ax5.scatter(plot_array2[:, 0], plot_array2[:, 1], color='r', marker='*', linewidth=20)

if check_output:
    ax5.scatter(points_output[0:20, 0], points_output[0:20, 1], color='b', marker='o', linewidth=25)
plt.show()
########################################################################################################################

