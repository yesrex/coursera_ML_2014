import numpy as np
import random
def sign(n):
    if n>0:
        return 1.0
    else :
        return -1.0

data = []
inp = open('hw1_18_train.dat')
for line in inp.readlines():
    x = line.strip().replace('\t',' ').split(' ')
    x = [1.] + x
    x = np.array([float(ele) for ele in x])
    data.append(x)

testset = []
inp2 = open('hw1_18_test.dat')
for line in inp2.readlines():
    x = line.strip().replace('\t',' ').split(' ')
    x = [1.] + x
    x = np.array([float(ele) for ele in x])
    testset.append(x)
sum = 0
leng=len(data)
test_leng=len(testset)
n=2000
for j in range(n):
    w = np.array([0,0,0,0,0])
    w_hat = w
    error_hat = leng
    ittnum=0

    while  ittnum < 100 :
        i=random.randint(0,leng-1)
        if sign(np.inner(w,data[i][0:5])*data[i][5]) < 0 :
            w = w + (data[i][0:5]) * (data[i][5])
            error = 0
            for l in range(leng):
                if sign(np.inner(w,data[l][0:5])*data[l][5]) < 0:
                    error += 1
            if error < error_hat:
                w_hat = w
                error_hat=error
            ittnum = ittnum + 1
    error = 0
    for l in range(test_leng):
        if sign(np.inner(w_hat,testset[l][0:5])*testset[l][5]) < 0:
            error += 1
    
    rate = float(error)/test_leng
    #print rate
    sum += rate
ave = sum/n
print ave
    #print w_hat

#for i in range(len(data)):
#    if sign(np.inner(w,data[i][0:4])) != data[i][4] :
#        print "wx = ", sign(np.inner(w,data[i][0:4])), " y= ",data[i][4]

