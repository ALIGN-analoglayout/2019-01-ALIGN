#!/bin/bash
# cleaning all files

## READ LIBRARY 
## Reads inputs netlist of spice format (".sp") from basic_library folder
## There is basic template of libraries which we provide: basic_template.sp
## User can add more templates in : user_template.sp
#python ./src/read_library.py
./src/read_library
# the output is stored in library_graph in yaml format

## READ input netlist 
## Reads inputs netlist of spice format (".sp") from input_circuit folder
## User need to keep his spice netlist in this directory : switched_cap_filter.sp
./src/read_netlist
# the output is stored in circuit_graph directory in yaml format

# <Place holder for generate LEF>


## MATCH GRAPH
## loads graph from circuit_graph and matches the graphs defined in library_graph
## reduces the graph by merging nodes of matched graphs
./src/match_graph
#store the matches and reduced graph in pickle binary format 

## GENERATE VERILOG
./src/write_verilog
#store output in verilog format in results dir
