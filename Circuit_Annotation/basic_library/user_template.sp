.SUBCKT SCM_BANK IBS_IN IBSp_OUT net7 VDD 
MP2 IBSp_OUT IBS_IN VDD VDD slvtpfet m=4 l=14n nf=3 nfin=3 fpitch=48n cpp=78n 
MP1 IBS_IN IBS_IN VDD VDD slvtpfet m=1 l=14n nf=3 nfin=3 fpitch=48n cpp=78n 
MP0 net7 IBS_IN VDD VDD slvtpfet m=1 l=14n nf=3 nfin=3 fpitch=48n cpp=78n 
.ENDS
.SUBCKT SCM_CMBANK_LVCASCODE_P_7 vdda1p2 net0116 net0117 net0136 cnp cnm net085 net60 vbp net030 net63 vdda1p2 vdda1p2 net0123 net0116 net058 net060 net0117 net057 net062 net061
*vbp net60 net030 net63 net0136 cnm net085 cnp vdda1p2 vbb
MT64 net0136 vbp net0123 vbb lvtpfet W=20u L=180.0n M=4 NF=2 
MT69 cnp vbp net0117 vbb lvtpfet W=10u L=180.0n M=1 NF=1 
MT70 cnm vbp net0116 vbb lvtpfet W=10u L=180.0n M=1 NF=1 
MT26 net085 vbp net058 vbb lvtpfet W=20u L=180.0n M=8 NF=2 
MT23 net60 vbp net061 vbb lvtpfet W=20u L=180.0n M=60 NF=2 
MT27 vbp vbp net057 vbb lvtpfet W=20u L=180.0n M=1 NF=2 
MT19 net030 vbp net062 vbb lvtpfet W=20u L=180.0n M=41 NF=2 
MT24 net63 vbp net060 vbb lvtpfet W=20u L=180.0n M=60 NF=2 
MT59 net0123 vbp vdda1p2 vbb pfet W=20u L=600n M=4 NF=2 
MT62 net0116 vbp vdda1p2 vbb pfet W=10u L=600n M=1 NF=1 
MT50 net058 vbp vdda1p2 vbb pfet W=20u L=600n M=8 NF=2 
MT49 net060 vbp vdda1p2 vbb pfet W=20u L=600n M=60 NF=2 
MT61 net0117 vbp vdda1p2 vbb pfet W=10u L=600n M=1 NF=1 
MT22 net057 vbp vdda1p2 vbb pfet W=20u L=600n M=1 NF=2 
MT46 net062 vbp vdda1p2 vbb pfet W=20u L=600n M=41 NF=2 
MT48 net061 vbp vdda1p2 vbb pfet W=20u L=600n M=60 NF=2
.ENDS

.SUBCKT SCM_CMBANK_LVCASCODE_P_4 vbp net60 net030 net63 net0136 cnm net085 cnp vdda1p2 vbb
MT27 vbp vbp net057 vbb lvtpfet W=20u L=180.0n M=1 NF=2 
MT22 net057 vbp vdda1p2 vbb pfet W=20u L=600n M=1 NF=2 
MT23 net60 vbp net061 vbb lvtpfet W=20u L=180.0n M=60 NF=2 
MT48 net061 vbp vdda1p2 vbb pfet W=20u L=600n M=60 NF=2 
MT19 net030 vbp net062 vbb lvtpfet W=20u L=180.0n M=41 NF=2 
MT46 net062 vbp vdda1p2 vbb pfet W=20u L=600n M=41 NF=2 
MT24 net63 vbp net060 vbb lvtpfet W=20u L=180.0n M=60 NF=2 
MT49 net060 vbp vdda1p2 vbb pfet W=20u L=600n M=60 NF=2 
MT64 net0136 vbp net0123 vbb lvtpfet W=20u L=180.0n M=4 NF=2 
.ENDS

.SUBCKT SCM_CMBANK_LVCASCODE_N_2 net0135 net056 net029 gnda 
MT43 net0122 net0135 gnda gnda nfet W=10u L=500n M=6 NF=2 
MT10 net81 net0135 gnda gnda nfet W=10u L=500n M=24 NF=2 
MT8 net78 net0135 gnda gnda nfet W=10u L=500n M=24 NF=2 
MT65 net0135 net0135 net0122 gnda natnfet W=10u L=500n M=4 NF=2 
MT35 net056 net0135 net78 gnda natnfet W=10u L=500n M=16 NF=2 
MT34 net029 net0135 net81 gnda natnfet W=10u L=500n M=16 NF=2 
.ENDS

.SUBCKT SCM_CMBANK_4 D1 D2 D3 D4 GND
MT0 D3 D1 GND GND nfet W=10u L=500n M=6 NF=2 MPL=6 mSwitch=1 idg=0 AD=1p 
MT1 D2 D1 GND GND nfet W=10u L=500n M=6 NF=2 MPL=6 mSwitch=1 idg=0 AD=1p 
MT2 D1 D1 GND GND nfet W=10u L=500n M=1 NF=2 MPL=1 mSwitch=0 idg=0 AD=1p 
MT3 D4 D1 GND GND nfet W=10u L=500n M=20 NF=2 MPL=20 mSwitch=1 idg=0
.ENDS

.SUBCKT CAP_BANK ON VCM
CC7 ON VCM $[vncap] $SUB=VSS m=1 w=3.555u 
CC6 ON VCM $[vncap] $SUB=VSS m=1 w=3.555u 
CC5 ON VCM $[vncap] $SUB=VSS m=1 w=3.555u 
CC4 ON VCM $[vncap] $SUB=VSS m=1 w=3.555u 
.ENDS
