import csv
from datetime import datetime
now = datetime.now()
date = now.strftime("%d/%m/%Y")
print(f"Hello David\nToday's date is {date}")
print("List of family birthdays:")
with open('birthdays_and_age.csv','r') as data:
    reader = csv.reader(data)
    for row in reader:
        print (row)
    