from qiskit_ibm_runtime import QiskitRuntimeService
from qiskit import QuantumCircuit, transpile
from qiskit_algorithms import AmplificationProblem, Grover
from qiskit.primitives import Sampler
from qiskit.visualization import plot_histogram

# Autenticazione con IBM Quantum
service = QiskitRuntimeService(channel="ibm_quantum", token="<MY_IBM_QUANTUM_TOKEN>")
service = QiskitRuntimeService()

# Real backend on a quantum computer with 16 qubits
backend = service.backend("ibmq_16_melbourne")

# We want to search the 11 state
good_state = ["11"]

# Oracle for the 11 state
oracle = QuantumCircuit(2)
oracle.cz(0, 1)

# Define Grover's algorithm
problem = AmplificationProblem(oracle, is_good_state=good_state)


grover_op = problem.grover_operator.decompose()
grover_op.draw(output='mpl', filename='grover_circuit.png')


grover = Grover(sampler=Sampler())

# Compile and trasform the circuit to run on the backend
grover_circuit = grover.amplify(problem).circuit
transpiled_circuit = transpile(grover_circuit, backend)

# Execute the circuit on the quantum computer
job = Sampler(backend).run(transpiled_circuit)
result = job.result()

# Count the results
counts = result.get_counts(transpiled_circuit)

# Visualize the result
print("Result counts:", counts)
plot_histogram(counts).savefig("grover_results.png")
