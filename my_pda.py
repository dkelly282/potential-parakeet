import csv
print("List of family birthdays:")
with open('birthdays_and_age.csv','r') as data:
    reader = csv.reader(data)
    for row in reader:
        print (row)
