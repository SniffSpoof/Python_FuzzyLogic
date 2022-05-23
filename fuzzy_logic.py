'''
This is the main library file. 
The fuzzy set class and quantifiers are described here.
'''

import fuzzy_funcs
import math as m
import matplotlib.pyplot as plt

class fuzzy_set(object):
	def __init__(self, type = "Empty", U1 = None, U2 = None, a = None, b = None, c = None, epsilon = 1, U = None):
		#init of params
		#U1 and U2 its definition set bounds
		if((U1 != None) and (U2 != None)):
			self.U = fuzzy_funcs.generate_U(U1, U2, epsilon)
		else:
			self.U = U
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
		elif (type == "Empty"):
			self.f = []
		else:
			self.f = []
			for i in self.U:
				try:
					v = ((i+b)/(a))**c
				except:					#if zero zero div
					v = ((i+b)/(a+0.00001))**c
				self.f.append(1/(1+v))
			
	def init_params(self):
		self.height = max(self.f)
		self.sup = set(self.f)
		
	def alpha_cut(self, alpha):
		#go through the set of values, if less than alpha - 0, if greater or equal - value at point
		self.f_alpha = []
		for i in self.f:
			if(i >= alpha):
				self.f_alpha.append(i)
			else:
				self.f_alpha.append(0)
			
	def plot(self):
		graph = plt.plot(self.U, self.f)
		grid1 = plt.grid(True)
	
	def plot_scatter(self):
		graph = plt.scatter(self.U, self.f, marker='o')
		grid1 = plt.grid(True)
		
		
	def kvant(self, type, f2 = None):
		if (type == "not"):
			self.f = not_a(self.f)
		elif (type == "very"):
			self.f = very_a(self.f)
			print(self.f)
		elif (type == "MOL"):
			self.f = MOL_a(self.f)
		elif (type == "or"):
			b = f2.f
			marker = 0 #if sets have different sizes, then comparisons will occur on a smaller
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
			
def show():
	plt.show()
	
def not_a(U):
	a = []
	for el in U:
		a.append(1 - el)
	return a
	
def very_a(U):
	a = []
	for el in U:
		a.append(el**2)
	return a
	
def MOL_a(U):
	#more or less
	a = []
	for el in U:
		a.append(m.sqrt(el))
	return a
	
def a_or_b(U1, U2):
	a = []
	i = 0
	marker = 0
	if (len(U1) > len(U2)):
		c = U1
		U1 = U2
		U2 = c
		marker = 1
	for el in U1:
		try:
			a.append(min(el, U2[i]))
		except:					#if went beyond the function definition
			a.append(0)
		i+=1
	return a, marker
	
def a_and_b(U1, U2):
	a = []
	i = 0
	marker = 0
	if (len(U1) > len(U2)):
		c = U1
		U1 = U2
		U2 = c
		marker = 1
	for el in U1:
		try:
			a.append(min(el, U2[i]))
		except:
			a.append(0)
		i+=1
	return a, marker
