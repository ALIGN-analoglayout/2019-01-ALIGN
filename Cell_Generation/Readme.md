# To run a file on local Machine

   Cell Name		File name		Syntax		
1. Switch (NMOS/PMOS)	fabric_Switch.pyc	python fabric_Switch.pyc nFin X_cells Y_cells
2. Differential Pair	fabric_DP.pyc		python fabric_DP.pyc nFin X_cells Y_cells
3. Differential Load	fabric_CMC.pyc		python fabric_CMC.pyc nFin X_cells Y_cells
4. Current Mirror Load	fabric_SCM.pyc		python fabric_SCM.pyc nFin X_cells Y_cells
5. Current Mirror	fabric_CM.pyc		python fabric_CM.pyc nFin Xcopy
6. Unit/arrary Capacitor fabric_Cap.pyc		python fabric_Cap.pyc unitCap X_cells Y_cells

# where 
      nFin: number of fins in a unit cell
      X_cells: number of cells in X-direction
      Y_cells: number of cells in y-direction
      Xcopy: "Xcopy" times reference current
      UnitCap: Value of the unit cap (e.g. python fabric_cap.py 2 1 1; it will generate a capacitance of value 2fF)

NOTE: After execution of the file  a Json file "mydesign_dr_globalrouting.json" will be generated in this directory; copy this file in "./Viewer/INPUT/" and open "./Viewer/index.html" to view the generated layout

# To run a file on Docker

Step 1. docker build -f Dockerfile.build.python -t with_python .

Step 2. docker build -t fabric .

Step 3. Go to "./Viewer/" and run following command: "docker build -t viewer_image ."

Step 4. docker run --mount source=inputVol,target=/INPUT fabric bash -c "source /sympy/bin/activate && cd /scripts && python "file_name" nFin X_cells Y_cells && python removeDuplicates.py && cp mydesign_dr_globalrouting.json /INPUT"

Step 5. docker run --mount source=inputVol,target=/public/INPUT --rm -d -p 8085:8000 viewer_image bash -c "source /sympy/bin/activate && cd /public && python -m http.server"

Step 6. xdg-open http://localhost:8085


