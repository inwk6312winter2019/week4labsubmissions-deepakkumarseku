class time:
    """Represents the time of day.
    attributes: hour, minute, second
    """

def is_after(t1,t2):
    """Returns True if t1 is after t2; false otherwise."""
    return (t1.hour, t1.minute, t1.second) > (t2.hour, t2.minute, t2.second)

def main():
    t1=time()
    t1.hour=12
    t1.minute=5
    t1.second=9
    t2=time()
    t2.hour=11
    t2.minute=45
    t2.second=55
    print(is_after(t1,t2))

if __name__ == '__main__':
    main()
