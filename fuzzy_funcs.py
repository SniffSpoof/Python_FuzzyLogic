def s_func(U, a=None, b=None, c=None):
    s = []

    if a is None:
        a = U.min()
    if c is None:
        c = U.max()
    if b is None:
        b = (a + c) / 2

    for x in U:
        if x < a:
            s.append(0)
        elif (x >= a) and (x < b):
            j = 2 * ((x - a) / (c - a) ** 2)
            s.append(j)
        elif (x >= b) and (x < c):
            j = 2 * ((x - c) / (c - a) ** 2)
            s.append(1 - j)
        elif x >= c:
            s.append(1)
    return s


def pi_func(U, a=None, b=None, c=None):
    pi_1 = []
    pi_2 = []

    if a is None:
        a = U.min()
    if c is None:
        c = U.max()
    if b is None:
        b = (a + c) / 2

    for x in U:
        if x < c:
            X = [x]
            el = s_func(X, c - b, c - (b / 2), c)
            pi_1.append(el[0])

        elif x >= c:
            X = [x]
            el = s_func(X, c, c + (b / 2), c + b)
            pi_2.append(1 - el[0])

    return pi_1 + pi_2


def t_func(U, a=None, b=None, c=None):
    t = []

    if a is None:
        a = U.min()
    if c is None:
        c = U.max()
    if b is None:
        b = (a + c) / 2

    for x in U:
        if x < a:
            t.append(0)
        elif (x >= a) and (x < b):
            t.append((x - a) / (b - a))
        elif (x >= b) and (x < c):
            t.append((c - x) / (c - b))
        elif x >= c:
            t.append(0)
    return t


def y_func(U, a=None, b=None):
    y = []

    if a is None:
        a = U.min()
    if b is None:
        b = U.max()

    for x in U:
        if x < a:
            y.append(0)
        elif (x >= a) and (x <= b):
            y.append((x - a) / (b - a))
        elif x > b:
            y.append(1)
    return y


def l_func(U, a=None, b=None):
    l = []

    if a is None:
        a = U.min()
    if b is None:
        b = U.max()

    for x in U:
        if x < a:
            l.append(1)
        elif (x >= a) and (x <= b):
            l.append((b - x) / (b - a))
        elif x > b:
            l.append(0)
    return l


class Universum(object):
    def __init__(self, l=0, r=10, epsilon=0):
        self.u = []
        step = 10 ** epsilon
        for i in range(l * step, (r+1) * step):
            self.u.append(i / step)
