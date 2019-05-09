import requests, json
from datetime import datetime


class Api:
    def __init__(self, api_base, token):
        self.api_base = api_base
        self.token = token

    def ban(self, login: str, start: datetime, end: datetime):
        startDate = str('{0:%Y-%m-%d}'.format(start))
        endDate = str('{0:%Y-%m-%d}'.format(end))
        payload = {'login': login, 'start': startDate, 'end': endDate}
        try:
            r = requests.post(self.api_base + "/admin/ban", data=payload, headers={'Authorization': self.token})
        except requests.exceptions.RequestException as e:
            return {'error': 'Something went wrong when connecting the server! \n('+str(e)+')'}
        return json.loads(r.text)
