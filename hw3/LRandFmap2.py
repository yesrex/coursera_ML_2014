import random
import numpy as np
#define value function
def fval(x1,x2):
	if x1**2+x2**2-0.6>=0:
		return 1
	else:
		return -1

#generate train set
trnum=1000											#number of traing set
trset=np.zeros([3,trnum])
for i in range(trnum):
	trset[0,i]=random.uniform(-1,1)
	trset[1,i]=random.uniform(-1,1)
	err=random.uniform(0,1)
	if err<0.1:
		trset[2,i]=-fval(trset[0,i],trset[1,i])
	else:
		trset[2,i]=fval(trset[0,i],trset[1,i])
# linear regression
X=np.ones((trnum,6))
X[:,1]=trset[0,:]
X[:,2]=trset[1,:]
X[:,3]=trset[0,:]*trset[1,:]
X[:,4]=trset[0,:]**2
X[:,5]=trset[1,:]**2
Y=trset[2,0:trnum].T
wlin=np.linalg.lstsq(X,Y)[0]

#generate test set
testnum=1000										#numbers of  average
testset=np.zeros([3,trnum])
for i in range(trnum):
	testset[0,i]=random.uniform(-1,1)
	testset[1,i]=random.uniform(-1,1)
	err=random.uniform(0,1)
	if err<0.1:
		testset[2,i]=-fval(testset[0,i],testset[1,i])
	else:
		testset[2,i]=fval(testset[0,i],testset[1,i])
#measure test error
Eout=0
for j in range(testnum):
	x=np.array([1,testset[0,j],testset[1,j],testset[0,j]*testset[1,j],testset[0,j]**2,testset[1,j]**2])
	if(testset[2,j]*(np.dot(wlin,x))<0):
		Eout=Eout+1
print Eout,float(Eout)/testnum		