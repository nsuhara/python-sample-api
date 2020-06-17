"""app/apis/client/get_read_one.py
"""
import requests

from apis.client import URL

url = '{url}?service=SERV_SAMPLE&statement=STAT_READ_ONE&id={id}'.format(**{
    'url': URL,
    'id': 1
})

res = requests.get(url=url)

print(res.status_code)
print(res.text)
