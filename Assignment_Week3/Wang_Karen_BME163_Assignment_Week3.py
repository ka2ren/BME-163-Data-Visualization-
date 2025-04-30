
import matplotlib.pyplot as plt
import matplotlib.patches as mplpatches
import numpy as np
import matplotlib
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--outFile','-o' ,type=str,action='store',help='output file')
parser.add_argument('--inFile','-p' ,type=str,action='store',help='output file',default='not hello')
parser.add_argument('--inFile2','-c' ,type=str,action='store',help='output file',default='not hello')
# parser.add_argument('--inFile3','-i3' ,type=str,action='store',help='output file',default='not hello') for BME 263

args = parser.parse_args()

outFile=args.outFile
input=args.inFile
input2=args.inFile2
# input3=args.inFile3 for BME 263

plt.style.use('BME163')
print(matplotlib.get_configdir())

''' Set up figure '''
figureWidth = 5
figureHeight = 3

plt.figure(figsize=(figureWidth, figureHeight))

''' Set up panels '''
panelWidth = 1.5
panelHeight = 1.5

relativePanelWidth = panelWidth / figureWidth
relativePanelHeight = panelHeight / figureHeight

panel1 = plt.axes([0.5/figureWidth, 0.5/figureHeight, relativePanelWidth, relativePanelHeight])
panel2 = plt.axes([2.5/figureWidth, 0.5/figureHeight, relativePanelWidth, relativePanelHeight])
panel3 = plt.axes([4.0/figureWidth, 1.1/figureHeight, 0.1/figureWidth, 0.3/figureHeight])

'''Set up color dictionary for panel1 '''
greenish=(120/255, 172/255, 145/255)
grey=(180/255, 180/255, 180/255)
darkblue=(87/255, 84/255, 120/255)

celltype_colors = {
    "tCell": greenish,
    "monocyte": grey,
    "bCell": darkblue,
}

''' Read cell-type data '''
celltypeDict = {}
with open(input2) as f: # input2 is the path to celltype.tsv
    firstLine = f.readline()
    print(firstLine)
    for line in f:
        number, celltype, name = line.strip().split()
        celltypeDict[name] = celltype

''' Read position data '''
xvalues = []
yvalues = []
colors = []

for line in open(input): # input is the path to position.tsv
    name, xvalue, yvalue = line.strip().split()
    xvalue = float(xvalue)
    yvalue = float(yvalue)
    celltype = celltypeDict[name]
    xvalues.append(xvalue)
    yvalues.append(yvalue)
    colors.append(celltype_colors.get(celltype, 'black')) # Default to black if celltype not in dictionary

''' Plot data for panel1 '''
panel1.scatter(xvalues, yvalues, c=colors, s=16, edgecolors='black', linewidth=0.1, alpha=1)

from matplotlib.patheffects import withStroke  # Import path effects for text styling

