from datetime import date,timedelta
dt = date.today() - timedelta(5) #timedelta is used to add or subtract date frm current date
print(timedelta(5))
print("Current Date :",date.today())
print("5 Days before Current Date :", dt)