.GLOBAL vdd vss
* topology from "Gondi, Srikanth, and Behzad Razavi. "Equalization and clock and data recovery techniques for 10-Gb/s CMOS serial-link receivers." IEEE Journal of Solid-State Circuits 42, no. 9 (2007): 1999-2011."
*  Generated on: Nov  8 13:53:22 2018
*  Design library name: ssyoun_lib
*  Design cell name: ctle_gondi_jssc2007
*  Design view name: schematic

* Begin print save of Definition File List
*  Library name: ssyoun_lib
*  Cell name: ctle_gondi_jssc2007
*  View name: schematic
* ----------------------------
* SRCSTATUS NOTCHECKED
* TAG: opuslib 
* COUNTER: 9972 
* Version: Unmanaged 
* INPUT:  vp_in-vn_in  vn_in-vp_in 
* OUTPUT:  vp_out-vn_out  vn_out-vp_out 
* ----------------------------
*.PININFO  vp_in-vn_in:I  vn_in-vp_in:I 
*.PININFO  vp_out-vn_out:O  vn_out-vp_out:O 
* ----------------------------

Rrs m1s-m2s m2s-m1s r='1Meg'
Rrdn-rdp vdd vn_out-vp_out r='1Meg'
Rrdp-rdn vdd vp_out-vn_out r='1Meg'
Ccs m1s-m2s m2s-m1s c=1p
Cc0n-c0p vn_out-vp_out vss c=1p
Cc0p-c0n vp_out-vn_out vss c=1p
Ii11-i01 m2s-m1s vss DC=0
Ii01-i11 m1s-m2s vss DC=0
Mm1-m0 vn_out-vp_out vn_in-vp_in m2s-m1s vss nmos off=FALSE
Mm0-m1 vp_out-vn_out vp_in-vn_in m1s-m2s vss nmos off=FALSE


.END
