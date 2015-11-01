import requests
from requests.exceptions import ConnectionError, Timeout

with open('ips.txt', 'r') as f:
    with open('urls.txt', 'a') as urls:
        for ip in f.readlines():
            try:
                r = requests.get('http://'+ip[:-2], timeout=1)
                if r.status_code == 200 or 302 or 300 or 202:
                    urls.write(r.url+'\n')
                    print(r.url, '-', r.status_code)

            except ConnectionError:
                print('Trying new ip...\n')
                print('error - ', ip)
                continue

            except Timeout:
                print('Trying new ip...\n')
                print('error - ', ip)
                continue


