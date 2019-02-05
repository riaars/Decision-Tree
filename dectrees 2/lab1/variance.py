from python import monkdata as m
from python import dtree as d
import random as r
import matplotlib.pyplot as plt
import numpy as np

def partition(data, fraction):
	ldata = list(data)
	r.shuffle(ldata)
	breakPoint = int(len(ldata) * fraction)
	return ldata[:breakPoint], ldata[breakPoint:]

size = 1000
errorlist = []
meanlist = []
part = []
std = []

plt.subplots_adjust(hspace = 0.45)

raw = plt.subplot(2,1,1)
raw.set_title('Mean and raw values')
raw.set_xlabel('fraction')
raw.set_ylabel('error')
stat = plt.subplot(2,1,2)
stat.set_title('Standard deviation')
stat.set_xlabel('fraction')
stat.set_ylabel('standard deviation')

for j in range(3,9):
	print j
	total = 0
	for k in range(size):
		monk1train, monk1val = partition(m.monk3, j/10.0)

		t = d.buildTree(monk1train, m.attributes)
		checkT = d.check(t, monk1val)

		while True:
			hold = checkT
			tprune = d.allPruned(t)

			for i in tprune:
				temp=(d.check(i, monk1val))
				if(temp > checkT):
					checkT = temp
					t = i
					#print checkT

			if(checkT == hold):
				break

		error =1 - d.check(t, m.monk3test)
		part.append([j/10.0,error])
		total += error

		#print errorlist
	errorlist.append(part)
	meanlist.append([j/10.0, total/size])

for i in errorlist:
	for a,b in i:
		raw.plot(a, b, marker ='.', color = 'gray', label = 'raw')

for a,b in meanlist:
	raw.plot(a,b, '-p', color = 'red', markersize =10, linewidth = 2, label = 'mean')

raw.legend(bbox_to_anchor=(0.2,-0.1))
j = 0.3
for i in errorlist:
	for a,b in i:
		std.append(b)

	stat.plot(j, np.std(np.array(std)), marker ='o')
	j += 0.1



plt.show()
