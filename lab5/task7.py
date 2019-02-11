class time:
    """Represents the time of day.
    attributes: hour, minute, second
    """
def int_to_time(seconds):
    """Makes a new Time object.
    seconds: int seconds since midnight.
    """
    time1 = time()
    minutes, time1.second = divmod(seconds, 60)
    time1.hour, time1.minute = divmod(minutes, 60)
    return time1


def time_to_int(time):
    """Computes the number of seconds since midnight.
    time: Time object.
    """
    minutes = time.hour * 60 + time.minute
    seconds = minutes * 60 + time.second
    return seconds

def valid_time(time):
    """Checks whether a Time object satisfies the invariants.
    time: Time
    returns: boolean
    """
    if time.hour < 0 or time.minute < 0 or time.second < 0:
        return False
    if time.minute >= 60 or time.second >= 60:
        return False
    return True


def increment(time, seconds):
    """Adds seconds to a Time object."""
    assert valid_time(time)
    seconds += time_to_int(time)
    return int_to_time(seconds)

def main():
    t=time()
    t.hour=11
    t.minute=5
    t.second=30
    time1=increment(t,150)
    print("Incremented time is : %.2d:%.2d:%.2d" %(time1.hour,time1.minute,time1.second))

if __name__ == '__main__':
    main()
