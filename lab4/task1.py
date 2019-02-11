import string

def file_read():
    """Reads a file and prints the words in the file"""
    fin=open("book.txt")
    count=0
    for line in fin:
        line = line.replace("-", " ")
        word=line.split()
        for item in word:
            item=item.strip(string.punctuation + string.whitespace)
            item=item.lower()
            print(item)
    return 0
    
print(file_read())
