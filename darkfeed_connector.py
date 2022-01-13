"""
API connector for the RansoMonitor By DarkFeed.
"""

import os
import time
from datetime import datetime

import requests


def get_feed(cookie: str=None, url: str='https://darkfeed.io/wp-json/wp/v2/posts/') -> list:
    """Get the feed and return a list of entries.

    Args:
        cookie (str, optional): Cookie to use for authentication. If None, use cookie.txt file. Defaults to None.
        url (str, optional): URl of the feed. Defaults to 'https://darkfeed.io/wp-json/wp/v2/posts/'.

    Returns:
        list: List of latest ransomware posts.
    """
    # Check if cookie is set
    if cookie is None:
        # Check if the cookie.txt file exists
        if not os.path.exists('cookie.txt'):
            with open("cookie.txt", "w", encoding="utf-8") as cookie_file:
                # Get the cookie and write it to the file
                cookie_file.write(input("Enter cookie value: ").strip())
        # If it does exist, read the cookie from the file
        with open("cookie.txt", "r", encoding="utf-8") as file:
            cookie = file.read()
    headers = {"Host": "darkfeed.io", "Cookie": cookie}

    return requests.get(url, headers=headers).json()


def scrape_feed():
    """Scrape the feed and print a list of entries."""
    # Get the feed data
    feed = get_feed()

    # Check if the log file exists
    if not os.path.exists('log.txt'):
        # If it doesn't, create it
        open('log.txt', "x", encoding="utf-8").close()

    # Check the log file for new entries
    with open("log.txt", 'r', encoding="utf-8") as log_file:
        log = log_file.read()

    # Get the new entries
    # Only include entries that are not in the log file
    new_entries = [post
                   for post in feed
                   if post["link"] not in log
                   ]

    if not new_entries:
        print("No new entries.\n")
        print('-' * 30 + '\n')
        return

    # Loop over the new_entries
    for entry in new_entries:
        # Get entry data
        date = datetime.strptime(entry["date"], "%Y-%m-%dT%H:%M:%S")
        link = entry["link"]
        group = entry['title']['rendered']
        victim = entry["excerpt"]["rendered"].replace("<p>", "").replace("</p>", "").strip()

        # Print the entry
        print('New Victim\n' \
             f'Group: {group}\n' \
             f'Victim: {victim}\n' \
             f'Date: {str(date)}\n' \
             f'Link: {link}\n'
            )
        print('-' * 30 + '\n')

        # Write the new entry to the log file
        with open("log.txt", "a", encoding="utf-8") as log_file:
            log_file.write(f'{link}\n')

        time.sleep(1)


if __name__ == '__main__':
    print()
    print("#" * 30)
    print("\n")
    print("RansoMonitor By DarkFeed")
    print("\n")
    print("#" * 30)
    print("\n")
    time.sleep(10)

    print("Building Current List From Feed.")
    print()
    print("Latest Victims On RansoMonitor:")
    print("\n")
    print("#" * 30)
    print()

    count = 1
    while True:
        scrape_feed()
        print(f'Number Of Runs: {count}')
        count += 1
        print()
        print("Done, next check in 60 Seconds")
        print()
        print("#" * 30)
        print()
        time.sleep(60)
