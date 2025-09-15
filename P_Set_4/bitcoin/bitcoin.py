import sys
import requests

# Check if exactly one command-line argument is provided
if len(sys.argv) != 2:
    sys.exit("Missing command-line argument")

# Try to convert the argument to a float (number of Bitcoins)
try:
    n_bitcoins = float(sys.argv[1])
except ValueError:
    sys.exit("Command-line argument is not a number")

# Place your CoinCap API Key here
API_KEY = "74aacd3e77b97e1f219191315e13c45b3faceb6dcd473fc69cbb3a37484a2446"
url = f"https://rest.coincap.io/v3/assets/bitcoin?apiKey={API_KEY}"

try:
    # Send a GET request to the CoinCap API
    response = requests.get(url)
    response.raise_for_status()  # Raise an error if the request fails

    # Parse JSON response and extract Bitcoin price in USD
    data = response.json()
    price_usd = float(data["data"]["priceUsd"])
except requests.RequestException:
    sys.exit("Error: Could not fetch data from API")
except KeyError:
    sys.exit("Error: Unexpected response format")

# Calculate the total cost of n Bitcoins
total_cost = n_bitcoins * price_usd

# Print result with thousands separator and 4 decimal places
print(f"${total_cost:,.4f}")

# Mohammad_Reza_Mokhtari_Kia
