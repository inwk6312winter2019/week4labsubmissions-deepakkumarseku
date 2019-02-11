import string

def file_read(filename):
    """Reads a file and counts the words frequency and total word count"""
    fin=open(filename)
    count=0
    d=dict()
    for line in fin:
        line=line.replace("-"," ")
        word=line.split()
        for item in word:
            item=item.strip(string.punctuation + string.whitespace)
            item=item.lower()
            d[item]=d.get(item,0)+1
            count=count+1
    return count,d

def print_dict(d):
    """Prints the histogram dictionary"""
    list1=list()
    for key,value in d.items():
        list1.append((value,key))
    list1.sort(reverse=True)
    for word,value in list1[:20]:
        print(word, value, sep='\t')

count1,d1=file_read("prideandprejudice.txt")
print("Total no of words in book1 is ",count1)
print_dict(d1)
