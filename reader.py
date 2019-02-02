import numpy as np
f=open("output.txt", "r")
losses=[]
acc=[]
def mean(numbers):
    return float(sum(numbers)) / max(len(numbers), 1)
for i in f.readlines():
	losses.append(float((i.split(" ")[3])))
	acc.append(float((i.split(" ")[6].replace("\n", "").replace("pr",""))))
print "mean loss " + str(mean(losses)) +" +/- "+ str(np.var(losses))
print "mean acc " + str(mean(acc)) + " +/- "+str(np.var(acc))
