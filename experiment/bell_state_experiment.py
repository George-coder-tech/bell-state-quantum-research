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

counts_ideal = result.get_counts()

print("Ideal Results:", counts_ideal)

from qiskit_aer.noise import NoiseModel, depolarizing_error

noise_model = NoiseModel()
error = depolarizing_error(0.05, 1)
noise_model.add_all_qubit_quantum_error(error, ['u1', 'u2', 'u3'])

noisy_simulator = AerSimulator(noise_model=noise_model)
result_noisy = noisy_simulator.run(qc, shots=1024).result()
counts_noisy = result_noisy.get_counts()

print("Noisy Results:", counts_noisy)

from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt
plt.show()
plot_histogram([counts_ideal, counts_noisy], legend=["Ideal", "Noisy"])


