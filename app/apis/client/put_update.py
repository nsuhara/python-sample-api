"""app/apis/client/put_update.py
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
        'statement': 'STAT_UPDATE'
    },
    {
        'id': 1,
        'transaction': 'update_sample1'
    }
])
headers = {
    'Content-Type': 'application/json'
}

res = requests.put(url=url, data=data, headers=headers)

print(res.status_code)
print(res.text)
