from faker import Faker
fake = Faker(locale='en_US')
name = fake.name()

print(name)

job = fake.job()
print(job)
