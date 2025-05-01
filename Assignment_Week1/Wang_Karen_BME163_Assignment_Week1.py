import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import argparse
import matplotlib

matplotlib.use('Agg')

parser = argparse.ArgumentParser()

parser.add_argument('--outFile','-o' ,type=str,action='store',help='output file')
args = parser.parse_args()

outFile=args.outFile

print(outFile)
print(matplotlib.get_configdir())
# Use the BME163 style sheet
plt.style.use('BME163')

# Set up figure
figureWidth = 5
figureHeight = 2
plt.figure(figsize=(figureWidth, figureHeight))

# Set up panel
panelLeft = 0.2
panelBottom = 0.2
panelWidth = 2
panelHeight = 1

left_panel = plt.axes([panelLeft/figureWidth, panelBottom/figureHeight, panelWidth/figureWidth, panelHeight/figureHeight])
left_panel.set_xlim(0, 101)
left_panel.set_ylim(0, 200)
left_panel.set_xticks([])
left_panel.set_yticks([])

# Viridis colormap anchor colors (from left to right)
viridis1 = (68/255,  1/255,   84/255)
viridis2 = (59/255,  82/255, 139/255)
viridis3 = (33/255, 145/255, 140/255)
viridis4 = (94/255, 201/255,  98/255)
viridis5 = (253/255,231/255,  37/255)

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

# Draw 101 vertical rectangles (each 1 unit wide) covering y = 100 to 200
for i in range(101):
    rect = patches.Rectangle((i, 100), 1, 100, facecolor=viridis_colors[i], edgecolor='none')
    left_panel.add_patch(rect)

# Plasma colormap anchor colors for diagonal line:
plasma1 = (15/255,   0/255, 118/255)
plasma2 = (87/255,   0/255, 151/255)
plasma3 = (190/255, 48/255, 101/255)
plasma4 = (245/255,135/255,  48/255)
plasma5 = (237/255,252/255,  27/255)

pr1 = np.linspace(plasma1[0], plasma2[0], 26)
pr2 = np.linspace(plasma2[0], plasma3[0], 26)
pr3 = np.linspace(plasma3[0], plasma4[0], 26)
pr4 = np.linspace(plasma4[0], plasma5[0], 26)
P_R = np.concatenate([pr1, pr2[1:], pr3[1:], pr4[1:]])

pg1 = np.linspace(plasma1[1], plasma2[1], 26)
pg2 = np.linspace(plasma2[1], plasma3[1], 26)
pg3 = np.linspace(plasma3[1], plasma4[1], 26)
pg4 = np.linspace(plasma4[1], plasma5[1], 26)
P_G = np.concatenate([pg1, pg2[1:], pg3[1:], pg4[1:]])

pb1 = np.linspace(plasma1[2], plasma2[2], 26)
pb2 = np.linspace(plasma2[2], plasma3[2], 26)
pb3 = np.linspace(plasma3[2], plasma4[2], 26)
pb4 = np.linspace(plasma4[2], plasma5[2], 26)
P_B = np.concatenate([pb1, pb2[1:], pb3[1:], pb4[1:]])

plasma_colors = [(P_R[i], P_G[i], P_B[i]) for i in range(101)]

# Plot the diagonal line
for i in range(101):
    left_panel.plot(
        i,i,  # x and y are the same, forming a diagonal line
        marker='o',
        markeredgewidth=0,
        markerfacecolor=plasma_colors[i],
        color='black',
        linewidth=1,
        linestyle='--',
        markersize=4,
        zorder=0
    )

# Add a horizontal black line at y = 100 to separate the upper and bottom panels.
left_panel.axhline(y=100, color='black', linewidth=1)

plt.savefig(outFile, dpi=600)

