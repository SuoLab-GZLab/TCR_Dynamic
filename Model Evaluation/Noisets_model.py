

#importing libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from noisets import noisettes as ns

import os
import pandas as pd
import glob


directory = "/home/xumeng/TCR_Dynamic/Ex_model_test/HCL/data4noiset/data/"
# directory = "/home/xumeng/TCR_Dynamic/Ex_model_test/HCL/data4noiset/data1/"


csv_files = glob.glob(os.path.expanduser(os.path.join(directory, "*.csv")))  

dataframes_dict = {}

for file_path in csv_files:
   
    file_name = os.path.splitext(os.path.basename(file_path))[0]
    
    try:
        df = pd.read_csv(file_path)
       
        dataframes_dict[file_name] = df
        print(f"Successfully loaded: {file_name}")
    except Exception as e:
        print(f"Failed to read {file_name}: {str(e)}")


dataframes_list = list(dataframes_dict.items())


print("\nDataFrame list:")
for name, df in dataframes_list:
    print(f"- {name}: {df.shape[0]} x {df.shape[1]}")


## NB


#Parameters of the noise model learnt in part II.
paras = [ -1.97822857,   1.25456411,   1.04465803, -10.14630235]
# Negative Binomial Sampling Noise Model
noise_model = 1 

expansion = ns.Expansion_Model() # Creating an object for which the associated methods are linked to the contraction/expansion
pval_threshold = 1  #Parameters to play with
smed_threshold = -10000 # Parameters to play with


base_path = '/home/xumeng/TCR_Dynamic/Ex_model_test/HCL/data4noiset/NB/'

for name, df in dataframes_list:
    print(f"- {name}: {df.shape[0]} x {df.shape[1]}")
    
    outpath = f'{base_path}Ex_NB_{name}_P1_'
    
    print(f"outpath: {outpath}")

    expansion.expansion_table(outpath, paras, paras, df, noise_model, pval_threshold, smed_threshold)
    


## NP

#Parameters of the noise model learnt in part II.
paras = [ -2.0, 1.54, 1.23, 6.65, -9.71]
# NB + Poisson
noise_model = 0 

expansion = ns.Expansion_Model() # Creating an object for which the associated methods are linked to the contraction/expansion
pval_threshold = 1  #Parameters to play with
smed_threshold = -10000 # Parameters to play with


base_path = '/home/xumeng/TCR_Dynamic/Ex_model_test/HCL/data4noiset/NP/'


for name, df in dataframes_list:
    print(f"- {name}: {df.shape[0]} x {df.shape[1]}")

    outpath = f'{base_path}Ex_NP_{name}_P1_'

    
    print(f"outpath: {outpath}")

    expansion.expansion_table(outpath, paras, paras, df, noise_model, pval_threshold, smed_threshold)
    


## P

#Parameters of the noise model learnt in part II.
paras = [ -2.15, -9.47]
# Poisson
noise_model = 2 

expansion = ns.Expansion_Model() # Creating an object for which the associated methods are linked to the contraction/expansion
pval_threshold = 1  #Parameters to play with
smed_threshold = -10000 # Parameters to play with


base_path = '/home/xumeng/TCR_Dynamic/Ex_model_test/HCL/data4noiset/P/'


for name, df in dataframes_list:
    print(f"- {name}: {df.shape[0]}行 x {df.shape[1]}列")
    
    outpath = f'{base_path}Ex_Poisson_{name}_P1_'
    
    print(f"outpath: {outpath}")

    expansion.expansion_table(outpath, paras, paras, df, noise_model, pval_threshold, smed_threshold)




