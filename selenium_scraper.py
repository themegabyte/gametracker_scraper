from __future__ import print_function
from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException
import argparse


def write_ips(ips):
    for ip in ips:
        print(ip.text)
        with open('ips.txt', 'a') as f:
            f.write(ip.text + '\n')


def crawl(game):
    game = game.searchterm
    browser = webdriver.Firefox()
    page = 1
    crawling = True
    while crawling:
        url = 'http://www.gametracker.com/search/{0}/?searchipp=50&searchpge={1}#search'.format(game, page)
        browser.get(url)
        browser.implicitly_wait(10)
        ips = browser.find_elements_by_class_name('ip')
        write_ips(ips)
        next_button = browser.find_element_by_class_name('paging').text
        if 'NEXT' not in next_button:
            print('Hit last page...\nEnding Crawl...')
            crawling = False
            break
        page += 1

    browser.quit()


def parse_args():
    parser = argparse.ArgumentParser(description='Scrape gametracker.com server list and save the ips to a txt file')
    parser.add_argument("-s", "--searchterm", action="store",
                        help="specify a game to search", required=True)
    return parser.parse_args()


if __name__ == '__main__':
    crawl(parse_args())
