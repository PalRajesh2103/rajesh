# Task-1: Read a File and Handle Errors Problem
# Statement: Write a Python program that:
# 1.Opens and reads a text file named sample.txt.
# 2. Prints its content line by line.
# 3.Handles errors gracefully if the file does not exist.

try:
    samplefile = open('sample.txt','r')   # Open() is used for open the specific file with mode
    #samplefile = open('sampl.txt', 'r')    # error : The file 'sampl.txt' was not found.
    reading=samplefile.read()
    print(reading)
    samplefile.close()                      # close is used for close the file.
except:
    print("The file 'sample.txt' was not found.")

#--------------------------------------------------------------------------------------------------------------


# Task-2:Write and Append Data to a File

# Problem Statement: Write a Python program that:
# 1.   Takes user input and writes it to a file named output.txt.
# 2.   Appends additional data to the same file.
# 3.   Reads and displays the final content of the file.

data=input("Enter text to write to the file: ")
outputfile = open('output.txt','w')
writingdata = outputfile.write(data)                        # write() is used to written the data in the file and return the number of character's
print(f"Data successfully written to the output.txt")
outputfile.close()

data1=input("Enter additional file to the append: ")
outputfile = open('output.txt','a')
appendingdata = outputfile.write("\n"+data1)                        # write() is used to written the data in the file and return the number of character's
print(f"Data successfully appended")
outputfile.close()

outputr=open('output.txt','r')
reading = outputr.read()
print("Final content of output.txt:\n",reading)
outputr.close()


