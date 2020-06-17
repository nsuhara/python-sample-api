"""app/apis/client/post_upsert.py
"""
import json

import requests

from apis.client import URL

url = '{url}'.format(**{
    'url': URL
})
data = json.dumps([
    {
        'service': 'SERV_SAMPLE',
        'statement': 'STAT_UPSERT'
    },
    {
        'transaction': 'sample1'
    },
    {
        'transaction': 'sample2'
    }
])
headers = {
    'Content-Type': 'application/json'
}

res = requests.post(url=url, data=data, headers=headers)

print(res.status_code)
print(res.text)
