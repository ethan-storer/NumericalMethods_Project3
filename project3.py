import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
from importcsv import *
data = importcsv('PatientA.csv')
#print(data)
A=4
k=0.013
X = data[0]
X_Plot = data[0]

Age = list(X)

Age_Plot = list(X_Plot)
Age_Plot.pop(0)
#print(Age_Plot)

P= data[1] #Pressure
Y=k*(P-13) #Function to integrate
#Empty arrays initialized for appending
my_Trapz_List=[]
Trapz_List=[]
Simps_List=[]

for i in range(2,len(Age)+1):
    from trapezoid import *
    myTrapz_area = trapezoid(Y[0:i],X[0:i]) 
    #print(myTrapz_area) =2.8274
    VL_myTrapz=A**(myTrapz_area) 
    #print(VL_myTrapz)
    my_Trapz_List.append(VL_myTrapz)
    #print(my_Trapz_List)
    #print(myTrapz_List)
    #print(VL_myTrapz) #=50.3877
    
    

    #VL_Trapz
    trapz_area = np.trapz(Y[0:i],X[0:i])
    #print(trapz_area) #=2.8274
    VL_Trapz=A**(trapz_area)
    #print(VL_Trapz)
    Trapz_List.append(VL_Trapz)
    
    #VL_Simpthird
    from scipy.integrate import simps
    simps_area = sp.integrate.simps(Y[0:i],X[0:i])
    #print(simps_area)  #=2.5963
    VL_Simps=A**(simps_area)
    #print(VL_Simps)
    Simps_List.append(VL_Simps)


#P vs time
fig, (ax1) = plt.subplots(1)
ax1.plot(Age, P, 'o', label='Patient A')
ax1.set_ylabel('Pressure (mm-Hg)')
ax1.set_xlabel('Age (Years)')
ax1.legend()
plt.show()

#VL vs time using different integration methods
fig, (ax2) = plt.subplots(1)
ax2.plot(Age_Plot,Simps_List , 'o', label='Simpsons Method') 
ax2.plot(Age_Plot,Trapz_List , 'v', label='Trapezoidal Integration')
ax2.plot(Age_Plot,my_Trapz_List , '^', label='Ethan Trapezoid Function')

#Label axes
ax2.set_ylabel('Vision Loss (Percentage)')
ax2.set_xlabel('Age (Years)')
ax2.legend()
plt.show()


