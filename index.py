python
import pandas as pd
import matplotlib.pyplot as plt
from fbprophet import Prophet

# Load the dataset
file_path = "water_consumption_data.csv"  # Replace with the actual file path
data = pd.read_csv(file_path)

# Inspect the data
print(data.head())

# Rename columns to match Prophet's requirements
data = data.rename(columns={"Year": "ds", "Water_Consumption_MCM": "y"})
data['ds'] = pd.to_datetime(data['ds'], format='%Y')

# Filter for a specific region (example: Etihad WE)
region_data = data[data['Region'] == 'Etihad WE']

# Initialize Prophet model
model = Prophet()
model.fit(region_data)

# Create future DataFrame for forecasting
future = model.make_future_dataframe(periods=5, freq='Y')
forecast = model.predict(future)

# Plot the forecast
fig = model.plot(forecast)
plt.title("Water Consumption Forecast for Etihad WE")
plt.xlabel("Year")
plt.ylabel("Water Consumption (MCM)")
plt.show()

# Save the forecast to a CSV file
forecast.to_csv("water_consumption_forecast.csv", index=False)
