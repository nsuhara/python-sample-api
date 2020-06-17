"""app/apis/client/get_read_all.py
"""
import requests

from apis.client import URL

url = '{url}?service=SERV_SAMPLE&statement=STAT_READ_ALL'.format(**{
    'url': URL
})

res = requests.get(url=url)

print(res.status_code)
print(res.text)
