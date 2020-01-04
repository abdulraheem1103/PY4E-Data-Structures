name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
nRead = handle.read()

counts = dict()    
for line in handle:
    if not line.startswith('From:'):   #checks if the line starts with From
        continue
    line = line.split()   #Split the lines
    line = line[1]     #takes the second word from the lines
    counts[line] = counts.get(line,0) + 1   #It counts key, values
    
#finds the maximum value
bigcount = None
bigword = None
for word,count in counts.items():
    if bigcount == None or count > bigcount:
        bigword = word
        bigcount = count
        
print(bigword, bigcount)
