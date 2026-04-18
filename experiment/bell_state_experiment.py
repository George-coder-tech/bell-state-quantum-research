from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

# Create 2-qubit circuit
qc = QuantumCircuit(2, 2)

# Bell state
qc.h(0)
qc.cx(0, 1)

# Measurement
qc.measure([0, 1], [0, 1])

# Simulator
simulator = AerSimulator()
result = simulator.run(qc, shots=1024).result()

counts = result.get_counts()

print("Results:", counts)
