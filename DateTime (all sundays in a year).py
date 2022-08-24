from datetime import date,timedelta

def all_sundays(year):
    # january 1st of given year
    dt = date(year,1,1)
    # 1st sunday of given year
    dt = dt + timedelta(days=6 - dt.weekday())
    while dt.year == year:
        yield dt
        dt = dt + timedelta(days=7)

for s in all_sundays(2022):
    print(s)