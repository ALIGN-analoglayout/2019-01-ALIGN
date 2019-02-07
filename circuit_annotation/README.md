# subckt identification

# Build docker image
docker build -t topology .

# Run a Python-based test using docker

docker run --mount source=inputVol,target=/INPUT --rm -d -p 8086:8000 topology bash -c "source /sympy/bin/activate && cd /DEMO && source runme.sh  && python -m http.server"

# to see the results directory 
xdg-open http://localhost:8086

# Direct run on terminal
source ./runme.sh

# INPUT is testbench circuit
You need to add your circuit in input_circuit directory


