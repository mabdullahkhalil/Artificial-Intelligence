import numpy as np
import PIL
from PIL import Image
import time


def sigmoid_Function(x, deriv=False):  
    if (deriv == True):
        return (x * (1 - x))

    return 1 / (1 + np.exp(-x))  



# loading files into vectors
Path="/Users/mABDULLAHk/Desktop/"
mainouttrain=[]
mainintrain=[]
with open('/Users/mABDULLAHk/Desktop/train/train.txt') as f:
    for line in f:
        line=line.rstrip()

        taken=int(line[len(line)-1])
        vec=[]
        for i in range(0,10):
            if i==taken:
                vec.append(1)
            else:
                vec.append(0)

        mainouttrain.append(vec)
        line=line.replace(' ', '')[:-1]
        print line
        img = PIL.Image.open(Path+line).convert("L")
        arr = np.array(img)
        y=255-(np.ravel(arr))
        mainintrain.append(y)


mainouttest=[]
maininptest=[]
file1=open('imagetestlabel.txt','w')

with open('/Users/mABDULLAHk/Desktop/test/test.txt') as f:
    for line in f:
        line=line.rstrip()

        taken=int(line[len(line)-1])
        file1.write(str(taken))
        file1.write('\n')

        line=line.replace(' ', '')[:-1]
        print line
        img = PIL.Image.open(Path+line).convert("L")
        arr = np.array(img)
        y=255-(np.ravel(arr))
        maininptest.append(y)
file1.close()



np.random.seed(1)


starttime=time.time()

#introducing weights
syn0 = 2 * np.random.random((784,30)) - 1         # creating a 784x30 array showing 784 inputs and 30 hidden layer
syn1 = 2 * np.random.random((30,10)) - 1          # creating a 30x10 array showing 30 hidden and 10 output

for z in xrange(0,2):
    for i in xrange(0,len(mainintrain)):
        X = np.array([mainintrain[i]])/float(255)     # normalising the input data
        y = np.array([mainouttrain[i]])


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
        syn1 += (np.dot(l1.T,l2_delta))*0.5
        syn0 += (np.dot(l0.T, l1_delta))*0.5

    arr=np.array(l2)
    arr=arr.tolist()


    print("Output after test")
    print(arr[0].index(max(arr[0])))


endtime=time.time()

# computing the expected value of testing data
file=open('imageresult(0.5).txt','w')
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




