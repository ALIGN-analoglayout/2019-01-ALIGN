#!/bin/bash
# cleaning all files

## READ LIBRARY 
## Reads inputs netlist of spice format (".sp") from basic_library folder
## There is basic template of libraries which we provide: basic_template.sp
## User can add more templates in : user_template.sp
#python ./src/read_library.py
python ./src/read_library.pyc
# the output is stored in library_graph in yaml format

## READ input netlist 
## Reads inputs netlist of spice format (".sp") from input_circuit folder
## User need to keep his spice netlist in this directory : switched_cap_filter.sp
#python ./src/read_netlist.py netlist_amp.sp amp 
#python ./src/read_netlist.py netlist_BS_AMP.sp TB_IBS_norm 
#python ./src/read_netlist.py Tristate_buffer.cdl Tristate_buffer

# the output is stored in circuit_graph directory in yaml format
#rm ./circuit_graphs/*
#python ./src/read_netlist.py opamp5.sp opamp5
#****************************************FOR OTA example******************************
python ./src/read_netlist.pyc ota.sp cascode_current_mirror_ota
#****************************************FOR switched_cap_filter example******************************
#python ./src/read_netlist.py switched_cap_filter.sp switched_cap_filter 

# <Place holder for generate LEF>


## MATCH GRAPH
## loads graph from circuit_graph and matches the graphs defined in library_graph
## reduces the graph by merging nodes of matched graphs
python ./src/match_graph.pyc
#store the matches and reduced graph in pickle binary format 

## GENERATE VERILOG
python ./src/write_verilog.pyc
#store output in verilog format in results dir
