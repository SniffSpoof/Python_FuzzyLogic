import math as m

def not_a (U):
	a = []
	for el in U:
		a.append(1 - el)
	return a
	
def very_a (U):
	a = []
	for el in U:
		a.append(el**2)
	return a
	
def MOL_a (U):
	#more or less
	a = []
	for el in U:
		a.append(m.sqrt(el))
	return a
	
def a_or_b (U1, U2):
	a = []
	i = 0
	if (len(U1) > len(U2)):
		c = U1
		U1 = U2
		U2 = c
	for el in U1:
		a.append(max(el, U2[i]))
		i+=1
	return a
	
def a_and_b (U1, U2):
	a = []
	i = 0
	if (len(U1) > len(U2)):
		c = U1
		U1 = U2
		U2 = c
	for el in U1:
		a.append(min(el, U2[i]))
		i+=1
	return a