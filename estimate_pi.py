import numpy as np
from math import pi as PI

def estimate_pi(sims):
    """
    takes the number of simulations as input to estimate pi
    """
    
    # counter to hold points lying inside the circle
    in_circle = 0
    
    for s in range(0,sims):
        
        x = np.random.rand()
        y = np.random.rand()
        
        if (x**2 + y**2) <= 1:
            in_circle += 1
        
    # The ratio of pts. inside the circle and the total pts. will be same as the ratio
    # of the area of circle to the area of the square, inside which the circle is inscribed
    # Area of circle = PI * R * R
    # Area of square = (2R) * (2R)
    
    pi_estimated = 4.0 * in_circle / sims
    
    print("Simulations ran: ", sims)
    print("Estimated pi", pi_estimated)
    print("Error", PI - pi_estimated)

pow = 0
input_sims = 100
while pow <= 8:
    estimate_pi(sims=input_sims)
    pow += 1
    input_sims *= 10

