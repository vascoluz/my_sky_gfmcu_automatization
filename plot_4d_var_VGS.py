import sys
import os
from lib_circ import graf



Path = os.getcwd() #get current directory



#Path = "/home/vasco/Desktop/sky130A/sim_data/tran_charact"
if len(sys.argv) > 3:
    # Retrieve the input value from the command-line argument
    file_name1 = sys.argv[1]
    file_name2 = sys.argv[2]
    file_name3 = sys.argv[3]
    if os.path.exists(file_name1):
        print("good boy")
    else:
        print("file_non-existant")  # Verify if it exists
        sys.exit(1)

file_name1 = os.path.join(Path,file_name1)
file_name2 = os.path.join(Path,file_name2)
file_name3 = os.path.join(Path,file_name3)


graf.vgs_vs_id_gm_variation_4d_from_file(file_name1,file_name2,file_name3)