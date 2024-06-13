# quantum-algorithms
# How run this code
### Install dependencies (qiskit is required)
To run the code you need to use qiskit, to simulate a quantum environment on your pc or connect to an ibm quantum computer
From the root folder of the project run the following command:
```
pip install -r requirements.txt
```
If you want to try the algorithm on your pc in a simulated environment, run:
```
python3 grovers_algorithm.py
```
After execution, an image representing the quantum circuit will be saved in the project folder.
If you want to run the algorithm on a quantum computer, you need to create an account on IBM Quantum Experience and get the API token to insert into the ```grovers_algorithm_quantum_pc.py``` script.
After entering the token and choosing which computer to run the script on, run the following command to execute the Grover's algorithm on a quantum computer:
```
python3 grovers_algorithm_quantum_pc.py 
```
