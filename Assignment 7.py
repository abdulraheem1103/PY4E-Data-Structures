# Use words.txt as the file name
fname = input("Enter file name: ") #took the input from the user
fh = open(fname) #used the open() function to open the file and using the iteration to read every line from 5th line
 
for line in fh:
    next_line = line.rstrip() #used the rstip() fuction to remove the spaces from left aswell the right
    new = next_line.upper() #used the upper() fuction to print the contents of the file in upper case
    print(new) 
