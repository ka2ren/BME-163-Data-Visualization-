'''
1. Set up your figure at right dimensions.
    Figure size: 3'' wide and 3'' high.

2. Make panels at right size and position.
    Main Panels 1.5'' wide and 1.5'' high.
    Left Panel: 0.25'' wide and 1.5'' high
    Top Panels: 1.5'' wide and 0.25'' high

3. Read the data from the file.
4. Plot (using plot function) the data.
5. Log convert the data.
6. Set xrange and yrange.
7. Make the center plot look like the template.
8. Make the top histogram.
9. Think about how to adjust the histogram code for left histogram.
'''


import matplotlib.pyplot as plt
import matplotlib.patches as mplpatches
import numpy as np
import matplotlib
import argparse
#matplotlib.use('Agg')
parser = argparse.ArgumentParser()
parser.add_argument('--outFile','-o' ,type=str,action='store',help='output file')
parser.add_argument('--inFile', '-i', type=str, action='store', help='input file', default='BME163_Input_Data_1.txt')

args = parser.parse_args()

outFile = args.outFile
inputFile = args.inFile

plt.style.use('BME163')

''' Set up figure (3 x 3) '''

figureWidth = 3
figureHeight = 3

plt.figure(figsize = (figureWidth, figureHeight))

''' Set up 2 histogram panels and 1 scatter plot panel '''

panelLeft1 = 0.7 / figureHeight # Main panel
panelBottom1 = 0.3 / figureWidth

panelLeft2 = 0.38 / figureWidth # Left panel
panelBottom2 = 0.3 / figureWidth

panelLeft3 = 0.7 / figureWidth # Top panel
panelBottom3 = 1.87 / figureHeight

mainPanelWidth = 1.5 / figureWidth
mainPanelHeight = 1.5 / figureHeight

leftHistWidth = 0.25 / figureWidth
leftHistHeight = 1.5 / figureHeight

topHistWidth = 1.5 / figureWidth
topHistHeight = 0.25 / figureHeight

# ax = plt.axes([left, bottom, width, height])
mainPanel = plt.axes([panelLeft1, 
                      panelBottom1, 
                      mainPanelWidth, 
                      mainPanelHeight])
leftPanel = plt.axes([panelLeft2, 
                      panelBottom2, 
                      leftHistWidth, 
                      mainPanelHeight])
topPanel = plt.axes([panelLeft3, 
                     panelBottom3, 
                     mainPanelWidth, 
                     topHistHeight])

''' Read the data from the file '''

# Open text file.
#test = open('BME163_Input_Data_1.txt','w') 

xvalues = []
yvalues = []

for line in open(inputFile): 
    # Read the input file line by line.
    splitLine = line.strip().split('\t')

    xvalues.append(float(splitLine[1]))
    yvalues.append(float(splitLine[2]))

#test.close() # Closes the temporary output file.

''' Log convert '''

xArray = np.array(xvalues)
logxArray = np.log2(xArray + 1)

yArray = np.array(yvalues)
logyArray = np.log2(yArray + 1)

''' Plot scatter in the main panel '''

mainPanel.plot(logxArray, logyArray,
            marker='o',
            markeredgewidth=0,
            markerfacecolor=(88/255,85/255,120/255),
            color=(88/255,85/255,120/255),
            linestyle='None',
            markersize=3,
            zorder=5,
            alpha=0.1
)

''' Plot histogram on the left panel '''

bins = np.arange(0, 15, 0.5)
yHisto, bins = np.histogram(logyArray, bins=bins)

for i in range(len(yHisto)):
    left = 0
    bottom = bins[i]
    width = np.log2(yHisto[i] + 1)
    height = bins[i+1] - bins[i]

    rectangle1 = mplpatches.Rectangle((left,bottom),width,height,
                                facecolor='grey',
                                linewidth=0.3,
                                edgecolor='black',)
    leftPanel.add_patch(rectangle1)

''' Plot histogram on the top panel '''

bins = np.arange(0, 15, 0.5)
xHisto,bins=np.histogram(logxArray, bins=bins)

for i in range(0,len(xHisto),1):
    left = bins[i]
    bottom = 0
    width = bins[i+1] - left
    height = np.log2(xHisto[i] + 1)

    rectangle1=mplpatches.Rectangle((left,bottom),width,height,
                                facecolor=(120/255,172/255,145/255),
                                linewidth=0.3,
                                edgecolor='black',

    )
    topPanel.add_patch(rectangle1)

''' Adjust panel axes '''

mainPanel.set_xlim(0, 15)
mainPanel.set_ylim(0, 15)

mainPanel.set_xticks(range(0, 16, 5))
mainPanel.set_yticks([])

leftPanel.set_xlim(20, 0)
leftPanel.set_ylim(0, 15)

leftPanel.set_xticks([20, 0])
leftPanel.set_yticks(range(0, 16, 5))

topPanel.set_xlim(0, 15)
topPanel.set_ylim(0, 20)

topPanel.set_xticks([])
topPanel.set_yticks([0, 20])

''' Save figure '''

plt.savefig(outFile,dpi=600)
