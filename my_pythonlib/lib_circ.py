import subprocess
import os
import pandas as pd
import numpy as np
import re
import sys
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.patches as mpatches


class tonka:
    def my_2_input():
        if len(sys.argv) > 3:
            # Retrieve the input value from the command-line argument
            file_name = sys.argv[1]
            file_enviorement = sys.argv[2]
            sim_type = sys.argv[3]
            if os.getenv(file_enviorement) is not None:
                return file_name,file_enviorement,sim_type
            else:
                print("enviorement variable is non_existent, please fix") #verify if it exists
                sys.exit(1) 
        else:
            print("ERROR")
            print("insert file_name file_enviorement")
            print("dont forget to set up file envirement")
            print("file name without extention")
            sys.exit(1)

    
    def variation_paramn_simu(spice_path,data_path): #simulation with variation all in the same function
        param_name = input("Enter the paramameter desired to change: ")#get the param input
        starting_val = float(input("Enter the starting value: "))#starting value
        variation_val = float(input("Enter the variation value: "))#variation value
        number_of_times = int(input("number of times: "))#number of times
        current_val = starting_val#makes the written value the starting value
        ngspice_command = f'ngspice -b {spice_path}' #spice command   
        combined_data = pd.DataFrame()

        for a in range(0,number_of_times+1,1): # simple for
            with open(spice_path, 'r') as file: #opens the file
                lines = file.readlines()
            for i, line in enumerate(lines): #search the lines in the file
                if line.startswith('.param ' + param_name): # finds where is the line with param name
                    param_parts = line.split('=')
                    updated_line = f'.param {param_name} = {current_val}\n'
                    lines[i] = updated_line#substitutes the line
                    break
            with open(spice_path, 'w') as file: #writes the new file
                file.writelines(lines)
            current_val = current_val + variation_val #current value modification
            current_val = round(current_val,5)  #to compensate float precision in certain cases so we dont have 1.0000003 cause of float
            subprocess.run(ngspice_command, shell=True)#simulation
            data = pd.read_csv(data_path, delim_whitespace=True,header=None) #reads the data in the data path
            combined_data = pd.concat([combined_data, data], axis=1)
        combined_data = pd.DataFrame(combined_data.values)

        #column_count = combined_data.shape[1]
        #combined_data[column_count] = [param_name,starting_val,variation_val,number_of_times] #adds an information column
        return combined_data,param_name,starting_val,variation_val

    def get_spice_sch(file_name,file_enviorement):
        a = file_name + ".sch" #get sch name
        spice_file = file_name + ".spice" #get spice netlist name
        sch_file = os.environ.get(file_enviorement) #gets the path to the file in envirement
        sch_file = os.path.join(sch_file, a)#sch path
        if os.path.exists(sch_file): #checks if files exists
            return(sch_file,spice_file)
        else:
            print("ERROR: sch not found in that directory") # error
            sys.exit(1)


    def netlist_export(sch_path,enviorement_var):
        spice_path = os.environ.get(enviorement_var) # caminho para ele escrever o spice file
        xschem_command = f'xschem -n {sch_path} -o {spice_path} --no_x --quit' #comando para escrever o spice no x nao abre o xschem, --quit sai do xschem
        subprocess.run(xschem_command, shell=True)#realização do comando


    def ngspice_sim(spice_path):
        ngspice_command = f'ngspice -b {spice_path}' #comando da simulação batch com o ngspice
        subprocess.run(ngspice_command, shell=True)#simulação


    def finding(spice_path,pattern): #feito essencialmente para encontrar onde o wrdata esta
        with open(spice_path, 'r') as file: #abrir o ficheiro de forma segura o "r" significa que le
            text = file.read() #igual o ficheiro aonde se quer
        match = re.findall(pattern, text)
        if match:
            for match in match:
                 file_path = match  # Extract the file path from the match
                 print("File Path:", file_path)
                 return(file_path)
            else:
                 print("File paths not found in the SPICE netlist.")
                 return 0
            

    def corner(spice_path):
        print("type of corners?")
        print("a-full process corners")
        print("b-full process corners with temp")
        print("c-full process corners with temp and with VDD")
        print("d-Only Temp")
        print("e-Only VDD")
        print("f-VDD with TEMP")
        corner = input("Enter the desired corner: ")#get the param input
        corners = ["tt","ff","fs","ss","sf"] # process corners
        Temp_corners = [-10,27,80]#temperature corners

        match corner:
            case "a":
                for a in range(0, len(corners)):
                    with open(spice_path, "r") as file:
                        content= file.read()
                
                updated_content = content.replace(".lib $::SKYWATER_MODELS/sky130.lib.spice tt", f".lib $::SKYWATER_MODELS/sky130.lib.spice {corners[a]}")
                with open(spice_path, "w") as file:
                    file.write(updated_content)



            case _:
                print("invalid corner")
                sys.exit(1)

        
    













