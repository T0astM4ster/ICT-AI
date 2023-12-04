import pandas as pd
import random

# Generating sample data for house prices and square footage
num_houses = 50  # Number of houses
min_price = 100000  # Minimum house price
max_price = 800000  # Maximum house price
min_sq_feet = 800  # Minimum square footage
max_sq_feet = 3000  # Maximum square footage

# Creating random data for house prices and square footage
house_prices = [random.randint(min_price, max_price) for _ in range(num_houses)]
square_feet = [random.randint(min_sq_feet, max_sq_feet) for _ in range(num_houses)]

# Creating a DataFrame
data = pd.DataFrame({
    'House_Price': house_prices,
    'Square_Feet': square_feet
})

# Saving the DataFrame to a CSV file
data.to_csv('house_prices_square_feet.csv', index=False)