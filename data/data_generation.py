# ==============================================================================
# DATA GENERATION & DIRTYING
# PURPOSE: To create and save a realistic, messy dataset for our analysis.
# This file simulates the process of receiving a "dirty" data file from a company's database or a third-party source.
# ==============================================================================

# --- Step 0: Import necessary libraries ---
import pandas as pd
import numpy as np

# --- Step 1: Initial Setup ---
# We set a "random seed" to ensure our results are reproducible.
np.random.seed(69)
print("--- Step 1: Setup Complete. Seed set to 69 for reproducibility. ---")

# --- Step 2: Define the Product Catalog ---
# This is the blueprint for our e-commerce store, "Digital Emporium".
# We create a nested dictionary to define our products.
# - The top-level keys are the 'category' names.
# - Inside each category, we have product names as keys.
# - For each product, we define:
#   - 'price': The base list price of the item.
#   - 'cost_factor': product_cost / list_price (a lower factor means a higher profit margin)
print("\n--- Step 2: Defining the product catalog... ---")
product_catalog = {
    'Electronics': {
        'Quantum Pro Soundbar': {'price': 399.99, 'cost_factor': 0.70}, 
        '4K Ultra HD TV (55 inch)': {'price': 799.99, 'cost_factor': 0.78}, 
        '4K Ultra HD TV (65 inch)': {'price': 1199.99, 'cost_factor': 0.80}, 
        'High-End Laptop (16-inch)': {'price': 2399.99, 'cost_factor': 0.82}, 
        'DSLR Camera Kit': {'price': 1499.99, 'cost_factor': 0.75}, 
        'Wireless Noise-Cancelling Headphones': {'price': 249.99, 'cost_factor': 0.65}, 
        'Premium In-Ear Headphones': {'price': 149.99, 'cost_factor': 0.60}, 
        'Smart Home Hub': {'price': 129.99, 'cost_factor': 0.62}, 
        'Smart Security Camera': {'price': 199.99, 'cost_factor': 0.68}, 
        '10-inch Tablet': {'price': 329.99, 'cost_factor': 0.72}, 
        'E-Reader Pro': {'price': 179.99, 'cost_factor': 0.70}, 
        'Bluetooth Speaker': {'price': 99.99, 'cost_factor': 0.60}, 
        'Gaming Mouse': {'price': 79.99, 'cost_factor': 0.55}, 
        'Mechanical Keyboard': {'price': 129.99, 'cost_factor': 0.58}, 
        'Portable Power Bank (20000mAh)': {'price': 49.99, 'cost_factor': 0.50}, 
        'USB-C Hub': {'price': 59.99, 'cost_factor': 0.52}, 
        'Webcam HD': {'price': 89.99, 'cost_factor': 0.57},
    }, 

    'Apparel': {
        'All-Weather Jacket': {'price': 119.99, 'cost_factor': 0.55}, 
        'Down Winter Coat': {'price': 249.99, 'cost_factor': 0.60}, 
        'Lightweight Windbreaker': {'price': 79.99, 'cost_factor': 0.50}, 
        'Denim Jacket': {'price': 99.99, 'cost_factor': 0.52}, 
        'Classic Cotton T-Shirt': {'price': 24.99, 'cost_factor': 0.40}, 
        'Graphic Print T-Shirt': {'price': 29.99, 'cost_factor': 0.42}, 
        'Long-Sleeve Henley': {'price': 39.99, 'cost_factor': 0.45}, 
        'Wool Sweater': {'price': 89.99, 'cost_factor': 0.50}, 
        'Flannel Shirt': {'price': 59.99, 'cost_factor': 0.48}, 
        'Denim Jeans': {'price': 89.99, 'cost_factor': 0.50}, 
        'Slim-Fit Chinos': {'price': 79.99, 'cost_factor': 0.48}, 
        'Performance Running Shorts': {'price': 39.99, 'cost_factor': 0.45}, 
        'Linen Trousers': {'price': 69.99, 'cost_factor': 0.47}, 
        'Leather Ankle Boots': {'price': 149.99, 'cost_factor': 0.58}, 
        'Canvas Sneakers': {'price': 69.99, 'cost_factor': 0.45}, 
        'Leather Belt': {'price': 49.99, 'cost_factor': 0.40}, 
        'Wool Scarf': {'price': 34.99, 'cost_factor': 0.35}, 
        'Designer Sunglasses': {'price': 179.99, 'cost_factor': 0.50},
    }, 
    
    'Home Goods': {
        'Artisan Ceramic Mug Set (4-pack)': {'price': 49.99, 'cost_factor': 0.50}, 
        'Non-Stick Cookware Set (10-piece)': {'price': 199.99, 'cost_factor': 0.65}, 
        'High-Powered Blender': {'price': 149.99, 'cost_factor': 0.60}, 
        'French Press Coffee Maker': {'price': 39.99, 'cost_factor': 0.48}, 
        'Electric Kettle': {'price': 49.99, 'cost_factor': 0.55}, 
        'Cast Iron Skillet': {'price': 69.99, 'cost_factor': 0.60}, 
        'Knife Block Set': {'price': 129.99, 'cost_factor': 0.62}, 
        'Air Fryer': {'price': 119.99, 'cost_factor': 0.68}, 
        'Egyptian Cotton Sheet Set (Queen)': {'price': 129.99, 'cost_factor': 0.55}, 
        'Down Alternative Comforter': {'price': 149.99, 'cost_factor': 0.58}, 
        'Plush Bath Towel Set': {'price': 79.99, 'cost_factor': 0.52}, 
        'Memory Foam Pillow': {'price': 59.99, 'cost_factor': 0.50}, 
        'Aromatherapy Diffuser': {'price': 59.99, 'cost_factor': 0.45}, 
        'Framed Wall Art': {'price': 99.99, 'cost_factor': 0.40}, 
        'Scented Candle (Large)': {'price': 29.99, 'cost_factor': 0.38}, 
        'Yoga Mat': {'price': 39.99, 'cost_factor': 0.42}, 
        'Weighted Blanket': {'price': 89.99, 'cost_factor': 0.55},
    }, 
    
    'Books': {
        'The Data Analyst\'s Handbook': {'price': 34.99, 'cost_factor': 0.35}, 
        'A Brief History of Everything': {'price': 19.99, 'cost_factor': 0.35}, 
        'The Art of Python Programming': {'price': 49.99, 'cost_factor': 0.40}, 
        'Investing 101': {'price': 24.99, 'cost_factor': 0.33}, 
        'Baking Illustrated': {'price': 29.99, 'cost_factor': 0.38}, 
        '30-Minute Meals': {'price': 22.99, 'cost_factor': 0.36}, 
        'Mystery of the Silent Lake': {'price': 14.99, 'cost_factor': 0.30}, 
        'The Sci-Fi Omnibus': {'price': 39.99, 'cost_factor': 0.42}, 
        'Bestselling Thriller': {'price': 18.99, 'cost_factor': 0.33}, 
        'Historical Fiction Saga': {'price': 21.99, 'cost_factor': 0.34}, 
        'Children\'s Picture Book': {'price': 12.99, 'cost_factor': 0.30}, 
        'Young Adult Fantasy Novel': {'price': 16.99, 'cost_factor': 0.32},
    }, 
    
    'Sports & Outdoors': {
        '2-Person Camping Tent': {'price': 129.99, 'cost_factor': 0.60}, 
        'Hiking Backpack (50L)': {'price': 149.99, 'cost_factor': 0.58}, 
        'Insulated Water Bottle': {'price': 29.99, 'cost_factor': 0.45}, 
        'Set of 2 Dumbbells (15lb)': {'price': 59.99, 'cost_factor': 0.65}, 
        'Bicycle Helmet': {'price': 49.99, 'cost_factor': 0.55}, 
        'Fishing Rod Combo': {'price': 89.99, 'cost_factor': 0.62},
    }
}

