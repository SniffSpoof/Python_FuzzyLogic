#main

from matplotlib import pylab as plt
from matplotlib import colors
import numpy as np
import math
from itertools import product
import fuzzy_funcs
import fuzzy_kvant
import fuzzy_logic

f1 = fuzzy_logic.exemple("PI", 0, 100, 0, 50, 100, 1)
f1.plot()
f2 = fuzzy_logic.exemple("S", 0, 200, 0, 100, 200, 1)
f2.plot()
f1.kvant("and",f2)
f1.plot()
fuzzy_logic.plot_show()