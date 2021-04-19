import fuzzy_logic
import math
import random
import matplotlib.pyplot as plt

Const = 0.636097993511823

def get_jar():
	weight = int(input("Вес банки с монетами? "))
	weight1 = int(input("Вес банки? "))
	return weight - weight1

#coins/weight, diameter
data1 = {
1:[3.175, 20.5],
2:[5.5, 23],
5:[6.225, 25],
10:[5.63, 22]
}

data2 = {
1:[3.175, 20.5],
2:[5.5, 23],
5:[6.225, 25],
10:[5.63, 22],
0.01:[1.5, 15.5],
0.05:[2.6, 18.5],
0.1:[1.9, 17.5],
0.5:[2.8, 19.5]
}

data = {}

bbb = get_jar()

jar = {
"weight":bbb
}

if(input("Есть копейки? ") == 0):
	data = data1
	x = [1, 2, 5, 10]
else:
	data = data2
	x = [1, 2, 5, 10, 0.01, 0.05, 0.1, 0.5]
		
nominals = []
kef = []
		
for i in range(1000):
	w = jar["weight"]
	nominal = 0
	now_w = 0
	
	while (now_w < w):
		g = random.randint(0, len(x)-1)
		
		nn = data[x[g]]
		now_w += nn[0]
		
		nominal += x[g]
	nominals.append(nominal)
	k = nominal / (now_w+0.000001)
	if (k <= Const):
		k = k / Const
	else:
		k = k / Const
		k -= 1
		k = 1 - k
	kef.append(k)
	
graph = plt.scatter	(nominals, kef, marker='o')
grid1 = plt.grid(True)
plt.show()