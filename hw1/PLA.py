import numpy as np
import random
def sign(n):
    if n>0:
        return 1.0
    else :
        return -1.0


data = []
inp = open('hw1_15.dat')
for line in inp.readlines():
    x = line.strip().replace('\t',' ').split(' ')
    x = [1.] + x
    x = np.array([float(ele) for ele in x])
    data.append(x)

#print data[0]
#print data[13]
"""
for i in range(len(data)):
    print data[i]

"""

leng=len(data)
seq = range(leng)
sum=0
n=5
for j in range(n):
    random.shuffle(seq)
    w = np.array([0,0,0,0,0])
    ittnum=0
    i=0
    rightnum=0
#print seq,max(seq),min(seq)

    while rightnum < leng and ittnum <= 1000 :
        if sign(np.inner(w,data[seq[i%leng]][0:5])*data[seq[i%leng]][5]) < 0 :
            #tmp = w
            w = w + 0.5*(data[seq[i%leng]][0:5]) * (data[seq[i%leng]][5])
            ittnum = ittnum + 1
            """
            print "+++++++++++++++++++++++++++++++++++++++++++++++++++++++"
            print data[i%leng]
            print tmp
            print np.inner(tmp,data[i%leng][0:4]), sign(np.inner(tmp,data[i%leng][0:4]))
            print w
            print "------------------------------------------------------"
            print rightnum
            """
            rightnum = 0
        else:
            rightnum += 1
        i += 1
    print ittnum , " j= " ,j
    print w
    sum += ittnum

print (sum/n)
#for i in range(len(data)):
#    if sign(np.inner(w,data[i][0:4])) != data[i][4] :
#        print "wx = ", sign(np.inner(w,data[i][0:4])), " y= ",data[i][4]

