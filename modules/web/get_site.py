import os
import sys
import requests


SITE_URL = 'https://www.google.com'

def get_site(url):
    return requests.get(SITE_URL)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        SITE_URL = sys.argv[1]
    print(get_site(SITE_URL))
