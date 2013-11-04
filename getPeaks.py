import numpy as np
from numpy import diff
from matplotlib import pyplot
import tkFileDialog
def getPeaks(inputFile, outputFile1, outputFile2):

	thRatio = 3.0
	#topMaxDistNum = 5.0

	rawdata= np.loadtxt(inputFile)
	data = rawdata[:, 1]
	#print data.shape, diff(data).shape
	threshold = np.amax(data, 0)/thRatio

	a = diff(np.sign(diff(data))).nonzero()[0] + 1 # local min+max
	minPos = (diff(np.sign(diff(data))) > 0).nonzero()[0] + 1 # local min
	minVal = data[minPos]
	maxPos = (diff(np.sign(diff(data))) < 0).nonzero()[0] + 1 # local max
	aboveTH = data > threshold
	aboveTHVal = data[aboveTH.nonzero()]
	finalMaxPos = np.logical_and(diff(np.sign(diff(data))) < 0, aboveTH[1:-1]).nonzero()[0] + 1
	## calculate background
	#distBetweenMax = diff(finalMaxPos)
	#print distBetweenMax
	#distBetweenMaxSorted = np.sort(distBetweenMax, axis = 0)
	#distTop = distBetweenMaxSorted[-topMaxDistNum:]
	#print distTop
	#bgMean = []
	#for i in np.arange(topMaxDistNum):
	#	#bgMean.append(np.average(data[distTop[i]:]))
	#	print list(distBetweenMax).index(distTop[i])
	#print 
	### end calculate background
	#print maxPos
	#overThPos = (data > threshold).nonzero()	
	#print overThPos
	# cal overlay
	#finalMaxPos = [ [val in overThPos for val in iterMaxPos] for iterMaxPos in maxPos]
	#finalMaxPos = [any (value in item for value in overThPos) for item in maxPos]
	maxVal0 = data[maxPos]
	maxVal = data[finalMaxPos]
    
    # PLOT DATA
	pyplot.plot(data)
	pyplot.plot(threshold*np.ones((data.size,1)),'--')
	pyplot.scatter(finalMaxPos, maxVal, color='red')
	#pyplot.scatter(maxPos, maxVal0, color='red')
	#pyplot.scatter(aboveTH.nonzero(), aboveTHVal, color = 'green')
	pyplot.show()

	## SAVE RESULT
	#output = np.vstack([finalMaxPos.transpose(), maxVal.transpose()])
	#np.savetxt(outputFile1, (finalMaxPos.transpose(), maxVal.transpose()), fmt='%.2e', delimiter = ',',newline='\n')
	np.savetxt(outputFile1, finalMaxPos, fmt='%.2e', delimiter = ',',newline='\n')
	np.savetxt(outputFile2, maxVal, fmt='%.2e', delimiter = ',',newline='\n')

if __name__ == "__main__":
    
    #inputFile = 'data2.txt'  #
    inputFile = tkFileDialog.askopenfilename()
    #print 'Please input your file name (txt): \n'
    #inputFile = raw_input() + '.txt'
    outputFile1 = inputFile[:-4] + '_rzltX.txt'
    outputFile2 = inputFile[:-4] + '_rzltY.txt'

    getPeaks(inputFile, outputFile1, outputFile2)
