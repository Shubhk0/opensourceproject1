import pandas as pd
#import vaex as pd
path='big.txt'
cols_span=[(0,2)]
d=pd.read_fwf(path,widths=[2,4],chunksize=10,skip=0,sep="\t",header=None)
for chunk in d:
    for i in range(len(chunk)):
        a=chunk.iloc[i]
        print(str(a[0]))
        print(str(a[1]))
                                                I