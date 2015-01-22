import random
import numpy as np
#define value function
def fval(x1,x2):
	if x1**2+x2**2-0.6>=0:
		return 1
	else:
		return -1

sumerr=0
exnum =100 												#number of experiments
for j in range(exnum):
	#generate random variable
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
	#linear regression
	X=(np.concatenate((np.ones((1,trnum)),trset[0:2,0:trnum]))).T
	Y=trset[2,0:trnum].T
	wlin=np.linalg.lstsq(X,Y)[0]
	#Calculate 0/1 error
	error=0
	for i in range(trnum):
		if(Y[i]*np.dot(X[i,:],wlin)<0):
			error+=1	
	sumerr+=error
print sumerr/exnum


#print  X.shape,Y.shape
#wlin.shape
#print trset[0:2,0:10]
#print np.ones((1,10))
#wlin=
#a=np.array([[1,1]])
#b=np.array([[1,2],[3,2],[2,1]])
#print b[0:3,:]
#c=append([a],[b])
#print np.ones(1,2)
#c=np.concatenate((np.ones((1,2)),b),axis=0)
#print c