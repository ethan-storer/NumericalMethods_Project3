import numpy as np
def importcsv(testcsv, header = True):


    if header == True:
        data = np.genfromtxt('PatientA.csv',dtype=float, delimiter=',', skip_header=1) #Ignore first row
        
    
    else:
        data = np.genfromtxt('PatientA.csv',dtype=float, delimiter=',', skip_header=0) #Don't ignore first row
        

    print((data)) 
    a = data[:,0]
    b = data[:,1]
    return [a,b]
    
#numpy read text
#