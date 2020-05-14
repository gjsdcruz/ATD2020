frequency = 50 #Hz


import pandas as pd
import glob
import numpy as np

def importdata():
    src = "/Users/guilhermecruz/Documents/LEI/ATD/2020/projeto/data"
    all_files = glob.glob(src + "/*.txt")
    li = []

    fi = open(src + "/labels.txt","r")

    for filename in all_files:
        df = pd.read_csv(filename, names=["X","Y","Z","label"], index_col=None, sep=" ")
        li.append(df)


    for line in fi:
        tokens = line.split()
        #print(tokens[0])
        #print(tokens[3] +":"+tokens[4])
        li[int(tokens[0])].loc[int(tokens[3]):int(tokens[4]),"label"] = int(tokens[2])
        print(li[int(tokens[0])])

    fi.close()
        
    #print(new_lbls)

    #frame = pd.concat(li, axis=0, ignore_index=True)

    return li