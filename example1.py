import csv
from faker import Faker
import json 


fake = Faker()

num_records = 10
fields = ['name','address',"phone_number","email"]

data = []

for i in range(num_records):
    data.append([fake.name(),fake.address(),fake.phone_number(),fake.email()])

print(data)
with open('data.csv', 'w') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(fields)
    csvwriter.writerows(data)
