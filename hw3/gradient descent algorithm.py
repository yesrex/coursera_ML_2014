import numpy as np
import math
def Eu(du,dv):
	return math.exp(du)+dv*math.exp(du*dv)+2*du-3
def Ev(du,dv):
	return 2*math.exp(dv)+du*math.exp(du*dv)-2*du+4*dv-2
def Efun(u,v):
	return math.exp(u)+math.exp(2*v)+math.exp(u*v)+u**2-2*u*v+2*+2*v**2-3*u-2*v

lp=5 										#loop of number
u=np.zeros(lp+1)
v=np.zeros(lp+1)
eta=0.01
for i in range(lp):
	u[i+1]=u[i]-eta*Eu(u[i],v[i])
	v[i+1]=v[i]-eta*Ev(u[i],v[i])


#print u[5],v[5]
print Efun(u[lp],v[lp])						#print the result after lp iteratves
