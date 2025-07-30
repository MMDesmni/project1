# Importing libraries we need

import pandas as pd
import random

#Creating some datas for our data frame

names = ["Alice", "Bob", "Charlie", "Diana", "Ethan", "Fiona", "George", "Hannah", "Ivan", "Julia", "Kevin", "Liam", "Mia", "Noah", "Olivia", "Peter", "Quinn", "Rachel", "Sam", "Tina"]
product_names = [
    "Smartwatch X", "Gaming PC Pro", "Wireless Earbuds", "Designer Dress", "Mountain Bike",
    "Robotic Vacuum", "Coffee Maker", "External SSD", "Graphic Novel", "Yoga Mat",
    "Digital Camera", "VR Headset", "Electric Scooter", "Drone Pro", "Portable Speaker",
    "Blender", "Smart Lock", "Fitness Tracker", "Board Game", "E-Reader"
]
product_groups = ["electric", "toy", "cloth", "car", "book", "home", "sport"]
countries = [
    "Germany", "France", "Japan", "Brazil", "India", "Australia", "Spain", "Mexico",
    "Italy", "South Korea", "Sweden", "Norway", "Argentina", "Egypt", "South Africa"
]

data = []
num_rows_to_generate = 20 

#Using for loop and random library to make samples

for _ in range(num_rows_to_generate):
    name = random.choice(names)
    product_nai = random.choice(product_names)
    value = random.randint(10, 5000) 
    product_gro = random.choice(product_groups)
    country = random.choice(countries)
    number_s = random.randint(1, 10) 

    data.append({
        "name": name,
        "product nai": product_nai,
        "value": value,
        "product gro": product_gro,
        "country": country,
        "number(s)": number_s
    })

#In final part we create and have the file as excel type

df_new_rows = pd.DataFrame(data)

output_excel_file = "generated_product_data.xlsx"

df_new_rows.to_excel(output_excel_file, index=False) 
print(f"Successfully generated {num_rows_to_generate} new rows and saved to '{output_excel_file}'")


print("\nFirst 5 rows of the generated data:")
print(df_new_rows.head())
