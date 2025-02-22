import pandas as pd  # Importing pandas for data manipulation
from matplotlib import pyplot as plt  # Importing matplotlib for visualization

# Reading the Excel file into a DataFrame
df = pd.read_excel("linechart.xlsx")
print(df.head())  # Display the first five rows of the dataset

# Creating a figure with a specific size for the line chart
plt.figure(figsize=(12, 4))

# Plotting sales data for different appliances over quarters
plt.plot(df["Quarter"], df["Fridge"], color="red", label="Fridge")
plt.plot(df["Quarter"], df["Dishwasher"], label="Dishwasher")
plt.plot(df["Quarter"], df["Washing Machine"], label="Washing Machine")

# Adding labels and title to the line chart
plt.xlabel('Quarter')
plt.ylabel('Sales')
plt.title('Appliance Sales Over Quarters')
plt.legend()  # Adding a legend to identify the lines

# Calculating total sales for each appliance category
total_sales = df[["Dishwasher", "Fridge", "Washing Machine"]].sum()
print(total_sales)  # Printing total sales

# Creating a pie chart to visualize the proportion of total sales
plt.pie(total_sales, labels=total_sales.index, autopct="%1.2f%%", 
        explode=(0.1, 0.1, 0.3), shadow=True, startangle=120)

# Creating a bar chart for sales data with "Quarter" on the x-axis
df.plot(kind="bar", x="Quarter")

# Setting "Quarter" as the index for easier plotting
df2 = df.set_index("Quarter")
print(df2)  # Displaying the modified DataFrame

# Creating another bar chart without specifying x, since "Quarter" is already set as index
df2.plot(kind="bar")

# Displaying all the plots
plt.show()
