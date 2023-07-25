import sys
import os
from lib_circ import graf



Path = os.getcwd() #get current directory


#Path = "/home/vasco/Desktop/sky130A/sim_data/tran_charact"
if len(sys.argv) > 1:
    # Retrieve the input value from the command-line argument
    file_name = sys.argv[1]
    if os.path.exists(file_name):
        print("good boy")
    else:
        print("file_non-existant")  # Verify if it exists
        sys.exit(1)
file_name = os.path.join(Path,file_name)

graf.vgs_vs_id_gm_variation_3d_from_file(file_name)
