from datetime import date
from datetime import datetime


class birthday:
    """This has a person birthday
        Attributes: year,month,date
    """
def age(birthday):
    """Age calculator
    Attributes: birthday YYYY-MM-DD
    returns: age in years
    """
    today = date.today()
    y = today.year - birthday.year
    if today.month < birthday.month or today.month == birthday.month and today.day < birthday.day:
        y -= 1
    return y

def bday_date_diff(birthday):
    """Calculates the tim euntil next birthday
        Attributes: birthday YYYY-MM-DD
        returns: age in years
        """
    today = date.today()
    now = datetime.now()
    t0=datetime(today.year,today.month,today.day,now.hour,now.minute,now.second)
    t1=datetime(today.year+1,birthday.month,birthday.day,00,00,00)
    t=t1-t0
    return t


def main():
    b=birthday()
    b.year=int(input("Enter the birth year YYYY:"))
    b.month =int(input("Enter the birth month MM:"))
    b.day = int(input("Enter the birth date DD:"))
    print("your current age is :",age(b))
    print("No of days until next birthday is:",bday_date_diff(b))

if __name__ == '__main__':
    main()
