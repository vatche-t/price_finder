# Price Scraping from arzine.org and WordPress Upload

This Python script scrapes prices from a specified URL and uploads them to a WordPress site. It utilizes the `requests` library for HTTP requests, the `loguru` library for logging, and a configuration file (`config.py`) for storing the URL.


## How to Run
1. Clone the repository to your local machine.
2. Ceate virtual env
-   python3.10 -m venv .venv
-   source .venv/bin/activate

### In addition, run the update_debs.sh script to update any necessary Debian packages. Run the following command:

```bash
./scripts/update_debs.sh
```

+ Install the required Python packages using pip:

```linux
pip install -r requirements.txt
```
## Usage

1. Run the script using the following command:


```css
python3 main.py
```
- The script will continuously scrape the prices every second from the specified URL and upload them to your WordPress site. It will log the process and any errors encountered in the price_scraping_logs.log file.

## Configuration

You can configure the script by modifying the following variables:

- `URL`: Update the URL in config.py to the desired source for scraping prices.

- `WordPress Integration`: Modify the upload_to_wordpress function to suit your WordPress setup. This may involve using a WordPress API, plugin, or other integration method to upload the prices to your WordPress site.

`Logging`: Adjust the log file name, rotation settings, compression, and log format in the logger.add statement to match your preferences.

## Logging

The script uses the Loguru library for logging. The log file (`app.log`) will be created in the same directory as the script. It rotates every 1 week, and the log level is set to INFO. You can modify the log configuration in the script if needed.

+ the file will execute every `20` second(deafult)

Last updated on: 2024-02-12

Last updated on: 2024-02-12

Last updated on: 2024-02-13

Last updated on: 2024-02-25

Last updated on: 2024-02-26

Last updated on: 2024-03-01

Last updated on: 2024-03-04

Last updated on: 2024-03-09

Last updated on: 2024-03-13

Last updated on: 2024-03-15

Last updated on: 2024-03-18

Last updated on: 2024-03-25

Last updated on: 2024-03-26

Last updated on: 2024-03-26

Last updated on: 2024-03-30

Last updated on: 2024-04-02

Last updated on: 2024-04-03

Last updated on: 2024-04-03

Last updated on: 2024-04-09

Last updated on: 2024-04-13

Last updated on: 2024-04-16

Last updated on: 2024-04-17

Last updated on: 2024-04-20

Last updated on: 2024-04-22

Last updated on: 2024-04-22

Last updated on: 2024-04-26

Last updated on: 2024-05-05

Last updated on: 2024-05-05

Last updated on: 2024-05-05

Last updated on: 2024-12-03

Last updated on: 2024-12-03

Last updated on: 2024-12-04

Last updated on: 2024-12-06

Last updated on: 2024-12-06