import numpy as np
import math

#training set
data = []
inp = open('train.dat')
for line in inp.readlines():
    x = line.strip().replace('\t',' ').split(' ')
    x = [1.] + x
    x = np.array([float(ele) for ele in x])
    data.append(x)
#test set
testset = []
inp = open('test.dat')
for line in inp.readlines():
    x = line.strip().replace('\t',' ').split(' ')
    x = [1.] + x
    x = np.array([float(ele) for ele in x])
    testset.append(x)

#define gradient of E
def gradE(data,w):
	return (1+math.exp(data[21]*np.dot(w,data[0:21])))**(-1)*(-data[21]*data[0:21])

	
#training
eta=0.001
Times =2000
w=np.zeros(21)
for j in range(Times):
	w=w-eta*gradE(data[j%len(data)],w)

#testing
Eout=0
for i in range(len(testset)):
	if(((1+math.exp(-np.dot(w,testset[i][0:21])))**(-1)-0.5)*testset[i][21]<0):
		Eout+=1
print float(Eout)/len(testset)