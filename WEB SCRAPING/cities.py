from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

import time
from time import sleep
import sqlite3
import os
import pandas as pd
import numpy as np
import requests
import csv

import matplotlib.pyplot as plt
import ipywidgets as widgets
from ipywidgets import interact


# BAR PLOT

options = webdriver.ChromeOptions()
options.add_argument('--headless')

# Set a normal desktop browser User-Agent header
options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")

# Hide Selenium automation flags
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)

# Tell Chrome not to wait for background scripts or tracking pixels to finish loading
options.page_load_strategy = 'eager'

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),options=options)

driver.set_page_load_timeout(15)
driver.set_script_timeout(15)

try:
    driver.get("https://www.timeanddate.com/weather/")
    # Testing by retrieving the title
    print("\n", driver.title, "\n")


    # Extracting Datas from the most popular cities
    city_rows = driver.find_elements(By.CSS_SELECTOR, 'table tbody tr')
    city_weather_lists = []

    if city_rows:
        print("\n ---- MOST POPULAR CITIES DATA ---- \n")
        for row in city_rows:

            # Finding City Names and URLs
            city_elements = row.find_element(By.CSS_SELECTOR, 'td a')
            links = city_elements.get_attribute('href')
            name = city_elements.text.strip()

            # Finding Local Times
            time_elements = row.find_element(By.CSS_SELECTOR, 'td.r')
            times = time_elements.text.strip()

            # Finding each Temperature
            temp_elements = row.find_element(By.CSS_SELECTOR, 'td.rbi')
            temperature = temp_elements.text.strip()

            city_weather_lists.append({
                "City": name,
                "URL": links,
                "LocalTime": times,
                "Temperature": temperature
            })

    print(city_weather_lists)

except Exception as e:
    print(f"Error: {type(e).__name__}: {e}")

finally:    
    driver.quit()


# SAVE EXTRACTED DATA TO A CSV FILE
with open('city_scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["City", "URL", "LocalTime", "Temperature"])
    for data in city_weather_lists:
        writer.writerow([
            data["City"],
            data["URL"],
            data["LocalTime"],
            data["Temperature"]
        ])

# DATA CLEANING
df = pd.read_csv('city_scraped_data.csv')
print("\n --- DATAFRAME BEFORE CLEANING --- \n")
print(df)

# Remove the unnecessary symbols in certain columns
df['City'] = df['City'].str.replace('*', '', regex=False).str.strip()
df['Temperature'] = df['Temperature'].str.replace('°F', '', regex=False).str.strip()

# Convert the temperatures into an integers
df['Temperature'] = pd.to_numeric(df['Temperature'], errors="coerce")

# Changing the column name
df.rename(columns={'Temperature': 'Temperature (in Farenheit)'}, inplace=True)

# Creating a New column (Temperature in Celsius)
df['Temperature (in Celsius)'] = ((df['Temperature (in Farenheit)']- 32) * 5 / 9).round(1)


print("\n --- DATAFRAME AFTER CLEANING --- \n")
print(df)




# SAVE THE CLEAN AND TRANSFROMED DATA INTO SQLITE 
os.makedirs("DB", exist_ok=True)
DB_PATH = "DB/weather.db"

if os.path.exists(DB_PATH):
    os.remove(DB_PATH)

try:
    conn = sqlite3.connect(DB_PATH)
    df.to_sql('city_scraped_data.csv', conn, if_exists='replace', index=False)

except Exception as e:
    print(f"Error: {type(e).__name__}: {e}")

finally:    
    if conn:
        conn.close()


# DATA VISUALIZATION

# GENERAL PLOT
x_axis = df['City']
y_axis = df['Temperature (in Farenheit)']

plt.figure(figsize=(16, 6))
plt.xticks(rotation=45, ha='right', fontsize=9)
plt.tight_layout()

plt.bar(x_axis, y_axis, color=["blue","green"])
plt.title("Weather by Popular Cities")
plt.xlabel("City")
plt.ylabel("Temperature (in Farenheit)")
plt.show()

# TOP 10 HOTTEST CITIES PLOT
top_10_hot = df.nlargest(10, 'Temperature (in Farenheit)')

plt.figure(figsize=(10, 5))
plt.bar(top_10_hot['City'], top_10_hot['Temperature (in Farenheit)'], color='firebrick')
plt.xticks(rotation=45, ha='right')
plt.ylabel('Temperature (°F)')
plt.title('Top 10 Hottest Cities Right Now')
plt.tight_layout()
plt.show()

# BOXPLOT
plt.figure(figsize=(6, 6))

plt.boxplot(df['Temperature (in Celsius)'].dropna(), patch_artist=True,
            boxprops=dict(facecolor='lightblue', color='blue'))
plt.ylabel('Temperature (°F)')
plt.title('Global Temperature Range & Quartiles')
plt.show()

# FILTER CITIES ABOVE A CERTAIN THRESHOLD
def plot_above_temp(min_temp):
    filtered_df = df[df['Temperature (in Farenheit)'] >= min_temp]
    
    plt.figure(figsize=(12, 5))
    plt.bar(filtered_df['City'], filtered_df['Temperature (in Farenheit)'], color='orange')
    plt.xticks(rotation=45, ha='right')
    plt.ylabel('Temperature (°F)')
    plt.title(f'Cities with Temperature ≥ {min_temp} °F')
    plt.tight_layout()
    plt.show()

interact(plot_above_temp, min_temp=widgets.IntSlider(min=30, max=100, step=5, value=60));