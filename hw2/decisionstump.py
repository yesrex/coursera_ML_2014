import numpy as np
import random
def sgn(x):
    if x>=0:
        return 1
    elif x<0:
        return -1
expnum=5000
Ein = np.array(range(expnum),dtype=np.float)
Eout = np.zeros(expnum,dtype = np.float)
for j in range(expnum):    
    x=np.random.uniform(-1,1,20)
    y=np.array(range(20))
    for i in range(20):
        y[i]=sgn(x[i])
        noise=np.random.uniform(0,1)
        if(noise<=0.2):
            y[i]=-y[i]

    eta=np.median(x)
    Ein1=0
    Ein2=0
    for i in range(20):
        if(sgn(x[i]-eta)!=y[i]):
            Ein1+=1
        else:
            Ein2+=1
    #print Ein1
    #print Ein2
    if Ein1<=Ein2:
        Ein[j]=(float(Ein1)/20)
        s=1
        #print float(Ein1)/20
        #print Ein[j]
    else:
        Ein[j]=float(Ein2)/20
        s=-1
    testx=np.random.uniform(-1,1)
    noise=np.random.uniform(0,1)
    if noise<0.2:
        testy= -sgn(testx)
    else:
        testy=  sgn(testx)
    if (s*sgn(testx-eta)!=testy):
        Eout[j] += 1

print np.mean(Ein)
print np.mean(Eout)
#print Ein


