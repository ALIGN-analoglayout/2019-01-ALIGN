//Verilog block level netlist file for netlist_BS_AMP
//Generated by UMN for ALIGN project 


module netlist_BS_AMP ( VDD ); 
inout VDD;
IBS_norm_rvt I34 ( .IBS_IN(net021), .IBSn_OUT(net038), .IBSp_OUT(net022), .VDD(VDD), .VSS(gnd!) );
IBS_norm_rvt I6 ( .IBS_IN(net013), .IBSn_OUT(net06), .IBSp_OUT(net032), .VDD(VDD), .VSS(gnd!) );
IBS_norm_lvt I44 ( .IBS_IN(net065), .IBSn_OUT(net059), .IBSp_OUT(net035), .VDD(VDD), .VSS(gnd!) );
IBS_norm_lvt I9 ( .IBS_IN(net011), .IBSn_OUT(net07), .IBSp_OUT(net012), .VDD(VDD), .VSS(gnd!) );
IBS_norm_hvt I22 ( .IBS_IN(net046), .IBSn_OUT(net042), .IBSp_OUT(net018), .VDD(VDD), .VSS(gnd!) );
IBS_norm_hvt I3 ( .IBS_IN(net015), .IBSn_OUT(net05), .IBSp_OUT(net031), .VDD(VDD), .VSS(gnd!) );
IBS_norm_slvt I47 ( .IBS_IN(net033), .IBSn_OUT(net061), .IBSp_OUT(net034), .VDD(VDD), .VSS(gnd!) );
IBS_norm_slvt I13 ( .IBS_IN(net010), .IBSn_OUT(net08), .IBSp_OUT(net014), .VDD(VDD), .VSS(gnd!) );
Amp_diff_norm_rvt I37 ( .IBSn(net022), .IN(net019), .IP(net020), .ON(rON), .OP(rOP), .VDD(VDD), .VSS(gnd!) );
Amp_diff_norm_lvt I51 ( .IBSn(net035), .IN(net066), .IP(net029), .ON(lON), .OP(lOP), .VDD(VDD), .VSS(gnd!) );
Amp_diff_norm_hvt I30 ( .IBSn(net018), .IN(net030), .IP(net028), .ON(hON), .OP(hOP), .VDD(VDD), .VSS(gnd!) );
Amp_diff_norm_slvt I43 ( .IBSn(net034), .IN(net062), .IP(net063), .ON(sON), .OP(sOP), .VDD(VDD), .VSS(gnd!) );
res_3k RR1 ( .VDD(VDD), .net05(net05) ); 
res_3k RR2 ( .VDD(VDD), .net06(net06) ); 
res_3k RR3 ( .VDD(VDD), .net07(net07) ); 
res_3k RR4 ( .VDD(VDD), .net08(net08) ); 
res_3k RR5 ( .net031(net031), .gnd!(gnd!) ); 
res_3k RR6 ( .net032(net032), .gnd!(gnd!) ); 
res_3k RR7 ( .net012(net012), .gnd!(gnd!) ); 
res_3k RR8 ( .net014(net014), .gnd!(gnd!) ); 

endmodule

module IBS_norm_slvt ( IBS_IN, IBSn_OUT, IBSp_OUT, VDD, VSS ); 
inout IBS_IN, IBSn_OUT, IBSp_OUT, VDD, VSS;

DiodeConnected_PMOS_3x3 MP1 ( .D(IBS_IN), .S(VDD) ); 
SCM_NMOS_3x3 MN1_MN0 ( .D1(net7), .D2(IBSn_OUT), .S(VSS) ); 
CMC_PMOS_3x3 MP2_MP0 ( .D1(IBSp_OUT), .G(IBS_IN), .D2(net7), .S(VDD) ); 

endmodule

module IBS_norm_hvt ( IBS_IN, IBSn_OUT, IBSp_OUT, VDD, VSS ); 
inout IBS_IN, IBSn_OUT, IBSp_OUT, VDD, VSS;

DiodeConnected_PMOS_4x3 MP1 ( .D(IBS_IN), .S(VDD) ); 
SCM_NMOS_4x3 MN1_MN0 ( .D1(net7), .D2(IBSn_OUT), .S(VSS) ); 
CMC_PMOS_4x3 MP2_MP0 ( .D1(IBSp_OUT), .G(IBS_IN), .D2(net7), .S(VDD) ); 

endmodule

module Amp_diff_norm_hvt ( IBSn, IN, IP, ON, OP, VDD, VSS ); 
inout IBSn, IN, IP, ON, OP, VDD, VSS;

res_3p83 RR0 ( .ON(ON), .VDD(VDD) ); 
res_3p83 RR9 ( .OP(OP), .VDD(VDD) ); 
SCM_NMOS_4x3 MN3_MN0 ( .D1(IBSn), .D2(net39), .S(VSS) ); 
DP_NMOS_4x3 MN1_MN2 ( .D1(ON), .G1(IP), .S(net39), .D2(OP), .G2(IN) ); 

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
SCM_NMOS_4x3 MN3_MN0 ( .D1(IBSn), .D2(net39), .S(VSS) ); 
DP_NMOS_4x3 MN1_MN2 ( .D1(ON), .G1(IP), .S(net39), .D2(OP), .G2(IN) ); 

endmodule

module Amp_diff_norm_slvt ( IBSn, IN, IP, ON, OP, VDD, VSS ); 
inout IBSn, IN, IP, ON, OP, VDD, VSS;

res_3p83 RR0 ( .ON(ON), .VDD(VDD) ); 
res_3p83 RR9 ( .OP(OP), .VDD(VDD) ); 
SCM_NMOS_2x3 MN3_MN0 ( .D1(IBSn), .D2(net39), .S(VSS) ); 
DP_NMOS_2x3 MN1_MN2 ( .D1(ON), .G1(IP), .S(net39), .D2(OP), .G2(IN) ); 

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
SCM_NMOS_2x3 MN3_MN0 ( .D1(IBSn), .D2(net39), .S(VSS) ); 
DP_NMOS_2x3 MN1_MN2 ( .D1(ON), .G1(IP), .S(net39), .D2(OP), .G2(IN) ); 

endmodule


// End HDL models
// Global nets module
`celldefine
module cds_globals;

supply0 VDD;
supply1 VSS;

endmodule
`endcelldefine