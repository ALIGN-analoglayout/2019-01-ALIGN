//Verilog block level netlist file for netlist_BS_AMP
//Generated by UMN for ALIGN project 


module netlist_BS_AMP ( VDD ); 
inout VDD;
Amp_diff_norm_rvt I37 ( .IBSn(net022), .IN(net019), .IP(net020), .ON(rON), .OP(rOP), .VDD(VDD), .VSS(gnd!) ); 
res_3k RR8 ( .net014(net014), .gnd!(gnd!) ); 

endmodule

module IBS_norm_slvt ( IBS_IN, IBSn_OUT, IBSp_OUT, VDD, VSS ); 
inout IBS_IN, IBSn_OUT, IBSp_OUT, VDD, VSS;
SCM_NMOS_3x3 MN1_MN0 ( .D1(net7), .D2(IBSn_OUT), .S(VSS) ); 


endmodule

module IBS_norm_hvt ( IBS_IN, IBSn_OUT, IBSp_OUT, VDD, VSS ); 
inout IBS_IN, IBSn_OUT, IBSp_OUT, VDD, VSS;

DiodeConnected_PMOS_4x3 MP1 ( .D(IBS_IN), .S(VDD) ); 
SCM_NMOS_1x4_4x3 MN1_MN0 ( .D1(net7), .D2(IBSn_OUT), .S(VSS) ); 
CMC_PMOS_4x3 MP2_MP0 ( .D1(IBSp_OUT), .G(IBS_IN), .D2(net7), .S(VDD) ); 

endmodule

module Amp_diff_norm_hvt ( IBSn, IN, IP, ON, OP, VDD, VSS ); 
inout IBSn, IN, IP, ON, OP, VDD, VSS;

res_3p83 RR0 ( .ON(ON), .VDD(VDD) ); 
res_3p83 RR9 ( .OP(OP), .VDD(VDD) ); 
SCM_NMOS_4x4_4x3 MN3_MN0 ( .D1(IBSn), .D2(net39), .S(VSS) ); 
DP_NMOS_2x2_4x3 MN1_MN2 ( .D1(ON), .G1(IP), .S(net39), .D2(OP), .G2(IN) ); 

endmodule

module IBS_norm_rvt ( IBS_IN, IBSn_OUT, IBSp_OUT, VDD, VSS ); 
inout IBS_IN, IBSn_OUT, IBSp_OUT, VDD, VSS;

DiodeConnected_PMOS_3x3 MP1 ( .D(IBS_IN), .S(VDD) ); 
SCM_NMOS_3x3 MN1_MN2 ( .D1(net7), .D2(IBSn_OUT), .S(VSS) ); 
CMC_PMOS_3x3 MP2_MP0 ( .D1(IBSp_OUT), .G(IBS_IN), .D2(net7), .S(VDD) ); 

endmodule

module Amp_diff_norm_rvt ( IBSn, IN, IP, ON, OP, VDD, VSS ); 
inout IBSn, IN, IP, ON, OP, VDD, VSS;

res_3p83 RR0 ( .ON(ON), .VDD(VDD) ); 
res_3p83 RR9 ( .OP(OP), .VDD(VDD) ); 
SCM_NMOS_4x4_4x3 MN3_MN0 ( .D1(IBSn), .D2(net39), .S(VSS) ); 
DP_NMOS_2x2_4x3 MN1_MN2 ( .D1(ON), .G1(IP), .S(net39), .D2(OP), .G2(IN) ); 

endmodule

module Amp_diff_norm_slvt ( IBSn, IN, IP, ON, OP, VDD, VSS ); 
inout IBSn, IN, IP, ON, OP, VDD, VSS;

res_3p83 RR0 ( .ON(ON), .VDD(VDD) ); 
res_3p83 RR9 ( .OP(OP), .VDD(VDD) ); 
SCM_NMOS_4x4_2x3 MN3_MN0 ( .D1(IBSn), .D2(net39), .S(VSS) ); 
DP_NMOS_2x2_2x3 MN1_MN2 ( .D1(ON), .G1(IP), .S(net39), .D2(OP), .G2(IN) ); 

endmodule

module IBS_norm_lvt ( IBS_IN, IBSn_OUT, IBSp_OUT, VDD, VSS ); 
inout IBS_IN, IBSn_OUT, IBSp_OUT, VDD, VSS;

DiodeConnected_PMOS_3x3 MP1 ( .D(IBS_IN), .S(VDD) ); 
SCM_NMOS_3x3 MN1_MN0 ( .D1(net7), .D2(IBSn_OUT), .S(VSS) ); 
CMC_PMOS_3x3 MP2_MP0 ( .D1(IBSp_OUT), .G(IBS_IN), .D2(net7), .S(VDD) ); 

endmodule

module Amp_diff_norm_lvt ( IBSn, IN, IP, ON, OP, VDD, VSS ); 
inout IBSn, IN, IP, ON, OP, VDD, VSS;

res_3p83 RR0 ( .ON(ON), .VDD(VDD) ); 
res_3p83 RR9 ( .OP(OP), .VDD(VDD) ); 
SCM_NMOS_4x4_2x3 MN3_MN0 ( .D1(IBSn), .D2(net39), .S(VSS) ); 
DP_NMOS_2x2_2x3 MN1_MN2 ( .D1(ON), .G1(IP), .S(net39), .D2(OP), .G2(IN) ); 

endmodule


// End HDL models
// Global nets module
`celldefine
module cds_globals;

supply0 VDD;
supply1 VSS;

endmodule
`endcelldefine