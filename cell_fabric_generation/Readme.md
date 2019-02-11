# To run a file on local Machine

Step 1. python "file_name" nFin X_cells Y_cells
where nFin: number of fins in a unit cell
      X_cells: number of cells in X-direction
      Y_cells: number of cells in y-direction

Step 2. python "file_name" unitCap X_cells Y_cells

where unitCap: value of unit cap in fF
e.g. python fabric_cap.py 2 1 1
it will generate a capacitance of value 2fF


Step 3. After execution of the file  a Json file "mydesign_dr_globalrouting.json" will be generated in this directory; copy this file in "./Viewer/INPUT/" and open "./Viewer/index.html" to view the generated layout

# To run a file on Docker

Step 1. docker build -f Dockerfile.build.python -t with_python .

Step 2. docker build -t fabric .

Step 3. Go to "./Viewer/" and run following command: "docker build -t viewer_image ."

Step 4. docker run --mount source=inputVol,target=/INPUT fabric bash -c "source /sympy/bin/activate && cd /scripts && python "file_name" nFin X_cells Y_cells && python removeDuplicates.py && cp mydesign_dr_globalrouting.json /INPUT"

Step 5. docker run --mount source=inputVol,target=/public/INPUT --rm -d -p 8085:8000 viewer_image bash -c "source /sympy/bin/activate && cd /public && python -m http.server"

Step 6. xdg-open http://localhost:8085


