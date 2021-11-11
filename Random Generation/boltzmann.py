import math
import random

def genEpsilon():
    return ()

def genAtomic():
    return "Node"

def genTree(v_param):
    def generating_function(x):
        return (1 - math.sqrt(1 - 4*x))/(2*x)
    if not((0 < v_param) and (v_param < 1/4)):
        return -1
    u = random.random()
    if u < 1/generating_function(v_param):
        return genEpsilon()
    else:
        return (genAtomic(), genTree(v_param), genTree(v_param))

print(genTree(0.249999999999999))
    