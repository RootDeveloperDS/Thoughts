import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

x=np.arange(0,50)
y=x**x+4
plt.plot(x,y,color="green",linestyle="dashed")
#plt.hist(x)
plt.title("graph for algebric expression")
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.show()

A=[1,2,36,47,953,367,58,39,29]
B=['one','two','three','four','five','six','seven','eight','nine']
S1=pd.Series(A,B)
print(S1)
