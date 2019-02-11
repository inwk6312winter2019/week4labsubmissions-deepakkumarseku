class kangaroo:
    def __init__(self):
        self.pouch_contents=[]
    def put_in_pouch(self,other):
        if(isinstance(other,kangaroo)):
            self.pouch_contents.append(other.pouch_contents)
        else:
            self.pouch_contents.append(other)
    def __str__(self):
        return str(self.pouch_contents)

def main():
    kanga=kangaroo()
    roo=kangaroo()
    kanga.put_in_pouch("apple")
    kanga.put_in_pouch(1)
    roo.put_in_pouch("orange")
    kanga.put_in_pouch(roo)
    print(kanga)
    print(roo)

if __name__ == '__main__':
    main()

