import requests
import os

def single_query(link, payload):
    response = requests.get(link, params=payload)
    if response.status_code != 200:
        print('WARNING', response.status_code)
    else:
        return response.json()

if __name__ == '__main__':
    link = 'http://api.nytimes.com/svc/search/v2/articlesearch.json'
    payload = {'api-key': 'K6auPXsmpT1c3sOI0KFgR9K50qOipDwp'}
    html_str = single_query(link, payload)
