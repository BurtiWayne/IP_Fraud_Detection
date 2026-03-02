import pandas as pd
import random
from faker import Faker
import os

fake = Faker()

# Automatically create data folder if not exists
os.makedirs("data", exist_ok=True)

rows = []

for i in range(10000):
    
    user_id = random.randint(1, 1000)
    ip_address = fake.ipv4()
    login_time = fake.date_time_between(start_date='-30d', end_date='now')
    latitude = random.uniform(-90, 90)
    longitude = random.uniform(-180, 180)
    country = fake.country()
    city = fake.city()
    device_id = fake.uuid4()
    isp = random.choice(["Airtel", "Jio", "Vodafone", "DataCenterISP"])

    rows.append([
        user_id, login_time, ip_address,
        device_id, latitude, longitude,
        country, city, isp
    ])

df = pd.DataFrame(rows, columns=[
    "user_id", "login_time", "ip_address",
    "device_id", "latitude", "longitude",
    "country", "city", "isp"
])
df.to_csv("D:/IP_Fraud_Project/data/generate_data.csv", index=False)

print("Dataset Created Successfully!")