'''
1. Set up x and y axis, set xticks ([pos], [labels'])
2. Read coverage file --> put it in a dictionary
3. Read identity file --> bin data 
4. Plot binned data as boxplots as placedots
5. Swarmplot function on (call it 4 times)
   move points around to avoid overlap

placed_points = []
position = 5

min_distance = ms/150

for shift in np.arrange(0, plot_area, min/distance/10): check if there are spaces on the left/right
    x_positions.append(position + shift) 
    x_positions.append(position - shift)

for yvalue in yvalues:
    if placed_points = empty:
        plot point at (position, yvalue)
    else:
        while point not plotted: or for all possible x_positions:
            distances = []
            for placed_point in placed_points:
                calculate distance to new point (position, yvalue)
                distances.append(distance)
            is min(distances) > min_distance:
                plot the point
            if not redo the whole thing with x offset
'''

import matplotlib.pyplot as plt
import matplotlib.patches as mplpatches
import numpy as np
import matplotlib
import argparse

#don't import non-standard libraries not discussed in class
#import BME163_Plot_functions_Vollmers_Christopher as Custom_plots

# -i for identity file, -c for coverage file, -q for quality file (BME263 only)  and -o
parser = argparse.ArgumentParser()
parser.add_argument('--outFile','-o' ,type=str,action='store',help='output file')
parser.add_argument('--inFile','-i' ,type=str,action='store',help='output file',default='not hello')
parser.add_argument('--inFile2','-c' ,type=str,action='store',help='output file',default='not hello')
# parser.add_argument('--inFile3','-o' ,type=str,action='store',help='output file',default='not hello')

args = parser.parse_args()

# ".ident" file: read names in the first column and identity (%) in the second column.
# ".cov" file: read names in the first column and subread coverage in the second column
outFile=args.outFile 
ident=args.inFile # identity file 
cov=args.inFile2 # coverage file
# input3=args.inFile3

print(outFile)
#absolute
plt.style.use('BME163')
print(matplotlib.get_configdir())

''' Set up panel '''
figureHeight = 2.5
figureWidth = 6

plt.figure(figsize=(figureWidth, figureHeight))

panelWidthCenter = 4.5
panelHeightCenter = 1.5

relativePanelWidthCenter = panelWidthCenter / figureWidth
relativePanelHeightCenter = panelHeightCenter / figureHeight

panelCenter = plt.axes([0.5/figureWidth, 0.15, relativePanelWidthCenter, relativePanelHeightCenter])

''' Adjust the axes limits and ticks '''
panelCenter.set_xlim(0.5, 4.5)
panelCenter.set_ylim(75, 100)

panelCenter.set_xticks([1, 2, 3, 4])
panelCenter.set_xticklabels(['1-3', '4-6', '7-9', '>=10'])

panelCenter.set_xlabel('Subread Coverage')
panelCenter.set_ylabel('Identity (%)')

''' Read coverage file and put it in a dictionary '''
dataDict = {}
with open(cov) as f:
    firstLine=f.readline()
    print(firstLine)
    for line in f:
        parts = line.strip().split() # split the cleaned line into a list called parts
        dataDict[parts[0]] = float(parts[1]) # name: number
        # print(parts[0], parts[1])

''' Read identity file and bin data '''
bins = {'1-3': [], '4-6': [], '7-9': [], '>=10': []}
with open(ident) as f:
    firstLine=f.readline()
    print(firstLine)
    for line in f:
        parts = line.strip().split() # split the cleaned line into a list called parts
        name = parts[0]
        identity = float(parts[1])
        if name in dataDict:
            coverage = dataDict[name]
            if 1 <= coverage <= 3:
                bins['1-3'].append(identity)
            elif 4 <= coverage <= 6:
                bins['4-6'].append(identity)
            elif 7 <= coverage <= 9:
                bins['7-9'].append(identity)
            elif coverage >= 10:
                bins['>=10'].append(identity)

''' Color '''
iBlue=(44/255,86/255,134/255)
iOrange=(230/255,87/255,43/255)
iYellow=(248/255,174/255,51/255)
iGreen=(32/255,100/255,113/255)

''' Function to create a swarmplot '''
colors = {
    '1-3': iBlue,
    '4-6': iGreen,
    '7-9': iYellow,
    '>=10': iOrange
}

x_positions = {'1-3': 1, '4-6': 2, '7-9': 3, '>=10': 4}

# swarmplot 
xmin = 0.5
xmax = 4.5
ymin = 75
ymax = 100
xrange = xmax - xmin
yrange = ymax - ymin
markersize = 2
minimum_distance = markersize / 72 # inches
increment = ((minimum_distance / 10) * xrange) / panelWidthCenter  # data units
span = 0.45

for bin_label in ['1-3', '4-6', '7-9', '>=10']:
    xPos = x_positions[bin_label]
    yvalues = bins[bin_label][:500]
    
    possible_positions = []
    for shift in np.arange(0, span, increment):
        possible_positions.append(xPos + shift)
        possible_positions.append(xPos - shift)

    plotted_points = []
    unplotted_points = 0

    for y1 in yvalues:

        if len(plotted_points) == 0:
            plotted_points.append((xPos, y1))
        else:
            point_plotted = False
            for x1 in possible_positions:
                distList = []
                for x2, y2 in plotted_points:
                    xdist = ((x2 - x1) / xrange) * panelWidthCenter
                    ydist = ((y2 - y1) / yrange) * panelHeightCenter
                    distance = (xdist**2 + ydist**2)**0.5
                    distList.append(distance)
                if min(distList) > minimum_distance:
                    plotted_points.append((x1, y1))
                    point_plotted = True
                    break
            if not point_plotted:
                unplotted_points += 1 
                print(f"Unplotted points for {bin_label}: {500 - len(plotted_points)}")
                break
                # break the entire for loop if you can't plot a point

    #print(f"Plotted points for {bin_label}: {len(plotted_points)}")

    for x1, y1 in plotted_points:
        panelCenter.plot(x1, y1, marker='o', ms=markersize, mew=0, linewidth=0, color=colors[bin_label])



        
# save figure

plt.savefig(outFile,dpi=1200)
  
