import string

def read_file(book):
    """Reads the given file, counts words and returns the dictionary"""
    d = dict()
    count = 0
    file = open(book)
    for line in book:
        line = line.replace("-"," ")
        words = line.split()
        for i in words:
            i = i.strip(string.punctuation + string.whitespace)
            i = i.lower()
            d[i] = d.get(i,0)+1
            count = count + 1
    return count,d

def print_dic(d):
    """Prints the histogram of dictionary"""
    print(len(d))
    for k,v in d.items():
        print(k,v)

def diff_words(d):
    diff_words = dict()
    for key in d.keys():
        if key not in diff_words:
            diff_words[key] = "none"
    return diff_words

def diff_words(d):
    """Prints the different words used in file"""
    dict_words=dict()
    for key in d.keys():
        if key not in dict_words:
            dict_words[key]="none"
    return dict_words

def compare_books(d1,d2):
    res = dict()
    for key in d1:
        if key not in d2:
            res[key] = None
    return res

def vocab(d1,d2):
    """Returns which book has more number of vocabulary"""
    if len(d1) > len(d2):
        return "Book 1"
    elif len(d2) > len(d1):
        return "Book 2"
    else:
        return None

count1,d1 = file_read("book1.txt")
print ("Total no. of words in book1: ",count1)
print_dict (d1)
dict_words = diff_words (d1)
print_dict (dict_words)
count2,d2 = file_read("book2.txt")
print ("Total no. of words in book2: ",count2)
d1md2 = compare_books(d1,d2)
d2md1 = compare_books(d2,d1)
print ("Best book with more vocabulary is: ",vocab(d1,d2))
