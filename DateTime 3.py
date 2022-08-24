import datetime
today = datetime.date.today()
yesterday = today - datetime.timedelta(days = 1)
tommorrow = today + datetime.timedelta(days = 1)
print("YESTERDAY :", yesterday)
print("TODAY :", today)
print("TOMMORROW :", tommorrow)