''' Calculate and add cell type names to the plot for panel1 '''
for celltype in set(celltypeDict.values()):  # Iterate over unique cell types
    # Get all x and y values for the current cell type
    x_positions = [xvalues[i] for i in range(len(xvalues)) if celltypeDict[list(celltypeDict.keys())[i]] == celltype]
    y_positions = [yvalues[i] for i in range(len(yvalues)) if celltypeDict[list(celltypeDict.keys())[i]] == celltype]
    
    # Calculate the median x and y positions
    x_median = sorted(x_positions)[len(x_positions) // 2]
    y_median = sorted(y_positions)[len(y_positions) // 2]
    
    # Add the cell type name to the plot with white edges
    text = panel1.text(x_median, y_median, celltype, fontsize=8, ha='center', va='center', zorder=10)
    text.set_path_effects([withStroke(linewidth=1, foreground='white')])  # Add white stroke

''' Color map for panel2'''
# Viridis colormap anchor colors (from left to right)
viridis1 = (68/255, 1/255, 84/255)
viridis2 = (59/255, 82/255, 139/255)
viridis3 = (33/255, 145/255, 140/255)
viridis4 = (94/255, 201/255, 98/255)
viridis5 = (253/255, 231/255, 37/255)

# Generate the viridis colormap
vr1 = np.linspace(viridis1[0], viridis2[0], 26)
vr2 = np.linspace(viridis2[0], viridis3[0], 26)
vr3 = np.linspace(viridis3[0], viridis4[0], 26)
vr4 = np.linspace(viridis4[0], viridis5[0], 26)
V_R = np.concatenate([vr1, vr2[1:], vr3[1:], vr4[1:]])
vg1 = np.linspace(viridis1[1], viridis2[1], 26)
vg2 = np.linspace(viridis2[1], viridis3[1], 26)
vg3 = np.linspace(viridis3[1], viridis4[1], 26)
vg4 = np.linspace(viridis4[1], viridis5[1], 26)
V_G = np.concatenate([vg1, vg2[1:], vg3[1:], vg4[1:]])
vb1 = np.linspace(viridis1[2], viridis2[2], 26)
vb2 = np.linspace(viridis2[2], viridis3[2], 26)
vb3 = np.linspace(viridis3[2], viridis4[2], 26)
vb4 = np.linspace(viridis4[2], viridis5[2], 26)
V_B = np.concatenate([vb1, vb2[1:], vb3[1:], vb4[1:]])
# Create a list of 101 viridis colors
viridis_colors = [(V_R[i], V_G[i], V_B[i]) for i in range(101)]


''' Calculate distances and assign colors for panel2 '''
distance_threshold = 5 / 45.3  # Diameter of the point in inches that are overlapping
counts = []
# Panel dimensions and ranges
xrange = panel1.get_xlim()[1] - panel1.get_xlim()[0]
yrange = panel1.get_ylim()[1] - panel1.get_ylim()[0]

# Calculate how many points are close to each point
for i in range(len(xvalues)):
    count = 0
    for j in range(len(xvalues)):
        if i != j:
            # Calculate scaled distances in panel dimensions
            xdist = ((xvalues[i] - xvalues[j]) / xrange) * panelWidth
            ydist = ((yvalues[i] - yvalues[j]) / yrange) * panelHeight
            distance = (xdist**2 + ydist**2)**0.5  # Euclidean distance in inches

            # Check if the distance is within the threshold
            if distance <= distance_threshold:
                count += 1
    counts.append(min(count, 100))  # Cap the count at 100

# Map counts to colors using the viridis colormap
colors_panel2 = [viridis_colors[count] for count in counts]

''' Plot data for panel2 '''
panel2.scatter(xvalues, yvalues, c=colors_panel2, s=14, edgecolors=None, linewidth=0.2, alpha=1)

''' Add text to Panel 2 '''
panel2.text(-28, -37.5, 'Density', fontsize=8, ha='left', va='bottom', zorder=10)

''' Show color gradient on Panel 3 '''
# Create a gradient for the viridis colormap
gradient = np.linspace(0, 1, 101).reshape(101, 1)  # Gradient from 0 to 1
panel3.imshow(gradient, aspect='auto', cmap=matplotlib.colors.ListedColormap(viridis_colors),
              extent=[0, 1, 0, 1], origin='lower')  # Ensure the gradient starts from Min (dark) to Max (light)

''' Adjust panel axes '''
panel1.set_xlim(-30, 30)
panel1.set_ylim(-40, 30)

panel2.set_xlim(-30, 30)
panel2.set_ylim(-40, 30)

''' Adjust panel 3 axes '''
panel3.set_ylim(0, 1)  # Set the y-axis range for panel3
panel3.set_yticks([0, 1])  # Set ticks at the min (0) and max (1)
panel3.set_yticklabels(["Min", "Max"])  # Set custom labels for the ticks
panel3.yaxis.tick_right()  # Move the y-axis ticks to the right side
panel3.set_xticks([])  # Remove x-axis ticks for panel3
panel3.set_xticklabels([])  # Remove x-axis labels for panel3

panel1.set_xticks([-20, 0, 20])
panel1.set_yticks([-40, -20, 0, 20])

panel2.set_xticks([-20, 0, 20])
panel2.set_yticks([-40, -20, 0, 20])

panel1.set_xlabel('tSNE 2')
panel1.set_ylabel('tSNE 1')

panel2.set_xlabel('tSNE 2')
panel2.set_ylabel('tSNE 1')

''' Save figure '''
plt.savefig(outFile, dpi=600)

