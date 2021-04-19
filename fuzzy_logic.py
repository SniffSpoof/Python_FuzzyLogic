import fuzzy_funcs
import math as m
import matplotlib.pyplot as plt

class exemple(object):
	def __init__(self, type, U1, U2, a, b, c, epsilon = 1):
		#init of params
		self.U = fuzzy_funcs.generate_U(U1, U2, epsilon)
		self.a = a
		self.b = b
		self.c = c
		self.type = type
		#init func
		if (type == "S"):
			self.f = fuzzy_funcs.S_func(self.U, self.a, self.b, self.c)
		elif (type == "t"):
			self.f = fuzzy_funcs.t_func(self.U, self.a, self.b, self.c)
		elif (type == "y"):
			self.f = fuzzy_funcs.y_func(self.U, self.a, self.b)
		elif (type == "L"):
			self.f = fuzzy_funcs.L_func(self.U, self.a, self.b)
		elif (type == "PI"):
			self.f = fuzzy_funcs.PI_func(self.U, self.a, self.b, self.c)
		else:
			self.f = []
			for i in self.U:
				a = a + 0.000001
				v = ((i+b)/(a))**c
				self.f.append(1/(1+v))
			
	def init_params(self):
		self.height = max(self.f)
		#self.sup = #диапозон
		
	def alpha_cut(self):
		#бежим по множеству значений, если меньше альфы - 0, если больше либо равно = значению в точке
		pass
			
	def plot(self):
		graph = plt.plot(self.U, self.f)
		grid1 = plt.grid(True)	 # линии вспомогательной сетки
		
		
	def kvant(self, type, f2 = None):
		if (type == "not"):
			self.f = not_a(self.f)
		elif (type == "very"):
			self.f = very_a(self.f)
		elif (type == "MOL"):
			self.f = MOL_a(self.f)
		elif (type == "or"):
			b = f2.f
			marker = 0
			self.f, marker = a_or_b(self.f, b)
			if(marker == 1):
				self.U = f2.U
		elif (type == "and"):
			b = f2.f
			marker = 0
			self.f, marker = a_and_b(self.f, b)
			if(marker == 1):
				self.U = f2.U
		else:
			print("None")
			
def plot_show():
	plt.show()
	
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
	marker = 0
	if (len(U1) > len(U2)):
		c = U1
		U1 = U2
		U2 = c
		marker = 1
	for el in U1:
		a.append(max(el, U2[i]))
		i+=1
	return a, marker
	
def a_and_b (U1, U2):
	a = []
	i = 0
	marker = 0
	if (len(U1) > len(U2)):
		c = U1
		U1 = U2
		U2 = c
		marker = 1
	for el in U1:
		a.append(min(el, U2[i]))
		i+=1
	return a, marker
