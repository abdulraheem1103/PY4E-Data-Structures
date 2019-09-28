# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count = 0
total = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    count = count + 1
    line_count = line.find(":")
    val = line[line_count+1 : ] 
    val = val.lstrip()
    val = float(val)
    total = total + val
    
#print("Done")
average = total/count

print('Average spam confidence:',average)
