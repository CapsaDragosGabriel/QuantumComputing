
from qiskit import *
from qiskit import QuantumCircuit, QuantumRegister
from qiskit.quantum_info.operators import Operator
import cmath
import math
#definim functia
def check_matrix (r1 , r2) :
    eps = sys.float_info.epsilon
    for i in range(16):
        for j in range(16):
            if(abs(r1[i][j]-r2[i][j])>=eps):
                return print("Matricile NU sunt egale! => Circuitele NU sunt echivalente pentru poarta "+ str(GATE))
    return print("Matricile sunt egale => Circuitele sunt echivalente pentru poarta "+ str(GATE))

controls = QuantumRegister(1)
circuit = QuantumCircuit(controls)


GATE=input("What gate do you want (X,Y,Z,H,S,custom) : ")
if GATE == "X":
    a= 0
    b= 1
    c=1
    d=0
elif GATE=="Y":
    a = 0
    b = complex(0, -1)
    c = complex(0, 1)
    d = 0
elif GATE=="Z":
    a = 1
    b = 0
    c = 0
    d = -1
elif GATE=="H":
    a = 1*math.sqrt(1/2)
    b = 1*math.sqrt(1/2)
    c = 1*math.sqrt(1/2)
    d = -1*math.sqrt(1/2)
elif GATE=="S":
    a = 1
    b = 0
    c = 0
    d = complex(0, 1)
elif GATE=="custom":
    print(
        "Your matrix will look like this:\n"
        "u11 u12\n"
        "u21 u22\n"
    )
    a =complex( input("Enter your value for u11: "))
    b =complex( input("Enter your value for u12: "))
    c =complex( input("Enter your value for u21: "))
    d = complex( input("Enter your value for u22: "))


print("Your chosen matrix is: \n"+ str(a)+","+str(b)+"\n"+str(c)+","+str(d)+"\n")

cu = Operator([
     [a, b],
     [c, d]
])
circuit.unitary(cu, [0], label='U')
print(circuit.draw())
circuit.unitary(cu, [0], label='U') 
custom = circuit.to_gate(label='U').control(3, '|010>', '010')

qc2 = QuantumCircuit(4)

qc2.append(custom, [0, 1, 2, 3])
print(qc2.draw())

simulator = Aer.get_backend('unitary_simulator')
result = execute(qc2, simulator).result()
#print(result.get_unitary(qc2, decimals=3))
# salvam matricea unitara a circuitului din stanga
rs = result.get_unitary(qc2, decimals=3)


qcd = QuantumCircuit(4)
qcd.x(0)
qcd.x(2)
dreapta = circuit.to_gate(label='U').control(3, '|111>', '111')

qcd.append(dreapta, [0, 1, 2, 3])
qcd.append(dreapta, [0, 1, 2, 3])
qcd.append(dreapta, [0, 1, 2, 3])
qcd.x(0)
qcd.x(2)
print(qcd.draw())
result = execute(qcd, simulator).result()
#print(result.get_unitary(qcd, decimals=3))
# salvam matricea unitara a circuitului din dreapta
rd = result.get_unitary(qcd, decimals=3)

check_matrix(rs, rd)
