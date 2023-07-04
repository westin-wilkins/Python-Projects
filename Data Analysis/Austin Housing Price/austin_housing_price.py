import pandas as pd
import matplotlib.pyplot as plt

# CSV Files
housing_df = pd.read_csv(r"austin_housing.csv")
unemployment_df = pd.read_csv(r"austin_unemployment.csv")

# Filter the data for Austin housing
austin_round_rock_df = housing_df[housing_df['Area'] == 'Austin-Round Rock']

# Set values for Austin housing
x_values_housing = austin_round_rock_df['Year']
y_values_housing = austin_round_rock_df['Overall_hpi']

# Set values for unemployment
x_values_unemployment = unemployment_df['Year']
y_values_unemployment = unemployment_df['Unemployment Rate']


plt.figure(figsize=(12,10))

# Graph of Overall_hpi and Year for Austin
plt.subplot(2,2,1)
plt.plot(x_values_housing, y_values_housing, label='Overall HPI')
plt.plot(x_values_housing, y_values_housing.ewm(span=10, adjust=False).mean(), label='EMA (10)')
plt.xlabel('Year')
plt.ylabel('Overall HPI')
plt.title('Austin HPI Moving Average')
plt.legend()

# Graph of the moving average of the unemployment rate
plt.subplot(2,2,2)
plt.plot(x_values_unemployment, y_values_unemployment, label='Austin Unemployment')
plt.plot(x_values_unemployment, y_values_unemployment.ewm(span=5, adjust=False).mean(), label='EMA (5)')
plt.xlabel('Year')
plt.ylabel('Unemployment')
plt.title('Austin Unemployment Rate Moving Average')
plt.legend()

# Graph of the Overall HPI
plt.subplot(2,2,3)
plt.bar(x_values_housing, y_values_housing, label='Overall HPI')
plt.xlabel('Year')
plt.ylabel('Overall HPI')
plt.title('Austin House Price Index')
plt.legend()

# Graph that compares the unemployment rate and HPI
fig, ax_left = plt.subplots()
ax_left.plot(x_values_unemployment, y_values_unemployment, color='blue')
ax_left.set_ylabel('Unemployment Rate')

ax_right = ax_left.twinx()
ax_right.plot(x_values_housing, y_values_housing, color='orange')
ax_right.set_ylabel('HPI')
plt.title('Austin HPI vs Unemployment Rate')
plt.show()
