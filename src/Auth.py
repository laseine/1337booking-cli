import requests, json, keyring

class Auth:

    def __init__(self, api_base):
        self.api_base = api_base

    def login(self, login: str, pwd: str):
        payload = {'login': login, 'pass': pwd}
        r = requests.post(self.api_base+"/login", data=payload)
        response = json.loads(r.text)
        if r.status_code == 200:
            keyring.set_password("system", "none", response['token'])
        return response

    def logout(self):
        if keyring.get_password("system", "none") is None:
            return {'error': 'You are not logged in.'}

        r = requests.get(self.api_base + "/logout", headers={'Authorization': keyring.get_password("system", "none")})
        response = json.loads(r.text)
        if r.status_code == 200:
            keyring.delete_password("system", "none")
            return {'good'}
        if response['error'] == 'Invalid token.':
            keyring.delete_password("system", "none")
        return response