# "Flatten" the catalog from a dictionary into a list of dictionaries.
products = []
for category, items in product_catalog.items():
    for name, details in items.items():
        products.append({
            'product_name': name, 
            'category': category, 
            'list_price': details['price'], 
            'cost_factor': details['cost_factor']
        })

# Convert the list into a DataFrame, which is like a spreadsheet in Python.
product_df = pd.DataFrame(products)

# Assign a unique product_id to each product.
product_df['product_id'] = range(1001, 1001 + len(product_df))
print("--- Product catalog created successfully. ---")


# --- Step 3: Generate the "Pristine" Transaction Data ---
# This is the core of the data generation, where we simulate customer purchases.
print("\n--- Step 3: Generating 2,000,000 pristine transaction records... ---")

# Define the total number of transactions and the date range.
n_transactions = 2000000
start_date = pd.to_datetime('2022-01-01'); end_date = pd.to_datetime('2023-12-31')

# Date generation
# 1. Calculate the total number of days in our date range.
n_days = (end_date - start_date).days
# 2. Generate random integers from 0 to n_days. This is a small, safe range that avoids integer overflow.
random_day_offsets = np.random.randint(0, n_days, n_transactions)
# 3. Convert these integer offsets into Timedelta objects (e.g., 5 becomes '5 days').
date_offsets = pd.to_timedelta(random_day_offsets, unit='d')
# 4. Add the random day offsets to the start_date to create our initial random dates.
initial_dates = start_date + date_offsets

