Creater: Texas A\&M University
Version: v0.1

Function: 
This binary can do physical synthesis for specified analog design.


How to use:
PnR_image DATA_FOLDER LEF_FILE VERILOG_FILE BLOCK_GDS_MAP_FILE DESIGN_RULE_FILE TOP_CELL_NAME
* DATA_FOLDER : the directory which contains all input data
* LEF_FILE: LEF file name
* VERILOG_FILE: block-level Verilog file name
* BLOCK_GDS_MAP_FILE: mapping file which records the GDS file of each building block
* DESIGN_RULE_FILE: design rule file name
* TOP_CELL_NAME: top cell for place and route

Example：
./PnR_image ./testcase_latest2 sc.lef sc_block.v sc.map drcRules_calibre_asap7_Rule_Deck.rul switched_capacitor_filter | tee log

Limitation:
1. In the current version only placement is enabled. Routing will be released in the next version.
2. For hierarchical design, only the placement of bottom level will be created (even the top cell is specified by augments).
