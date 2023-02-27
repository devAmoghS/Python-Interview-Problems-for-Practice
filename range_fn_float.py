# Make a range function that works for `float` inputs

def float_for(start, stop, increment, stop_inclusive=True):  
  if stop_inclusive:
    stop += increment
    
  while start < stop:
    # The yield statement returns a `generator` object to 
    # the one who calls the function which contains yield, 
    # instead of simply returning a value.
    yield start
    start += increment


for i in float_for(0.5, 0.95, 0.05):
  print(i)
  
"""
Output:

0.5
0.55
0.6000000000000001
0.6500000000000001
0.7000000000000002
0.7500000000000002
0.8000000000000003
0.8500000000000003
0.9000000000000004
0.9500000000000004
"""
