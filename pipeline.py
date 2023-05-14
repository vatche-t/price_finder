import requests
import time
from loguru import logger

import config

def scrape_prices():
    price_url = config.URL
    price_response = requests.get(price_url)
    price_data = price_response.json()

    buy_price = price_data['data']['buy_price']
    sell_price = price_data['data']['sale_price']

    return buy_price, sell_price

def upload_to_wordpress(buy_price, sell_price):
    # Code to upload prices to your WordPress site
    # This implementation depends on your WordPress setup and requirements
    # You may need to use a WordPress API or plugin to achieve this

    logger.info(f"Buy price: {buy_price}")
    logger.info(f"Sell price: {sell_price}")

# Configure logger
logger.add("price_scraping_logs_detail.log", rotation="50 MB", compression="zip", format="{time} {level} {message}")


try:
    buy_price, sell_price = scrape_prices()
    upload_to_wordpress(buy_price, sell_price)
except Exception as e:
    logger.error(f"An error occurred: {e}")
