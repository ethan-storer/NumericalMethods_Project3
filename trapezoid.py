def trapezoid(Y, X):
# Calculate integral using trapezoidal method

    length_X=(len(X)-1)

    I= [] #Keep a running list of array

    for i in range(length_X):
  
        A=X[i+1]
        B=X[i]
        Step=A-B
    
        Fa=Y[i+1]
        Fb=Y[i]
    
        Area=Step*((Fa+Fb)/2)
    
        Summation=sum(I)
    return(Summation)

