import numpy as np
import math
def gradE(u,v):
	gE1=math.exp(u)+v*math.exp(u*v)+2*u-2*v-3
	gE2=2*math.exp(2*v)+u*math.exp(u*v)-2*u+4*v-2
	return np.array([gE1,gE2])
def HessE(u,v):
	H11=math.exp(u)+v**2*math.exp(u*v)+2
	H12=math.exp(u*v)+v*u*math.exp(u*v)-2
	H21=H12
	H22=4*math.exp(2*v)+u**2*math.exp(u*v)+4
	return np.array([[H11,H12],[H21,H22]])
def Efun(u,v):
	return math.exp(u)+math.exp(2*v)+math.exp(u*v)+u**2-2*u*v+2*+2*v**2-3*u-2*v

lp=7											#number of iteratives
pos=np.zeros(2)								#initial position
for i in range(lp):
	pos = pos-np.dot(np.linalg.inv(HessE(pos[0],pos[1])),gradE(pos[0],pos[1]))
	#print pos
print Efun(pos[0],pos[1])





#a=np.array([[1,2],[2,3]])
#b=np.array([2,3])

#pos = pos-np.dot(np.linalg.inv(HessE(pos[0],pos[1])),gradE(pos[0],pos[1])
#print np.dot(a,b)