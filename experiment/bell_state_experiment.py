from qiskit import QuantumCircuit, Aer, execute
from qiskit.visualization import plot_histogram

# Step 1: Create 2-qubit circuit
qc = QuantumCircuit(2, 2)

# Step 2: Create Bell state
qc.h(0)
qc.cx(0, 1)

# Step 3: Measurement
qc.measure([0,1], [0,1])

# Step 4: Run simulator
simulator = Aer.get_backend('qasm_simulator')
job = execute(qc, simulator, shots=1024)
result = job.result()

counts = result.get_counts()

print("Simulation results:", counts)
