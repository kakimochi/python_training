# import numpy as np
import matplotlib.pyplot as plt

with open("data.txt", 'r') as inputfile:
	lines = inputfile.readlines()
	x = []
	y = []
	for line in lines:
		value = line.replace('\n', '').split('\t')
		x.append(value[0])
		y.append(value[1])

plt.plot(x,y)
plt.savefig('data.png', dpi=300, orientation='portrait', transparent=False, pad_inches=0.0)

plt.show()
