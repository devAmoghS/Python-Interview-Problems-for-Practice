# Libraries Included:
# Numpy, Scipy, Scikit, Pandas

import pandas as pd
#print("Hello, world!")

def get_merged(series1, series2):
    merged = []
    temp = {}
    
    for i in series1:
        if i[0] not in temp.keys():
            temp[i[0]] = i[1]
        else:
            curr = temp.get(i[0])
            temp[i[0]] = (curr + i[1]) / 2

    for i in series2:
        if i[0] not in temp.keys():
            temp[i[0]] = i[1]
        else:
            curr = temp.get(i[0])
            temp[i[0]] = (curr + i[1]) / 2

    #print(temp)
    ordered = sorted(temp.items(), key=temp.items[1], reverse=False)
    #print(ordered)

    #for k,v in ordered.items():
     #   merged.append((k,v))
    
    return ordered
        
# timeseries data
series1 = [
 ('2010-01-01', 34), 
 ('2010-01-02', 27), 
 ('2010-01-04', 58), 
 ('2010-01-05', 22)]

series2 =  [
 ('2010-01-01', 15), 
 ('2010-01-03', 39), 
 ('2010-01-05', 23), 
 ('2010-01-06', 47)]

res = get_merged(series1, series2)
print(res)

# merged = [
# ('2010-01-01', 34), 
# ('2010-01-02', 27), 
# ('2010-01-03', 39), 
# ('2010-01-04', 58), 
# ('2010-01-05', 22.5), 
# ('2010-01-06', 47)]

# input array of series
# subfunc(inp_ser, temp) -> updated_temp
# keep track of series encounteered


# freq_dict -> (date, counter)
        
    for i in series1:
        if i[0] not in temp.keys():
            temp[i[0]] = i[1]
            freq_dict[i[0]] = 1
        else:
            curr = temp.get(i[0])
            freq_dict[i[0]] += 1
            temp[i[0]] = (curr + i[1]) / freq_dict.get(i[0])
        
        
        
        
        
