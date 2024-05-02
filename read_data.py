import pandas as pd

files = ["./data/data_classA.h5", "./data/data_classB.h5", "./data/data_classC.h5", 
        "./data/data_classD.h5", "./data/data_classE.h5", "./data/data_classF.h5", 
        "./data/data_classG.h5", "./data/data_classH.h5"]

for f in files:
    df = pd.read_hdf(f, "y")
    print(df.head())
    print("\n\n")