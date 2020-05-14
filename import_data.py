frequency = 50 #Hz


import pandas as pd
import glob
import numpy as np

def importdata():
    src = "data"
    all_files = glob.glob(src + "/*.txt")
    li = []


    #Import all files as separate dataframes
    for filename in all_files:
        df = pd.read_csv(filename, names=["X","Y","Z","label"], index_col=None, sep=" ")
        li.append(df)

    fi = open("labels.txt","r")

    for line in fi:
        tokens = line.split()
        #print(tokens[0])
        #print(tokens[3] +":"+tokens[4])
        li[int(tokens[0])-1].iloc[int(tokens[3]):int(tokens[4]),3] = int(tokens[2])
        
    

    fi.close()
        
    #print(new_lbls)

    #frame = pd.concat(li, axis=0, ignore_index=True)

    return li