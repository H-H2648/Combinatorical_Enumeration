
import random
import time
from collections import defaultdict

def binary0(v):
    return "0"

def binary1(v):
    return "1"

def binaryEmpty(v):
    return ""

##A, B refers to the generating function
def generateAdd(A, B, gammaA, gammaB, v):
    total = A(v) + B(v)
    rand = random.random()
    if rand < A(v)/(total):
        return gammaA(v)
    else:
        return gammaB(v)

def generateMult(gammaA, gammaB, v):
    return gammaA(v) + gammaB(v)

##A refers to the generating function
def generateSEQ( A, gammaA, v):
    rand = random.random()
    k = 0
    Av = A(v)
    add_val = 1-Av
    S = add_val
    while S < rand:
        k +=1
        add_val *= Av
        S += add_val
    output = ""
    for _ in range(k):
        output += gammaA(v)
    return output

###-1 refers to error
def main(v):
    radius = (5**(1/2)-1)/2
    if v < 0 or v > radius:
        return -1
    # def block_genF(v):
    #     return 1/(1-v)
    def eps_genF(v):
        return 1
    def atom_genF(v):
        return v
    def generateSEQ1(v):
        return generateSEQ( atom_genF, binary1, v)
    SEQ_1 = generateSEQ1(v)
    def generateSEQ1_with1(v):
        return generateMult(binary1, generateSEQ1, v)
    def generateSEQ1_with01(v):
        return generateMult(binary0, generateSEQ1_with1, v)
    def generateSEQ_SEQ1_with_01(v):
        def generating_func(x):
            return x**2/(1-x)
        return generateSEQ(generating_func, generateSEQ1_with01, v)
    MAIN_BLOCKS = generateSEQ_SEQ1_with_01(v)
    FINAL = generateAdd(eps_genF, atom_genF, binaryEmpty, binary0, v)
    return SEQ_1 + MAIN_BLOCKS + FINAL

# print("\\begin{itemize}")
# for _ in range(10):
#     print (f"\\item {main(0.6)}")
#     print("\n")
# print("\\end{itemize}")

t_end = time.time() + 60 
dict = defaultdict(int)
while time.time() < t_end:
    dict[len(main(0.6))] +=1

total_count = 0
total_length = 0
for length in dict:
    total_length += dict[length]*length
    total_count += dict[length]
print(total_length/total_count)
    


