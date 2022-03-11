import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def plot_interface(file_name,linestyle):
    data = np.loadtxt(file_name,skiprows=2)
    columns = ['x','y','z','alpha']
    df = pd.DataFrame(data=data,columns=columns,dtype='float') 
    df = df.sort_values('x')
    data = df.to_numpy()
    data = np.delete(data,np.where(data[:,2]!=0)[0],axis=0)
    plt.plot(data[:,0],data[:,1],linestyle=linestyle)

plot_interface('alpha.water_isoSurface.raw','dashed')
plt.show()
