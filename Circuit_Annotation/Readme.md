## Steps to run the module


Step 1: Copy spice netlist of the circuit in the "input_circuit" directory


Step 2: Define subcircuit name in the runme.sh file 

Step 3: Run the module on docker or local machine

        # Docker commands
       3.1: docker build -t topology .
       
       3.2: docker run --mount source=inputVol,target=/INPUT --rm -d -p 8086:8000 topology bash -c "source /sympy/bin/activate && cd /DEMO && source runme.sh  && python -m http.server"
       


