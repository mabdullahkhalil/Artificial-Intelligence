
import numpy as np
import time

def sigmoid_Function(x, deriv=False):  
    if (deriv == True):
        return (x * (1 - x))

    return 1 / (1 + np.exp(-x))  



# loading files into vectors
mainouttest=[]
with open('test-labels.txt') as f:
    for line in f:
        taken=int(line)
        vec=[]
        for i in range(0,10):
            if i==taken:
                vec.append(1)
            else:
                vec.append(0)

        mainouttest.append(vec)

q=0
maininptest=[]
with open('test.txt') as f:
    polyShape = []
    for line in f:
        line = line.split() 

        for i in range(0,len(line)):
            if line[i] == "]" or line[i] == "[":
                continue
            elif line[i][len(line[i])-1]=="]":
                x=line[i][:-1]
                print q
                q=q+1
                polyShape.append(int(x))
                maininptest.append(polyShape)
                polyShape=[]
                break
            else:
                polyShape.append(int(line[i]))


mainout=[]
with open('train-labels.txt') as f:
    for line in f:

        taken=int(line)
        vec=[]
        for i in range(0,10):
            if i==taken:
                vec.append(1)
            else:
                vec.append(0)

        mainout.append(vec)

q=0;
maininp=[]
with open('train.txt') as f:
    polyShape = []
    for line in f:
        line = line.split() 
        for i in range(0,len(line)):
            if line[i] == "]" or line[i] == "[":
                continue
            elif line[i][len(line[i])-1]=="]":
                x=line[i][:-1]
                print q
                q=q+1
                polyShape.append(int(x))
                maininp.append(polyShape)
                polyShape=[]
                break
            else:
                polyShape.append(int(line[i]))

np.random.seed(1)


starttime=time.time()

#introducing weights
syn0 = 2 * np.random.random((784,30)) - 1         # creating a 784x30 array showing 784 inputs and 30 hidden layer
syn1 = 2 * np.random.random((30,10)) - 1          # creating a 30x10 array showing 30 hidden and 10 output

for z in xrange(0,2):
    for i in xrange(0,len(maininp)):
        X = np.array([maininp[i]])/float(255)     # normalising the input data
        y = np.array([mainout[i]])


        # forward feed
        l0 = X
        l1 = sigmoid_Function(np.dot(l0, syn0))
        l2 = sigmoid_Function(np.dot(l1, syn1))


        # back propagation
        l2_error = y - l2

        l2_delta = l2_error * sigmoid_Function(l2, deriv=True)

        l1_error=np.dot(l2_delta,syn1.T)

        l1_delta = l1_error * sigmoid_Function(l1, deriv=True)


        # updating the weights
        syn1 += (np.dot(l1.T,l2_delta))*0.7
        syn0 += (np.dot(l0.T, l1_delta))*0.7

    arr=np.array(l2)
    arr=arr.tolist()


    print("Output after test")
    print(arr[0].index(max(arr[0])))


endtime=time.time()

# computing the expected value of testing data
file=open('finalresult(0.7).txt','w')
for i in xrange(0,len(maininptest)):
    X = np.array([maininptest[i]])/float(255)

    l0 = X
    l1 = sigmoid_Function(np.dot(l0, syn0))
    l2 = sigmoid_Function(np.dot(l1, syn1))



    print("Output after train")
    arr=np.array(l2)
    arr=arr.tolist()
    print(arr[0].index(max(arr[0])))
    y=str(arr[0].index(max(arr[0])))
    file.write(y)
    file.write('\n')

file.close()
print "total time: ",endtime-starttime
