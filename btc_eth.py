import json
import requests
import time
from time import sleep

# Key
api_endpoint = "https://api.binance.com/api/v3/ticker/price?symbol=ETHBTC"


import requests
import time

# Replace 'your_api_endpoint_here' with your actual API endpoint URL

# Initialize variables
previous_prices = []

while True:
    # Response from API
    data = requests.get(api_endpoint)

    # Check if the request was successful
    if data.status_code == 200:
        # Convert to JSON format for easy handling
        info = data.json()

        # Extracting the current price
        current_price = float(info["price"])
        print(f"Current price: {current_price}")

        # Add the current price to the list of previous prices
        previous_prices.append(current_price)

        # Keep only the last 60 prices in the list
        previous_prices = previous_prices[-60:]

        # Calculate the percentage change over the last 60 minutes
        price_change_percentage = (
            (current_price - previous_prices[0]) / previous_prices[0]
        ) * 100

        # Printing the result
        print(f"Price change over the last 60 minutes: {price_change_percentage:.2f}%")

        # Check if the price changed by 1%
        if abs(price_change_percentage) >= 1.0:
            print("Price changed by 1% in the last 60 minutes!")

    else:
        print(f"Error: Unable to fetch data. Status Code: {data.status_code}")

    # Introduce a delay to avoid making too many requests
    time.sleep(
        60
    )  # Adjust the sleep time based on your API rate limits and requirements