# Simulate order dates with a bias towards Q4 for holiday seasonality.
# 1. Identify which dates fall in Q4 (October, November, December).
q4_mask = initial_dates.month.isin([10, 11, 12])
# 2. For dates NOT in Q4, push them back in time randomly. This concentrates more sales in Q4.
dates = initial_dates.where(q4_mask, initial_dates - pd.to_timedelta(np.random.randint(0, 180, n_transactions), unit='d'))

# For each of the 2M transactions, randomly sample a product from our catalog.
# We use 'weights' to make the simulation more realistic (e.g., cheaper items might sell more often).
product_samples = product_df.sample(n_transactions, replace=True, weights=product_df['list_price'].rdiv(1).pow(0.5)).reset_index(drop=True)

# --- Simulate Discounts (Vectorized) ---
# Create an array of zeros, then fill in discounts based on category-specific rules.
discounts = np.zeros(n_transactions)
is_apparel = (product_samples['category'] == 'Apparel').values
is_electronics = (product_samples['category'] == 'Electronics').values
is_other = (~is_apparel & ~is_electronics)
# Apply different discount probabilities and amounts for each category segment.
apparel_rand = np.random.rand(n_transactions); discounts[is_apparel & (apparel_rand < 0.4)] = np.random.choice([0.10, 0.15, 0.20, 0.25, 0.30, 0.50], size=(is_apparel & (apparel_rand < 0.4)).sum())
electronics_rand = np.random.rand(n_transactions); discounts[is_electronics & (electronics_rand < 0.2)] = np.random.choice([0.05, 0.10, 0.15, 0.20], size=(is_electronics & (electronics_rand < 0.2)).sum())
other_rand = np.random.rand(n_transactions); discounts[is_other & (other_rand < 0.1)] = np.random.choice([0.05, 0.10], size=(is_other & (other_rand < 0.1)).sum())

# --- Calculate Prices, Quantities, and Costs (Vectorized) ---
# Calculate final price after discount.
final_prices = product_samples['list_price'].values * (1 - discounts)
# Simulate quantity: mostly 1, but a chance for more on cheaper items.
quantities = np.ones(n_transactions, dtype=int)
cheap_items_mask = final_prices < 50
quantities[cheap_items_mask] = np.random.choice([1, 2, 3], size=cheap_items_mask.sum(), p=[0.8, 0.15, 0.05])
# Simulate competitor prices to be close to our list price, with some random variation.
competitor_prices = product_samples['list_price'].values * np.random.uniform(0.92, 1.08, n_transactions)

