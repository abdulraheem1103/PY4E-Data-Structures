name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

di = dict()
for line in handle:
	if line.startswith('From '):  #checks if the line startswith "From"
		line = line.split()         # splits the lines
		word = line[5]              #takes the word at 5th position
		word = word.split(':')      #split the 5th position with ":" (colons)
		hour = word[0]
		di[hour] = di.get(hour,0) + 1  #gets the key,value pairs from first position after splitting
        
list = []

for hour, count in di.items():
	list.append( (hour, count) )
    
list.sort()

for hour, count in list:
	print (hour, count)
  
