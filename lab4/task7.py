import string
def removepattern(word):
    punc = string.punctuation
    string = ""
    for p in punc:
        string = word.strip()
        string = word.replace(p,'')
    return string

def read(filename1,filename2):
     try:
        master = open(filename1,"r")
        slave = open(filename2,"w")
        for ma in master:
            new = removepattern(ma)
            slave.write(ma)
        print("File write operation completed successfully :-)")
     except:
        print("Oops something went wrong!!!")


x = input("Enter master file for copy operation:")
y = input("Enter slave file:")
read(x,y)

