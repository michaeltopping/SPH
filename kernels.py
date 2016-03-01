# this will contain all of the smoothing kernals used
import numpy as np

# find the magnitude of the difference between two vectors
def mag(r1, r2):
    r12 = r1-r2
    total = 0
    for ri in r12:
        total += ri**2
    return np.sqrt(total)


# this is the smoothing kernel W
def W(ri, rj, h):
    x = mag(rj,ri)/h
    A = 1/(np.pi*h**3)
    # check which regime the kernel should be in
    if x <= 1:
        return A*(1-1.5*x**2+.75*x**3)
    elif x <= 2:
        return A*.25*(2-x)**3
    else: 
        return 0



# this is the gradient of the kernel W
def gradW(ri, rj, h):
    x = mag(rj,ri)/h
    runit = (rj-ri)/mag(rj, ri)
    A = runit/(np.pi*h**4)
    # check which regime the the kernel should operate
    if x <= 1:
        return A*(9./4.*x**2-3*x)
    elif x <= 2:
        return -A*.75*(2-x)**2
    else:
        return np.array([0, 0, 0])
    
    
