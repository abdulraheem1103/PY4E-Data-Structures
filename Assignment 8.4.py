fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    pieces = line.split()
    for i in pieces:
        if i not in lst:
            lst.append(i)
           

lst.sort()
print(lst)
