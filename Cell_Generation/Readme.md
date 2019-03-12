# To run a file on local Machine (Use Python 3.7)

Layouts for these basic cells can be generated:

1. Switch (fabric_Switch_NMOS/PMOS.py)	                     
2. Differential Pair (fabric_DP_NMOS/PMOS.py)		                     
3. Differential Load (fabric_CMC_NMOS/PMOS.py)		                     
4. Current Mirror Load (fabric_SCM_NMOS/PMOS.py)		                     
5. Current Mirror	     (fabric_CM_NMOS/PMOS.py)		                     
6. Unit/arrary Capacitor (fabric_Cap.py)

## Syntax to run these files (Use Python 3.7)

1. python fabric_Switch_NMOS/PMOS.py nFin X_cells Y_cells
2. python fabric_DP_NMOS/PMOS.py nFin X_cells Y_cells
3. python fabric_CMC_NMOS/PMOS.py nFin X_cells Y_cells
4. python fabric_SCM_NMOS/PMOS.py nFin X_cells Y_cells
5. python fabric_CM_NMOS/PMOS.py nFin Xcopy
6. python fabric_Cap.pyc unitCap X_cells Y_cells

NOTE: After execution of these scripts a Json file "mydesign_dr_globalrouting.json" will generate in this directory; copy this file in "./Viewer/INPUT/" and open "./Viewer/index.html" to view the generated layout

# where 
      nFin: number of fins in a unit cell
      X_cells: number of cells in X-direction
      Y_cells: number of cells in y-direction
      Xcopy: "Xcopy" times reference current
      UnitCap: Value of the unit cap (e.g. python fabric_cap.py 2 1 1; it will generate a capacitance of value 2fF)


# To run a file on Docker

Step 1. docker build -f Dockerfile.build.python -t with_python .

Step 2. docker build -t fabric .

Step 3. Go to "./Viewer/" and run following command: "docker build -t viewer_image ."

Step 4. docker run --mount source=inputVol,target=/INPUT fabric bash -c "source /sympy/bin/activate && cd /scripts && python "file_name" nFin X_cells Y_cells && python removeDuplicates.py && cp mydesign_dr_globalrouting.json /INPUT"

Step 5. docker run --mount source=inputVol,target=/public/INPUT --rm -d -p 8085:8000 viewer_image bash -c "source /sympy/bin/activate && cd /public && python -m http.server"

Step 6. xdg-open http://localhost:8085


