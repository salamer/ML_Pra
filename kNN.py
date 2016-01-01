'''
author:aljun
date:20160101
from:<machine learnning in action> chapter 2

'''


from numpy import *

import operator

def createDataSet():
	group=array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
	labels=['A','A','B','B']

	return group,labels

def classify0(inX,dataSet,labels,k):
	dataSetSize=dataSet.shape[0]
	diffMat=tile(inX,(dataSetSize,1))-dataSet
	sqDiffMat=diffMat**2
	sqDistances=sqDiffMat.sum(axis=1)
	distances=sqDistances**0.5
	sortedDistIndicies=distances.argsort()
	classCount={}
	for i in range(k):
		voteIlabel=labels[sortedDistIndicies[i]]
		classCount[voteIlabel]=classCount.get(voteIlabel,0)+1

	sortedClassCount=sorted(classCount.iteritems(),key=operator.itemgetter(1),reverse=True)
	return sortedClassCount[0][0]

def file2matrix(filename):
	fr=open(filename)
	arrayOLines=fr.readlines()
	numerOfLines=len(arrayOLines)
	returnMat=zeros((numberOfLines,3))
	classLabelVector=[]
	index=0
	for line in arrayOLines:
		line=line.strip()
		listFromLine=line.split('\t')
		returnMat[index,:]=listFromLine[0:3]
		classLabelVector.append(int(listFromLine[-1]))
		index+=1

	return returnMat,classLabelVector

def autoNorm(dataSet):
	minVals=dataSet.min(0)
	maxVals=dataSet.max(0)
	ranges=maxVals-minVals
	normDataSet=zeros(shape(dataSet))
	m=dataSet.shape[0]
	normDataSet=dataSet-tile(minVals,(m,1))
	normDataSet=normDataSet/tile(ranges,(m,1))
	return normDataSet,ranges,minVals



'''
手写系统

'''

def img2vector(filename):
	returnVect=zeros((1,1024))
	fr=open(filename)
	for i in range(32):
		lineStr=fr.readline()
		for j in range(32):
			returnVect[0,32*i+j]=int(lineStr[j])
	return returnVect



def handwritingClasstest():
	hwLabels=[]
	trainingFileList=listdir('trainingDigits')
	m=len(trainingFileList)
	tariningMat=zeros((m,1024))
	for i in range(m):
		fileNameStr=trainingFileList[i]
		fileStr=fileNameStr.split('.')[0]
		classNumber=int(fileStr.split('_')[0])
		hwLabels.append(classNumber)
		tariningMat[i,:]=img2vector('trainingDigits/%s' % fileNameStr)
	testFileList=listdir('testDigits')
	errorCount=0.0
	mTest=len(testFileList)
	for i in range(mTest):
		fileNameStr=testFileList[i]
		fileStr=fileNameStr.split('.')[0]
		classNumberStr=int(fileStr.split('_')[0])
		vectorUnderTest=img2vector('testDigits/%s'%fileNameStr)
		classifierResult=classify0(vectorUnderTest,tariningMat,hwLabels,3)
		print "real answer is %d" % (classifierResult,classNumStr)
		if(classifierResult!=classNumStr):
			errorCount+=1.0
	print "error is %s"%errorCount








