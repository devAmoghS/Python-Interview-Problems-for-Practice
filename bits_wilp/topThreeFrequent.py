filepath = './sample.txt'
freq_counter = {}

# using context manager
with open(filepath, mode='r') as handle:
  content = handle.read()
  words = content.split()
  # file is closed now
  
for w in words:
  if w not in freq_counter.keys():
    freq_counter[w] = 1
  else:
    freq_counter[w] += 1

# sorting the sequence by values in `reverse` order
sorted_by_freq = sorted(freq_counter, key=freq_counter.get, reverse=True)

top_three = sorted_by_freq[:3]
for k in top_three:
  print(k, ":", freq_counter[k])
