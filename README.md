# Bell-State Quantum Research

# Abstract
This project investigates the creation of Bell-state entanglement using quantum circuits.
An ideal quantum simulator was used to establish baseline behavior prior to execution on real quantum hardware.

# Methodology
A two-qubit quantum circuit was constructed using a Hadamard gate followed by a CNOT gate.
Measurements were performed using 1024 shots using Qiskit.

# Results
The simulator produced an approximately equal probability distribution between |00⟩ and |11⟩ states,
confirming successful Bell-state entanglement in a noise-free environment.

# Future Work
This experiment will be extended to real IBM Quantum hardware to analyze the effects of noise and decoherence.
