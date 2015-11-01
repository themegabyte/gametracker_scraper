# gametracker_scraper
Scrape server lists from gametracker.com

This script uses Selenium to scrape all server ips for a given game. 
The `get_urls.py` is used to determine which servers have web servers running on them.
The output of both tools is saved to a text file.

The reason I chose selenium was that the website prevented me from scraping it using tools like requests.

# Usage

    python selenium_scraper.py -s <searchterm>

example

    python selenium_scraper.py -s arma2
