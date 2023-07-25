import subprocess
import os
import pandas as pd
import numpy as np
import re
from lib_circ import tonka
from lib_circ import graf
import sys


#basic script to only test single transistor chracteristics the charecteristics that are wanted is the Id relation with VG
#we will test with first with only basic simulation check
#second with w variation defined by user check
#third with L variation check
#with corner variation
#with temp and corner variation
# with vdd, temp and corner variation
# with montecarlo variation
#this is the objectives for now



pattern = r"wrdata\s+(\S+)"  #is to find written data that is define in the spice simulation, it always starts with wrdata
file_name,envirement_var,sim_type = tonka.my_2_input() #get the three inputs needed
sch_path,spice_name = tonka.get_spice_sch(file_name,envirement_var) #sch_path
tonka.netlist_export(sch_path,envirement_var) #extracts the spice file from sch and writes in enviroment_ar directory
enviorement_path = os.environ.get(envirement_var)#gets envirement path

spice_path = os.path.join(enviorement_path, spice_name)#spice file path
data_path = tonka.finding(spice_path,pattern) #gets the location and name of the data file when the spice is simulated
sim_data_path ="/home/vasco/Desktop/sky130A/sim_data/tran_charact"         #my custom data path










match sim_type :
    case "normal": #just simulates the extracted data without changes
        tonka.ngspice_sim(spice_path)#simulates the spice file
        graf.vgs_vs_Id_gm(data_path) # prints the id and gm
        file_name = file_name +".txt"
        sim_data_path = os.path.join(sim_data_path,file_name)
        subprocess.run(["cp", data_path, sim_data_path])
        #finished

    case "var":
       data = pd.DataFrame()
       data,param_name,starting_val,varitation_val = tonka.variation_paramn_simu(spice_path,data_path)
       graf.vgs_vs_id_gm_variation(data,param_name)
       file_name = file_name+"_"+str(param_name)+"_"+str(starting_val)+"_"+str(varitation_val)+".csv"
       file_name = os.path.join(sim_data_path,file_name)
       data.to_csv(file_name, index=False)



    case "corner":
        data = pd.DataFrame()
        tonka.corner(spice_path)
        
    case _:
        print("invalid sim type: sim intruduced")
        print("sim provided")
        sys.exit(1)




