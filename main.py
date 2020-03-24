'''This program determines a week type, based on 2-weeks lap.

'''

from datetime import datetime as dt

# start week Monday date
year = 2020
month = 2
day = 3


def main(year, month, day, types=('первая', 'вторая')):
    start = dt(year=year, month=month, day=day)
    today = dt.now().date()
    delta = today-start
    delta -= delta % 7 # setting day to Monday

    if not delta % 14:
        return types[0]
    if not delta % 7:
        return types[1]
    return 'Some else'
    

main()
