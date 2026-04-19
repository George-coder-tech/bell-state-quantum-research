from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

# -----------------------
# IDEAL SIMULATION
# -----------------------
qc = QuantumCircuit(2, 2)
qc.h(0)
qc.cx(0, 1)
qc.measure([0, 1], [0, 1])

simulator = AerSimulator()
result = simulator.run(qc, shots=1024).result()
counts_ideal = result.get_counts()

print("Ideal Results:", counts_ideal)

# -----------------------
# NOISY SIMULATION
# -----------------------
from qiskit_aer.noise import NoiseModel, depolarizing_error

noise_model = NoiseModel()
error = depolarizing_error(0.05, 1)
noise_model.add_all_qubit_quantum_error(error, ['u1', 'u2', 'u3'])

noisy_simulator = AerSimulator(noise_model=noise_model)
result_noisy = noisy_simulator.run(qc, shots=1024).result()
counts_noisy = result_noisy.get_counts()

print("Noisy Results:", counts_noisy)

# -----------------------
# PROBABILITY ANALYSIS
# -----------------------
total = sum(counts_ideal.values())
print("\nProbability for Ideal Simulation")
for state, count in counts_ideal.items():
    print(state, count/total)

total = sum(counts_noisy.values())
print("\nProbability for Noisy Simulation")
for state, count in counts_noisy.items():
    print(state, count/total)

# -----------------------
# PLOT COMPARISON
# -----------------------
plt.show()
plot_histogram([counts_ideal, counts_noisy], legend=["Ideal", "Noisy"])
