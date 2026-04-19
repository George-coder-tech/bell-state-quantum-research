# Bell-State Quantum Analysis

 1. Theoretical Background

A Bell state is a maximally entangled quantum state of two qubits.  
For the |Φ⁺⟩ state, the expected result is:

- |00⟩ with ~50% probability  
- |11⟩ with ~50% probability  
- |01⟩ and |10⟩ should be 0% (ideal case)

This reflects perfect quantum entanglement.

---

 2. Simulation Results

The quantum circuit was executed using a Qiskit simulator with 1024 shots.

Observed results:
- |00⟩ ≈ 50%
- |11⟩ ≈ 50%

This matches theoretical predictions for an ideal, noise-free quantum system.

---

3. Interpretation

The results confirm that:

- The Hadamard gate correctly created superposition
- The CNOT gate successfully generated entanglement
- Measurement outcomes are correlated as expected

This verifies correct implementation of a Bell state.

---

 4. Limitations

The simulation assumes a perfect quantum system and does not include:

- Decoherence
- Gate errors
- Readout noise

Therefore, real quantum hardware is expected to produce deviations.

---
 5. Future Work

The next phase of this project will involve:

- Running the same circuit on real IBM Quantum hardware
- Comparing noisy results with simulator results
- Quantifying the effect of quantum noise on entanglement

This will provide insight into real-world quantum computing limitations.
