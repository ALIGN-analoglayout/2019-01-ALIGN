************************************************************************
* auCdl Netlist:
* 
* Library Name:  GF65_sim
* Top Cell Name: amp
* View Name:     schematic
* Netlisted on:  Jan  9 14:50:09 2019
************************************************************************

*.BIPOLAR
*.RESI = 2000 
*.RESVAL
*.CAPVAL
*.DIOPERI
*.DIOAREA
*.EQUATION
*.SCALE METER
*.MEGA
.PARAM



************************************************************************
* Library Name: USC_65nm_Release_Dec20_2018
* Cell Name:    inv_1x
* View Name:    schematic
************************************************************************

.SUBCKT inv_1x IN OUT vm vp
*.PININFO IN:I OUT:O vm:B vp:B
MT2 OUT IN vm vm nfet W=210.0n L=60n M=1 NF=1 MPL=1 mSwitch=0 idg=0 AD=33.6f 
+ AS=33.6f PD=740.0n PS=740.0n NRD=0.4762 NRS=0.4762 PTWELL=1 plnest=1 
+ plorient=1 pld200=1 pccrit=1 sa=1.6e-07 sb=1.6e-07 sd=0 p_vta=0 panw1=0p 
+ panw2=0p panw3=0p panw4=0p panw5=0p panw6=0p panw7=0p panw8=0p panw9=0p 
+ panw10=0p
MT1 OUT IN vp vp pfet W=410.0n L=60n M=1 NF=1 MPL=1 mSwitch=0 idg=0 AD=65.6f 
+ AS=65.6f PD=1.14u PS=1.14u NRD=0.2439 NRS=0.2439 pccrit=1 plnest=1 
+ plorient=1 pld200=1 sa=160.0n sb=160.0n sd=0 p_vta=0 panw1=0p panw2=0p 
+ panw3=0p panw4=0p panw5=0p panw6=0p panw7=0p panw8=0p panw9=0p panw10=0p
.ENDS

************************************************************************
* Library Name: GF65_sim
* Cell Name:    amp
* View Name:    schematic
************************************************************************

