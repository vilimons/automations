import pandas as pd
import random
from faker import Faker
from random import randrange
from datetime import datetime   
from openpyxl import Workbook
from openpyxl.utils.dataframe import dataframe_to_rows
from win32com.client import Dispatch

pd.set_option('display.max_columns', None)

nr_of_customers = 2000

fake = Faker('de_DE')

customers = []

for customers_id in range(nr_of_customers):

    # Transactions Dates
    d1 = datetime.strptime(f'1/1/2021', '%m/%d/%Y')
    d2 = datetime.strptime(f'8/10/2022', '%m/%d/%Y')
    transaction_date = fake.date_between(d1, d2)

    # Create customer's name
    name = fake.name()

    # Create gender
    gender = random.choice(["M", "F"])

    # Create email
    email = fake.ascii_email()
    
    # Create City
    city = fake.city()

    # Create product ID in 8-digit barcode
    product_ID = fake.ean(length=8)

    # Create amount spent
    amount_spent = fake.pyfloat(right_digits=2, positive=True, min_value=1, max_value=100)
    
    customers.append([transaction_date, name, gender, email, city, product_ID, amount_spent])


# Create the DataFrame with the data we generated
df = pd.DataFrame(customers, columns=['Transaction_date', 'Name', 'Gender', 'Email', 'City', 'Product_ID', 'Amount_spent'])

workbook = Workbook()
sheet = workbook.active

for row in dataframe_to_rows(df, index=False, header=True):
    sheet.append(row)

workbook.save("pandas.xlsx")

xl = Dispatch("Excel.Application")
xl.Visible = True

wb = xl.workbooks.Open(r'C:\Users\Administrator\Desktop\projects\automations\excel-automation\data\pandas.xlsx')