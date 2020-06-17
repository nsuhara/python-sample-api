"""app/apis/client/delete_delete.py
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
        'statement': 'STAT_DELETE'
    },
    {
        'id': 1
    }
])
headers = {
    'Content-Type': 'application/json'
}

res = requests.delete(url=url, data=data, headers=headers)

print(res.status_code)
print(res.text)
