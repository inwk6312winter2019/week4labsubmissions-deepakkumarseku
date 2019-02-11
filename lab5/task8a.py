import calendar
from datetime import date

def main():
    my_date = date.today()
    print("Today's date :",my_date)
    print("Current day of the week is :",calendar.day_name[my_date.weekday()])


if __name__ == '__main__':
    main()