.SUBCKT amp gnda ib im ip om on op vdda1p2
*.PININFO gnda:I ib:I im:I ip:I on:I vdda1p2:I om:O op:O
RR1 o1m net49 $SUB=gnda $[opppcres] m=1 w=300n l=5u r=12.75K s=4 pbar=1 bp=1 
+ mSwitch=0
RR0 net49 o1p $SUB=gnda $[opppcres] m=1 w=300n l=5u r=12.75K s=4 pbar=1 bp=1 
+ mSwitch=0
MT4 o1p net49 vdda1p2 vdda1p2 pfet W=40u L=500n M=1 NF=8 MPL=1 mSwitch=0 idg=0 
+ AD=4p AS=4.6p PD=41.6u PS=51.84u NRD=0.0025 NRS=0.0025 pccrit=1 plnest=1 
+ plorient=1 pld200=1 sa=160.0n sb=160.0n sd=200n p_vta=0 panw1=0p panw2=0p 
+ panw3=0p panw4=0p panw5=0p panw6=0p panw7=0p panw8=0p panw9=0p panw10=0p
MT3 o1m net49 vdda1p2 vdda1p2 pfet W=40u L=500n M=1 NF=8 MPL=1 mSwitch=0 idg=0 
+ AD=4p AS=4.6p PD=41.6u PS=51.84u NRD=0.0025 NRS=0.0025 pccrit=1 plnest=1 
+ plorient=1 pld200=1 sa=160.0n sb=160.0n sd=200n p_vta=0 panw1=0p panw2=0p 
+ panw3=0p panw4=0p panw5=0p panw6=0p panw7=0p panw8=0p panw9=0p panw10=0p
MT27 vdda1p2 o1p op gnda natnfet W=20u L=300n M=1 NF=4 MPL=1 mSwitch=0 idg=0 
+ AD=2p AS=2.75p PD=20.8u PS=31.1u NRD=0.005 NRS=0.005 PTWELL=1 plnest=1 
+ plorient=1 pld200=1 pccrit=1 sa=175.00n sb=175.00n sd=200n p_vta=0 panw1=0p 
+ panw2=0p panw3=0p panw4=0p panw5=0p panw6=0p panw7=0p panw8=0p panw9=0p 
+ panw10=0p
MT24 vdda1p2 o1m om gnda natnfet W=20u L=300n M=1 NF=4 MPL=1 mSwitch=0 idg=0 
+ AD=2p AS=2.75p PD=20.8u PS=31.1u NRD=0.005 NRS=0.005 PTWELL=1 plnest=1 
+ plorient=1 pld200=1 pccrit=1 sa=175.00n sb=175.00n sd=200n p_vta=0 panw1=0p 
+ panw2=0p panw3=0p panw4=0p panw5=0p panw6=0p panw7=0p panw8=0p panw9=0p 
+ panw10=0p
MT2 o1m ip net47 gnda natnfet W=15.0u L=300n M=1 NF=3 MPL=1 mSwitch=0 idg=0 
+ AD=1.875p AS=1.875p PD=20.75u PS=20.75u NRD=0.0067 NRS=0.0067 PTWELL=1 
+ plnest=-1.0 plorient=-1.0 pld200=1 pccrit=1 sa=175.00n sb=175.00n sd=200n 
+ p_vta=0 panw1=0p panw2=0p panw3=0p panw4=0p panw5=0p panw6=0p panw7=0p 
+ panw8=0p panw9=0p panw10=0p
MT1 o1p im net47 gnda natnfet W=15.0u L=300n M=1 NF=3 MPL=1 mSwitch=0 idg=0 
+ AD=1.875p AS=1.875p PD=20.75u PS=20.75u NRD=0.0067 NRS=0.0067 PTWELL=1 
+ plnest=1 plorient=1 pld200=1 pccrit=1 sa=175.00n sb=175.00n sd=200n p_vta=0 
+ panw1=0p panw2=0p panw3=0p panw4=0p panw5=0p panw6=0p panw7=0p panw8=0p 
+ panw9=0p panw10=0p
MT30 ib onb vbn vdda1p2 pfet W=5u L=60n M=1 NF=1 MPL=1 mSwitch=0 idg=0 AD=800f 
+ AS=800f PD=10.32u PS=10.32u NRD=0.02 NRS=0.02 pccrit=1 plnest=1 plorient=1 
+ pld200=1 sa=160.0n sb=160.0n sd=0 p_vta=0 panw1=0p panw2=0p panw3=0p 
+ panw4=0p panw5=0p panw6=0p panw7=0p panw8=0p panw9=0p panw10=0p
MT54 gnda onb vbn gnda nfet W=5u L=60n M=1 NF=1 MPL=1 mSwitch=0 idg=0 AD=800f 
+ AS=800f PD=10.32u PS=10.32u NRD=0.02 NRS=0.02 PTWELL=1 plnest=1 plorient=1 
+ pld200=1 pccrit=1 sa=160.0n sb=160.0n sd=0 p_vta=0 panw1=0p panw2=0p 
+ panw3=0p panw4=0p panw5=0p panw6=0p panw7=0p panw8=0p panw9=0p panw10=0p
MT26 op vbn gnda gnda nfet W=10u L=500n M=6 NF=2 MPL=6 mSwitch=1 idg=0 AD=1p 
+ AS=1.6p PD=10.4u PS=20.64u NRD=0.01 NRS=0.01 PTWELL=1 plnest=1 plorient=1 
+ pld200=1 pccrit=1 sa=160.0n sb=160.0n sd=200n p_vta=0 panw1=0p panw2=0p 
+ panw3=0p panw4=0p panw5=0p panw6=0p panw7=0p panw8=0p panw9=0p panw10=0p
MT25 om vbn gnda gnda nfet W=10u L=500n M=6 NF=2 MPL=6 mSwitch=1 idg=0 AD=1p 
+ AS=1.6p PD=10.4u PS=20.64u NRD=0.01 NRS=0.01 PTWELL=1 plnest=1 plorient=1 
+ pld200=1 pccrit=1 sa=160.0n sb=160.0n sd=200n p_vta=0 panw1=0p panw2=0p 
+ panw3=0p panw4=0p panw5=0p panw6=0p panw7=0p panw8=0p panw9=0p panw10=0p
MT20 vbn vbn gnda gnda nfet W=10u L=500n M=1 NF=2 MPL=1 mSwitch=0 idg=0 AD=1p 
+ AS=1.6p PD=10.4u PS=20.64u NRD=0.01 NRS=0.01 PTWELL=1 plnest=1 plorient=1 
+ pld200=1 pccrit=1 sa=160.0n sb=160.0n sd=200n p_vta=0 panw1=0p panw2=0p 
+ panw3=0p panw4=0p panw5=0p panw6=0p panw7=0p panw8=0p panw9=0p panw10=0p
MT0 net47 vbn gnda gnda nfet W=10u L=500n M=20 NF=2 MPL=20 mSwitch=1 idg=0 
+ AD=1p AS=1.6p PD=10.4u PS=20.64u NRD=0.01 NRS=0.01 PTWELL=1 plnest=1 
+ plorient=1 pld200=1 pccrit=1 sa=160.0n sb=160.0n sd=200n p_vta=0 panw1=0p 
+ panw2=0p panw3=0p panw4=0p panw5=0p panw6=0p panw7=0p panw8=0p panw9=0p 
+ panw10=0p
MT31 gnda vbn gnda gnda nfet W=85.0u L=5u M=1 NF=17 MPL=1 mSwitch=0 idg=0 
+ AD=8.8p AS=8.8p PD=93.52u PS=93.52u NRD=0.0012 NRS=0.0012 PTWELL=1 plnest=1 
+ plorient=1 pld200=1 pccrit=1 sa=160.0n sb=160.0n sd=200n p_vta=0 panw1=0p 
+ panw2=0p panw3=0p panw4=0p panw5=0p panw6=0p panw7=0p panw8=0p panw9=0p 
+ panw10=0p
XI17 on onb gnda vdda1p2 / inv_1x
.ENDS

