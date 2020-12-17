# Process the string "k:1 |k1:2|k2:3|k3:4" into a dictionary {k:1,k1:2,...}

StringToProcess = "k:1 |k1:2|k2:3|k3:4" 

d2 = dict()
keyvalue_list = StringToProcess.split('|') # ['k:1' , 'k1:2' , 'k2:3' ,'k3:4']

for keyval in keyvalue_list:
  k,v = keyval.split(':') # (k,1) , (k1,2) , (k2,3) ,(k3,4)
  d2[k] = v


print(d2) # {'k': '1 ', 'k1': '2', 'k2': '3', 'k3': '4'}
