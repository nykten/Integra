import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.colors as mcolors
from matplotlib.cm import ScalarMappable
import numpy as np
import os
import sys

file_path_default = sys.argv[1]

file_path = os.path.join(file_path_default, "stimulus_results.txt")

data = []

with open(file_path, 'r') as file:
    for i,line in enumerate(file):
        if i==0:
            continue
        fields = line.strip().split(',')
        fields[1], fields[3] = fields[1].strip('('), fields[3].strip(' )')
        del fields[2]
        data.append(fields)

invalid_counts = {}


for index, x, y, seen_stimulus, time_since_test_start, reaction_time, was_looking_at_centre in data:
    if was_looking_at_centre == 'False' and seen_stimulus == 'True':
        key = (float(x), float(y))
        if key not in invalid_counts:
            invalid_counts[key] = 0
        invalid_counts[key] += 1


x_vals, y_vals, colors = [], [], []

for (x, y), count in invalid_counts.items():
    x_vals.append(x)
    y_vals.append(y)
    if count == 3:
        colors.append('red')
    elif count == 2:
        colors.append('orange')
    elif count == 1:
        colors.append('yellow')



count_to_numeric = {'yellow': 1, 'orange': 2, 'red': 3}
numeric_counts = [count_to_numeric[color] for color in colors]

cmap = mcolors.ListedColormap(['yellow', 'orange', 'red'])
bounds = [0.5, 1.5, 2.5, 3.5]
norm = mcolors.BoundaryNorm(bounds, cmap.N)

plt.figure(figsize=(8, 6))

scatter = plt.scatter(x_vals, y_vals, c=numeric_counts, cmap=cmap, norm=norm, s=50, marker='o', edgecolor='none')

cbar = plt.colorbar(ScalarMappable(norm=norm, cmap=cmap), ticks=[1, 2, 3])
cbar.ax.set_yticklabels(['1 Invalid Entry', '2 Invalid Entries', '3 Invalid Entries'])

plt.axhline(y=0, color='black', linewidth=1)
plt.axvline(x=0, color='black', linewidth=1)
plt.title('Graph Showcasing Invalid Stimulus Entries by Count')
plt.xlabel('X Coordinate')
plt.ylabel('Y Coordinate')
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
caption_text = "Displays count of invalid entries: User responses when test rules were not followed"
plt.figtext(0.5, 0.01, caption_text, wrap=True, horizontalalignment='center', fontsize=10)

output_dir_path = os.path.join(os.path.dirname(file_path_default), "processed")
output_file_path = os.path.join(output_dir_path, "invalid.png")

plt.savefig(output_file_path, dpi=300)

plt.close()
