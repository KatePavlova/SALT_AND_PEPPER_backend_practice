from datetime import datetime, timedelta

def date_in_future(integer = None):
    date = datetime.now()
    if type(integer) is int:
        date += timedelta(days = integer)
    return date.strftime('%d-%m-%Y %H:%M:%S')

if __name__ == "__main__":
    print(date_in_future([]))     # => текущая дата
    print(date_in_future(2))      # => текущая дата + 2 дня
    print(date_in_future(35))     # => текущая дата + 35 дней
    print(date_in_future())       # => текущая дата
    print(date_in_future(True))   # => текущая дата




