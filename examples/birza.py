import random
money_on_start = 30000
#global variables
R_up = float(input("Риск при росте? "))
R_down = float(input("Риск при падении? "))
random.seed(version=2)
quotation = 100
func = [quotation]; quotation += random.randint(-10, 10); func.append(quotation)
days = [1, 2]
is_up = (func[0]<func[1])
is_buy = False
money_now = money_on_start
bank = 0
start = quotation

import matplotlib.pyplot as plt
import fuzzy_logic
risk_up = fuzzy_logic.fuzzy_set("y", 0, 25, 0, R_up, 1, 4)
risk_down = fuzzy_logic.fuzzy_set("y", 0, 25, 0, R_down, 1, 4)

def show_graph(U, f):
	graph = plt.plot(U, f)
	grid = plt.grid(True)#линии вспомогательной сетки
	plt.show()

def up_or_down():
	global is_up
	is_up = (func[-2]<func[-1])

def buy():
	global money_now
	global bank
	bank = money_now // quotation
	money_now -= bank*quotation
	global is_buy
	is_buy = True
	
def sell():
	global money_now
	global bank
	money_now += bank*quotation
	bank = 0
	global is_buy
	is_buy = False
	
def buy_or_sell():
	global start
	now_risk = round((start/quotation), 3)
	if(is_buy):
		if(R_up <= risk_up.f[risk_up.U.index(now_risk)]):
			sell()
			start = quotation
	
	elif(R_down < risk_down.f[risk_down.U.index(now_risk)]):
		buy()
		start = quotation

for day in range(3, (368)+1):
	#global start
	quotation += random.randint(-10, 10)
	if(quotation == 0):
		break
	days.append(day)
	func.append(quotation)
	
	up_or_down()
	if (is_up == False):
		sell()
		start = quotation
	else:
		buy_or_sell()
	
sell()
print("Было вложено:", money_on_start, "₽")
h = ((money_now/money_on_start) - 1)*100
print("Прибыль за год:", money_now - money_on_start, "₽ Прибыльность: ", h, "%")
print("Это успех?", (h > 10))
show_graph(days, func)