class graf:
    def vgs_vs_Id_gm(data_path): #plots ID and gm in function of VGS, without any corners/modification/ will be add later
        data = pd.read_csv(data_path, delim_whitespace=True,header=None) #divides the data
        vgs = data[0].to_numpy()# transforms vgs dataframe column into an array
        id = data[1].to_numpy()# transforms id dataframe column into an array
        id_mA = id / 1e-3#transforms the data to mA standart measurment data
        plt.figure(1)  # Set the figure size
        plt.plot(vgs, id_mA , color='red', linewidth=2, marker='o', markersize=1, label='ID')
        plt.xlabel("Vgs(V)")
        plt.ylabel("Id(mA)")
        plt.title("Id vs Vgs")
        plt.grid(True)  # Add gridlines
        plt.legend("Id current")  # Add legend
        gm = np.gradient(id, vgs)# transcondutance calculation
        plt.figure(2)  # Set the figure size
        plt.plot(vgs, gm , color='red', linewidth=2, marker='o', markersize=1, label='ID')
        plt.xlabel("Vgs(V)")
        plt.ylabel("gm(A/V)")
        plt.title("gm")
        plt.grid(True)  # Add gridlines
        plt.legend()  # Add legend
        plt.show()

    def vgs_vs_id_gm_variation(data,param_name):
        #data = data.drop(data.columns[-1], axis=1)#drop the last column, the information column

        Vgs = data.iloc[:, 0::2]  # Select odd columns starting from index 1
        Vgs = Vgs.values.T  # Co
        Id = data.iloc[:, 1::2]  # Select pair columns starting from index 0
        Id = Id.values.T  # Co
        gm = np.zeros_like(Id)
        Id_m = Id / 1e-3#transforms the data to mA standart measurment data

        plt.figure(1)  # Set the figure size
        for i in range(0,Vgs.shape[0],1):
            plt.plot(Vgs[i], Id_m[i], label=f"{param_name} {i+1}")
            gm[i] = np.gradient(Id[i], Vgs[i])  # Handle divide by zero and invalid value warnings

        plt.title("Id vs Vgs")
        plt.xlabel("Vgs")
        plt.ylabel("Id(ma)")
        plt.legend()
        plt.grid(True)  # Add gridlines
        plt.figure(2)  # Set the figure size
        for i in range(0,Vgs.shape[0],1):
            plt.plot(Vgs[i], gm[i], label=f"{param_name} {i+1}")
        plt.title("gm vs Vgs")
        plt.xlabel("Vgs")
        plt.ylabel("gm")
        plt.legend()
        plt.grid(True)  # Add gridlines
        plt.show()



    def vgs_vs_id_gm_variation_3d_from_file(data_path):
        pattern = r'.*test_(\w+)_([\d.]+)_([\d.]+)\.csv'#standart patter type of the file
        match = re.match(pattern, data_path)
        if match:
            param_name = match.group(1)  # Extract the parameter name
            starting_value = float(match.group(2))  # Extract the starting value
            variation = float(match.group(3))  # Extract the variation
        else:
             print("Invalid file name pattern.")
             sys.exit(1)
        data = pd.read_csv(data_path)
    
        Vgs = data.iloc[:, 0::2]  # Select odd columns starting from index 1
        Vgs = Vgs.values.T  # Co
        Id = data.iloc[:, 1::2]  # Select pair columns starting from index 0
        Id = Id.values.T  # Co
        gm = np.zeros_like(Id)
        z = np.zeros_like(Id)
        Id_m = Id / 1e-3#transforms the data to mA standart measurment data


        for a in range (0,len(Id),1): #prencher os valores z
            z[a] = starting_value + a*variation
            gm[a] = np.gradient(Id[a], Vgs[a])#gets the transcondutance
                                                
        fig = plt.figure()#basicly gets plots the 3D graph
        ax = fig.add_subplot(111, projection='3d')
        ax.plot_surface(Vgs, z, Id_m)
        ax.grid(True)
        ax.set_xlabel("Vgs",fontsize=12, fontweight='bold')
        ax.set_ylabel(param_name,fontsize=12, fontweight='bold')
        ax.set_zlabel('id(mA)',fontsize=12, fontweight='bold')
        ax.set_title('data plot')
        plt.show()


        fig = plt.figure() #plots the 3d graph of the transcondutance
        ax = fig.add_subplot(111, projection='3d')
        ax.plot_surface(Vgs, z, gm)
        ax.grid(True)
        ax.set_xlabel("Vgs",fontsize=12, fontweight='bold')
        ax.set_ylabel(param_name,fontsize=12, fontweight='bold')
        ax.set_zlabel('transcondutancia',fontsize=12, fontweight='bold')
        ax.set_title('data plot')
        plt.show()




    def vgs_vs_id_gm_variation_4d_from_file(data_path1,data_path2,data_path3):
        pattern = r'.*T(-?\d+)_L([\d.]+)_test_(\w+)_([\d.]+)_([\d.]+)\.csv'#standart patter type of the file #extracts a temperatura, L size e o resto

         # em geral todos os parmetros deverao ser iguais mas deixei isto para mostrar pode ser automtizado com um for secalhar no futuro
        match1 = re.match(pattern, data_path1)
        if match1:
            Temperature1 = float(match1.group(1))  # Extract the parameter name
            L_size1 = float(match1.group(2))  # Extract the starting value
            param_name1 = (match1.group(3))  # Extract the variation
            starting_value1 =float(match1.group(4))
            variation1 =float(match1.group(5))
        else:
             print("Invalid file name pattern.")
             sys.exit(1)

        match2 = re.match(pattern, data_path2)
        if match2:
            Temperature2 = float(match2.group(1))  # Extract the parameter name
            L_size2 = float(match2.group(2))  # Extract the starting value
            param_name2 = (match2.group(3))  # Extract the variation
            starting_value2 =float(match2.group(4))
            variation2 =float(match2.group(5))
        else:
             print("Invalid file name pattern.")
             sys.exit(1)
        
        match3 = re.match(pattern, data_path3)
        if match3:
            Temperature3 = float(match3.group(1))  # Extract the parameter name
            L_size3 = float(match3.group(2))  # Extract the starting value
            param_name3= (match3.group(3))  # Extract the variation
            starting_value3 =float(match3.group(4))
            variation3 =float(match3.group(5))
        else:
             print("Invalid file name pattern.")
             sys.exit(1)

        T = [Temperature1,Temperature2,Temperature3] # juntar as 3 temperaturas
    




        data1 = pd.read_csv(data_path1)
        data2 = pd.read_csv(data_path2)
        data3 = pd.read_csv(data_path3)


        #tratamento dos dados no datapath1
        Vgs1 = data1.iloc[:, 0::2]  # Select odd columns starting from index 1
        Vgs1 = Vgs1.values.T  # Co
        Id1 = data1.iloc[:, 1::2]  # Select pair columns starting from index 0
        Id1 = Id1.values.T  # Co
        gm1 = np.zeros_like(Id1)
        z1 = np.zeros_like(Id1)
        Id_m1 = Id1 / 1e-3#transforms the data to mA standart measurment data
        for a in range (0,len(Id1),1): #prencher os valores z
            z1[a] = starting_value1 + a*variation1
            gm1[a] = np.gradient(Id1[a], Vgs1[a])#gets the transcondutance

        #tratamento dos dados no datapath2
        Vgs2 = data2.iloc[:, 0::2]  # Select odd columns starting from index 1
        Vgs2 = Vgs2.values.T  # Co
        Id2 = data2.iloc[:, 1::2]  # Select pair columns starting from index 0
        Id2 = Id2.values.T  # Co
        gm2 = np.zeros_like(Id2)
        z2 = np.zeros_like(Id2)
        Id_m2 = Id2 / 1e-3#transforms the data to mA standart measurment data
        for a in range (0,len(Id2),1): #prencher os valores z
            z2[a] = starting_value2 + a*variation2
            gm2[a] = np.gradient(Id2[a], Vgs2[a])#gets the transcondutance


        #tratamento dos dados no datapath2
        Vgs3 = data3.iloc[:, 0::2]  # Select odd columns starting from index 1
        Vgs3 = Vgs3.values.T  # Co
        Id3 = data3.iloc[:, 1::2]  # Select pair columns starting from index 0
        Id3 = Id3.values.T  # Co
        gm3 = np.zeros_like(Id3)
        z3 = np.zeros_like(Id3)
        Id_m3 = Id3 / 1e-3#transforms the data to mA standart measurment data
        for a in range (0,len(Id3),1): #prencher os valores z
            z3[a] = starting_value3 + a*variation3
            gm3[a] = np.gradient(Id3[a], Vgs3[a])#gets the transcondutance


        fig = plt.figure()#basicly gets plots the 3D graph
        ax = fig.add_subplot(111, projection='3d')
        surf1 = ax.plot_surface(Vgs1, z1, Id_m1)
        surf2 = ax.plot_surface(Vgs2, z2, Id_m2)
        surf3 = ax.plot_surface(Vgs3, z3, Id_m3)
        ax.grid(True)
        ax.set_xlabel("Vgs",fontsize=12, fontweight='bold')
        ax.set_ylabel(param_name1,fontsize=12, fontweight='bold')
        ax.set_zlabel('id(mA)',fontsize=12, fontweight='bold')
        ax.set_title('ID VS VGS')

        surf1_proxy = mpatches.Patch(color=np.array(surf1._facecolors[0]))
        surf2_proxy = mpatches.Patch(color=np.array(surf2._facecolors[0]))
        surf3_proxy = mpatches.Patch(color=np.array(surf3._facecolors[0]))



        legend_labels = [f"T={T[0]}", f"T={T[1]}", f"T={T[2]}"]
        ax.legend([surf1_proxy, surf2_proxy, surf3_proxy], legend_labels, loc='best')
        plt.show()




        fig = plt.figure()#basicly gets plots the 3D graph
        ax = fig.add_subplot(111, projection='3d')
        surf1 = ax.plot_surface(Vgs1, z1, gm1)
        surf2 = ax.plot_surface(Vgs2, z2, gm2)
        surf3 = ax.plot_surface(Vgs3, z3, gm3)
        ax.grid(True)
        ax.set_xlabel("Vgs",fontsize=12, fontweight='bold')
        ax.set_ylabel(param_name1,fontsize=12, fontweight='bold')
        ax.set_zlabel('id(mA)',fontsize=12, fontweight='bold')
        ax.set_title('transcondutancia')

        surf1_proxy = mpatches.Patch(color=np.array(surf1._facecolors[0]))
        surf2_proxy = mpatches.Patch(color=np.array(surf2._facecolors[0]))
        surf3_proxy = mpatches.Patch(color=np.array(surf3._facecolors[0]))



        legend_labels = [f"T={T[0]}", f"T={T[1]}", f"T={T[2]}"]
        ax.legend([surf1_proxy, surf2_proxy, surf3_proxy], legend_labels, loc='best')
        plt.show()




                                                




        



        return 0









