import string

def file_read(filename):
    """Reads a file and return the words as a list"""
    fin=open(filename)
    word_list=list()
    for line in fin:
        line=line.strip()
        word_list.append(line)
    return word_list

def file_read1(filename):
    """Reads a file and counts the words frequency and total word count"""
    fin=open(filename)
    d=dict()
    for line in fin:
        line=line.replace("-"," ")
        word=line.split()
        for item in word:
            item=item.strip(string.punctuation + string.whitespace)
            item=item.lower()
            d[item]=d.get(item,0)+1
    return d

def compare_books(word_list,d1):
    res = list()
    for key in d1:
        if key not in word_list:
            res.append(key)
    return res

word_list=file_read("words.txt")
d=file_read1("prideandprejudice.txt")
res=compare_books(word_list,d)
print(res)
