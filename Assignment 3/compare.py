mainouttest=[]
with open('test-labels.txt') as f:
    for line in f:

       taken=int(line)
       mainouttest.append(taken)


maintrain=[]
with open('finalresult(1.4325).txt') as f:
    for line in f:

       print line[0]
       taken=int(line[0])
       maintrain.append(taken)        

count=0
print len(mainouttest)
print len(maintrain)
for i in range(0,len(mainouttest)):
    if mainouttest[i]==maintrain[i]:
        count =count+1;

print "length",len(maintrain)
print "count",count