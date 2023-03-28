from faker import Faker
import csv
import json

fake = Faker(locale='en_US')

def create_employee(num):
    employee_list = []
    for i in range(1,num):
        employee = {}
        employee['name'] = fake.name()
        employee['address'] = fake.address()
        employee['job'] = fake.job()
        employee['phone_number'] = fake.phone_number()
        employee['email'] = fake.email()
        employee['salary'] = fake.random_int(min=10000, max=100000, step=1)
        employee['company'] = fake.company()
        employee['ssn'] = fake.ssn()        
        employee_list.append(employee)

    return employee_list

def write_csv(employee_list):
    with open('employee.csv', 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        count = 0
        for employee in employee_list:
            if count == 0:
                header = employee.keys()
                csvwriter.writerow(header)
                count += 1
            csvwriter.writerow(employee.values())

def write_json(employee_list):
    with open('employee.json', 'w') as jsonfile:
        json.dump(employee_list, jsonfile)

if __name__ == '__main__':
    employee_list = create_employee(10)
    write_csv(employee_list)
    write_json(employee_list)

# Path: FakerData/dataset.py