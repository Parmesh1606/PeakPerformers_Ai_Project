Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import random

# Generate weather data for regions from 2012 to 2023
regions = ["North", "South", "East", "West", "Central", "Coastal", "Highlands"]
years = range(2012, 2024)  # Updated years
months = range(1, 13)

# Generate synthetic weather data
regional_data = []

for region in regions:
    for year in years:
        for month in months:
            if region == "North":
                temperature = round(random.uniform(-10, 10), 1)
                rainfall = round(random.uniform(0, 100), 1)
                humidity = round(random.uniform(40, 60), 1)
            elif region == "South":
                temperature = round(random.uniform(20, 35), 1)
                rainfall = round(random.uniform(50, 300), 1)
                humidity = round(random.uniform(60, 80), 1)
            elif region == "East":
                temperature = round(random.uniform(15, 30), 1)
                rainfall = round(random.uniform(100, 400), 1)
                humidity = round(random.uniform(50, 70), 1)
            elif region == "West":
                temperature = round(random.uniform(5, 25), 1)
                rainfall = round(random.uniform(20, 150), 1)
                humidity = round(random.uniform(40, 60), 1)
            elif region == "Central":
                temperature = round(random.uniform(10, 25), 1)
                rainfall = round(random.uniform(50, 200), 1)
                humidity = round(random.uniform(45, 65), 1)
            elif region == "Coastal":
                temperature = round(random.uniform(25, 35), 1)
                rainfall = round(random.uniform(150, 500), 1)
                humidity = round(random.uniform(70, 90), 1)
            elif region == "Highlands":
                temperature = round(random.uniform(-5, 15), 1)
                rainfall = round(random.uniform(20, 120), 1)
                humidity = round(random.uniform(50, 70), 1)

            # Append data
            regional_data.append([region, year, month, temperature, humidity, rainfall])

# Create a DataFrame
columns = ["Region", "Year", "Month", "Temperature", "Humidity", "Rainfall"]
data = pd.DataFrame(regional_data, columns=columns)

# Save to a CSV file
output_path = "C:/Users/Shanu Patel/Desktop/updated_weather_data_2012_2023.csv"  # Update to your path
data.to_csv(output_path, index=False)
... print(f"Weather data from 2012 to 2023 saved to: {output_path}")
... 
... # Visualize Trends
... sns.set(style="whitegrid")
... 
... # Group data by region and year for trend analysis
... regional_trends = data.groupby(['Region', 'Year']).mean().reset_index()
... 
... # Temperature trends
... plt.figure(figsize=(12, 6))
... sns.lineplot(data=regional_trends, x='Year', y='Temperature', hue='Region', marker='o')
... plt.title("Temperature Trends Across Regions (2012-2023)")
... plt.ylabel("Average Temperature (°C)")
... plt.xlabel("Year")
... plt.legend(title='Region')
... plt.grid(True)
... plt.show()
... 
... # Humidity trends
... plt.figure(figsize=(12, 6))
... sns.lineplot(data=regional_trends, x='Year', y='Humidity', hue='Region', marker='o')
... plt.title("Humidity Trends Across Regions (2012-2023)")
... plt.ylabel("Average Humidity (%)")
... plt.xlabel("Year")
... plt.legend(title='Region')
... plt.grid(True)
... plt.show()
... 
... # Rainfall trends
... plt.figure(figsize=(12, 6))
... sns.lineplot(data=regional_trends, x='Year', y='Rainfall', hue='Region', marker='o')
... plt.title("Rainfall Trends Across Regions (2012-2023)")
... plt.ylabel("Average Rainfall (mm)")
... plt.xlabel("Year")
... plt.legend(title='Region')
... plt.grid(True)
