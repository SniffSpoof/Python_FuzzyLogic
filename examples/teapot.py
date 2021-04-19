import fuzzy_logic
import math

def integral (data):
	c = 0
	for i in data:
		c += i
	return c

#teapot
user = 100 - int(input("Со скольки градусов чайник уже хотя бы немного не холодный?: "))
f1 = fuzzy_logic.exemple("PI", 0, 100, 0, user, 100, 1)
f2 = fuzzy_logic.exemple("PI", 0, 100, 0, user, 100, 1)

f1.kvant("not")
f1.kvant("MOL")

f2.kvant("very")
f2.kvant("MOL")
f2.kvant("not")

print("The first: ", integral(f1.f))
print("The second: ", integral(f2.f))

f1.plot()
f2.plot()
fuzzy_logic.plot_show()
