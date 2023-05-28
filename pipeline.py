import requests
import time
from loguru import logger

import config

def scrape_prices():
    # Old URL
    arzine_price_url = config.URL
    arzine_price_response = requests.get(arzine_price_url)
    arzine_price_data = arzine_price_response.json()

    arzine_buy_price = float(arzine_price_data['data']['buy_price'])  # Convert to float
    arzine_sell_price = float(arzine_price_data['data']['sale_price'])  # Convert to float

    # New URL
    abantether_url = 'https://abantether.com/management/all-coins/'
    abantether_response = requests.get(abantether_url)
    abantether_data = abantether_response.json()

    # Find symbol "USDT"
    usdt_data = next((coin for coin in abantether_data if coin['symbol'] == 'USDT'), None)
    if usdt_data:
        abantether_buy_price = float(usdt_data['priceBuy'])  # Convert to float
        abantether_sell_price = float(usdt_data['priceSell'])  # Convert to float
        logger.info(f"USDT Buy price (abantether): {abantether_buy_price}")
        logger.info(f"USDT Sell price (abantether): {abantether_sell_price}")
    else:
        logger.warning("USDT data (abantether) not found.")

    return arzine_buy_price, arzine_sell_price, abantether_buy_price, abantether_sell_price

# Configure logger
logger.add("price_scraping_logs_detail.log", rotation="50 MB", compression="zip", format="{time} {level} {message}")

try:
    arzine_buy_price, arzine_sell_price, abantether_buy_price, abantether_sell_price = scrape_prices()

    # Calculate difference
    if 'arzine_buy_price' in locals() and 'arzine_sell_price' in locals() and 'abantether_buy_price' in locals() and 'abantether_sell_price' in locals():
        usdt_buy_price_diff = abantether_buy_price - arzine_buy_price
        usdt_sell_price_diff = abantether_sell_price - arzine_sell_price
        logger.info(f"USDT Buy price difference: {usdt_buy_price_diff:+}")
        logger.info(f"USDT Sell price difference: {usdt_sell_price_diff:+}")
    else:
        logger.warning("USDT prices not available for comparison.")
except Exception as e:
    logger.error(f"An error occurred: {e}")