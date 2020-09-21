from collections import Counter

with open('names.txt') as f:
  names = f.read().split('\n')


counts = Counter(names)
sorted = open('sorted','a')
outputstring = ''
print(counts)

for key in sorted(counts):
  #print(key, ' : ', value)
  outputstring = outputstring + key + " : " + str(counts[key]) + "\n"
  #string = key + ' : ' + str(value)
  #sorted.write(string)

sorted.write(outputstring)  
sorted.close()