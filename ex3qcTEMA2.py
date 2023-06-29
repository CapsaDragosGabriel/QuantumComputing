from qiskit import *
from qiskit import QuantumCircuit, QuantumRegister
from qiskit.quantum_info.operators import Operator
from qiskit.circuit.bit import Bit
from qiskit.circuit.library import RGate
import matplotlib.pyplot as plt
import cmath
import math
import array
array.array('i')
def do_modulo(a,x,N):
    i=1
    nr=1
    while i<=x:
        nr=(nr*(a%N))%N
        i=i+1
    return nr
a=9
x=100
n=55



l = []
i=1
for i in range(x+1):
    if i>=1:
        l.append(i)
        l
i=1
y =[]
for i in range(x+1):
    if i>=1:
        y.append(do_modulo(a,i,n))


# plotting the points
plt.plot(l, y)

# naming the x axis
plt.xlabel('x-ul are valorile')
# naming the y axis
plt.ylabel('%N are valoarea')

# giving a title to my graph
plt.title('Graful functiei')


# function to show the plot
plt.show()