# --- Assemble the Final Pristine DataFrame ---
# Combine all the generated arrays into a single pandas DataFrame.
df = pd.DataFrame({'order_id': range(50000, 50000 + n_transactions), 'order_date': dates, 'product_id': product_samples['product_id'], 'product_name': product_samples['product_name'], 'category': product_samples['category'], 'list_price': product_samples['list_price'], 'discount_applied': discounts, 'final_price': final_prices, 'quantity': quantities, 'product_cost': product_samples['list_price'] * product_samples['cost_factor'], 'competitor_price': competitor_prices})
df['order_date'] = pd.to_datetime(df['order_date']).dt.date
print("--- Pristine data generated. Starting the 'dirtying' process... ---")


# --- Step 4: Intentionally "Dirty" the Data ---
# This section simulates the common errors found in real-world datasets.
print("\n--- Step 4: Simulating real-world data issues... ---")
df_dirty = df.copy() # Work on a copy to keep the original pristine df for comparison if needed.

# 4a. Introduce more complex missing values (hidden nulls).
print("...adding hidden nulls (e.g., 'missing', 'N/A')")
missing_indices = df_dirty.sample(frac=0.03, random_state=1).index
df_dirty.loc[missing_indices, 'product_cost'] = np.random.choice(['missing', '-', 'N/A', np.nan], size=len(missing_indices))
df_dirty.loc[df_dirty.sample(frac=0.02, random_state=2).index, 'competitor_price'] = 'not available'

# 4b. Introduce mixed data types and formatting issues.
print("...adding mixed data types (e.g., '$ 199.99', '2 units')")
str_price_indices = df_dirty.sample(frac=0.05, random_state=3).index
df_dirty.loc[str_price_indices, 'final_price'] = df_dirty.loc[str_price_indices, 'final_price'].apply(lambda x: f"$ {x:,.2f}")
str_qty_indices = df_dirty.sample(frac=0.01, random_state=4).index
df_dirty.loc[str_qty_indices, 'quantity'] = df_dirty.loc[str_qty_indices, 'quantity'].astype(str) + ' units'

# 4c. Introduce more inconsistent category names.
print("...adding inconsistent text (e.g., 'Elec.', 'HOME GOODS')")
df_dirty['category'] = df_dirty['category'].replace({
    'Electronics': np.random.choice([' electronics ', 'Elec.', 'ELECTRONICS'], p=[0.5, 0.3, 0.2]),
    'Home Goods': np.random.choice(['Home Goods', 'HOME GOODS', 'Home & Garden'], p=[0.7, 0.2, 0.1]),
    'Apparel': 'Apparel '
})

# 4d. Introduce logical errors and outliers.
print("...adding logical errors (e.g., negative discount)")
logical_error_indices = df_dirty.sample(n=500, random_state=5).index
df_dirty.loc[logical_error_indices, 'final_price'] = df_dirty.loc[logical_error_indices, 'list_price'] * 1.1 # final_price is impossibly higher than list_price
df_dirty.loc[df_dirty.sample(n=200, random_state=6).index, 'discount_applied'] = -0.1 # A negative discount is illogical

# 4e. Introduce duplicate rows.
print("...adding duplicate rows")
duplicate_rows = df_dirty.sample(n=1000, random_state=7)
df_dirty = pd.concat([df_dirty, duplicate_rows]).reset_index(drop=True)

print("--- Data 'dirtying' process complete. ---")

# --- Step 5: Save the Dirty Dataset to a CSV file ---
print("\n--- Step 5: Saving the dirty dataset... ---")
df_dirty.to_csv('transactions_data.csv', index=False)
print(f"Successfully saved 'transaction_data.csv' with {len(df_dirty):,} rows.")