def s_func (U, a = None, b = None, c = None):
    S = []

    if(a == None):
        a = U.min()
    if(c == None):
        c = U.max()
    if(b == None):
        b = (a+c)/2
    
    for x in U:
        if(x < a):
            S.append(0)
        elif((x >= a) and (x < b)):
            j = 2*((x-a)/(c-a)**2)
            S.append(j)
        elif((x >= b) and (x < c)):
            j = 2*((x-c)/(c-a)**2)
            S.append(1 - j)
        elif(x >= c):
            S.append(1)
    return S

def pi_func (U, a = None, b = None, c = None):
    PI_1 = []
    PI_2 = []

    if(a == None):
        a = U.min()
    if(c == None):
        c = U.max()
    if(b == None):
        b = (a+c)/2
	
    for x in U:	
        if(x < c):
            X = [x]
            el = S_func(X, c-b, c-(b/2), c)
            PI_1.append(el[0]) 
            
        elif(x >= c):
            X = [x]
            el = S_func(X, c, c + (b/2), c+b)
            PI_2.append(1 - el[0])
            
    return(PI_1 + PI_2)
    
def t_func (U, a = None, b = None, c = None):
    t = []

    if(a == None):
        a = U.min()
    if(c == None):
        c = U.max()
    if(b == None):
        b = (a+c)/2
    
    for x in U:
        if(x < a):
            t.append(0)
        elif((x >= a) and (x < b)):
            t.append((x-a)/(b-a))
        elif((x >= b) and (x < c)):
            t.append((c-x)/(c-b))
        elif(x >= c):
            t.append(0)
    return t
    
def y_func (U, a = None, b = None):
    y = []

    if(a == None):
        a = U.min()
    if(b == None):
        b = U.max()
        
    for x in U:
        if(x < a):
            y.append(0)
        elif((x >= a) and (x <= b)):
            y.append((x-a)/(b-a))
        elif(x > b):
            y.append(1)
    return y
    
def l_func (U, a = None, b = None):
    L = []

    if(a == None):
        a = U.min()
    if(b == None):
        b = U.max()
        
    for x in U:
        if(x < a):
            L.append(1)
        elif((x >= a) and (x <= b)):
            L.append((b-x)/(b-a))
        elif(x > b):
            L.append(0)
    return L
	
def generate_U (a = 0, b = 10, epsilon = 0):
        U = []
	step = 10**epsilon
        for i in range(a*step, b*step):
            U.append(i/step)
        U.append(b/1.0)
        return U
