v {xschem version=3.4.0 file_version=1.2
}
G {}
K {}
V {}
S {}
E {}
N 380 80 430 80 {
lab=VG}
N 470 80 560 80 {
lab=GND}
N 470 110 470 150 {
lab=GND}
N 470 10 470 50 {
lab=#net1}
N 50 390 50 420 {
lab=GND}
N 50 290 50 330 {
lab=VDD}
N 250 290 250 330 {
lab=VG}
N 470 150 470 190 {
lab=GND}
N 560 80 560 150 {
lab=GND}
N 470 150 560 150 {
lab=GND}
N 470 190 470 230 {
lab=GND}
N 250 390 250 420 {
lab=GND}
N 470 -90 470 -70 {
lab=VDD}
N 470 -10 470 10 {
lab=#net1}
C {sky130_fd_pr/nfet_01v8.sym} 450 80 0 0 {name=M2
L=l1
W=w1
nf=1 mult=1
model=nfet_01v8
spiceprefix=X
}
C {devices/code.sym} -10 20 0 0 {name=ngspice script
only_toplevel=true
format="tcleval( @value )"
value="
** opencircuitdesign pdks install
.lib $::SKYWATER_MODELS/sky130.lib.spice tt

.param VDD = 1.8
.param w1 = 1
.param l1 = 1.5
.TEMP 100


.control
  save all
  dc V_gate 0 1.8 0.0001
  plot i(V1)
  wrdata /home/vasco/Desktop/sky130A/TESTS/transistor_tests/nfet_01v8_dc_vgs.txt i(V1) 
  

.endc

"}
C {devices/vsource.sym} 50 360 0 0 {name=VDD value=VDD}
C {devices/vsource.sym} 250 360 0 0 {name=V_gate value=0
}
C {devices/gnd.sym} 50 420 0 0 {name=l2 lab=GND}
C {devices/gnd.sym} 470 230 0 0 {name=l4 lab=GND}
C {devices/lab_pin.sym} 380 80 0 0 {name=p1 sig_type=std_logic lab=VG}
C {devices/lab_pin.sym} 470 -90 0 0 {name=p2 sig_type=std_logic lab=VDD}
C {devices/lab_pin.sym} 250 290 0 0 {name=p3 sig_type=std_logic lab=VG
}
C {devices/lab_pin.sym} 50 290 0 0 {name=p4 sig_type=std_logic lab=VDD}
C {devices/gnd.sym} 250 420 0 0 {name=l1 lab=GND}
C {devices/ammeter.sym} 470 -40 0 0 {name=V1}
