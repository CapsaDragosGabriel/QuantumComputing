from qiskit import *
from qiskit import QuantumCircuit, QuantumRegister
from qiskit.quantum_info.operators import Operator
from qiskit.circuit.bit import Bit
from qiskit.circuit.library import RGate
import cmath
import math

j1=int (input("Enter first decimal (0/1):"));
j2=int(input("Enter second decimal (0/1):"));
j3=int(input("Enter third decimal (0/1):"));
#print(math.pi)
pi=math.pi
number=(0*1000+j1*100+j2*10+j3)/1000
print(number)
circuit = QuantumCircuit(4)
circuit.y(3)
circuit.z(3)
circuit.barrier()
circuit.h(0)
circuit.h(1)
circuit.h(2)
u_gate=RGate(4*pi*number, pi/2).control(1)

circuit.barrier()
circuit.append(u_gate,[0,3])
circuit.append(u_gate,[1,3])
circuit.append(u_gate,[1,3])
circuit.append(u_gate,[2,3])
circuit.append(u_gate,[2,3])
circuit.append(u_gate,[2,3])
circuit.append(u_gate,[2,3])
circuit.barrier()
circuit.h(0)
circuit.h(1)
circuit.h(2)
r1=RGate(-pi/4,0).control(1)
circuit.append(r1,[2,0])
r2=RGate(-pi/2,0).control(1)
circuit.append(r2,[1,0])
circuit.append(r2,[2,1])
circuit.barrier()

circuit.measure_all()

print(circuit.draw())

simulator = Aer.get_backend('qasm_simulator')
result = execute(circuit, simulator, shots=1024).result()
counts = result.get_counts()
print(counts)