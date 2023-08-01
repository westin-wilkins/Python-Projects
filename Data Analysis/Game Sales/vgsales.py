import pandas as pd
import matplotlib.pyplot as plt

# Year column contains 271 null values
df = pd.read_csv(r"Game Sales\vgsales.csv")
df.dropna(inplace=True)

# Sum duplicate genres to get the total global sales for each one
genre_sales_df = df.groupby("Genre")["Global_Sales"].sum().reset_index().sort_values("Global_Sales")
x_values_genre = genre_sales_df["Genre"]
y_values_global = genre_sales_df["Global_Sales"]

# Filter data to only include rows where platform = Nintendo
nintendo_df = df[df['Publisher'] == 'Nintendo']
nintendo_by_year_df = nintendo_df.sort_values("Year", ascending=False).reset_index().groupby("Year")["Global_Sales"].sum().reset_index()
x_values_nin_year = nintendo_by_year_df["Year"]
y_values_nin_sales = nintendo_by_year_df["Global_Sales"]

# Used sum to get yearly global sales
max_sales_year = nintendo_by_year_df.loc[nintendo_by_year_df["Global_Sales"].idxmax(), "Year"]
min_sales_year = nintendo_by_year_df.loc[nintendo_by_year_df["Global_Sales"].idxmin(), "Year"]

# Sum duplicate publishers to get global sales for each one
publisher_sales_df = df.groupby("Publisher")["Global_Sales"].sum().reset_index().sort_values("Global_Sales")
x_values_publisher = publisher_sales_df["Publisher"].tail(20)
y_values_pub_global_sales = publisher_sales_df["Global_Sales"].tail(20)

# Global sales by genre plot
plt.subplot(2, 2, 1)
plt.bar(x_values_genre, y_values_global)
plt.xlabel("Genres")
plt.ylabel("Global Sales")
plt.title("Global Sales by Genres")
plt.tick_params(axis='x', rotation=90)

# Global sales by publisher plot
plt.subplot(2, 2, 2)
plt.bar(x_values_publisher, y_values_pub_global_sales)
plt.xlabel("Publisher")
plt.ylabel("Global Sales")
plt.title("Global Sales by Publisher")
plt.tick_params(axis='x', rotation=90)

# Nintendo global sales plot
plt.subplot(2, 2, 3)
plt.plot(x_values_nin_year, y_values_nin_sales)
plt.xlabel("Year")
plt.ylabel("Global Sales")
plt.title("Yearly Nintendo Global Sales")

print("Year with highest global sales for Nintendo:", int(max_sales_year))
print("\nYear with lowest global sales for Nintendo:", int(min_sales_year))

plt.show()


