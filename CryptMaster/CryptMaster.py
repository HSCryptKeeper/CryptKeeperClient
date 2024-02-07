import httpx
import uuid
import SaltShaker

from time import sleep




class CryptMaster:
    def __init__(self, server, port=2053):
        self.SALT = SaltShaker.SALT
        self.system_id = uuid.getnode()
        self.server = f'https://{server}:{port}'

    def get_secret(self, requested_secret):
        payload = {"requested_password": requested_secret, 'system_id': self.system_id}
        url = f'{self.server}/get_secret'
        while True:
            response = httpx.post(url=url, json=payload, timeout=5, verify=False)
            if response.status_code != 200:
                print('Did not get a good response')
                sleep(20)
                continue
            response = response.json()
            secret = response.get('secret', None)
            status = response.get('response', None)
            if secret is not None:
                break
            else:
                print(status)
                sleep(20)
                continue
        return secret

    def enroll_server(self):
        payload = {'system_id': self.system_id, 'system_salt': self.SALT}
        url = f'{self.server}/enroll_server'
        while True:
            response = httpx.post(url=url, json=payload, timeout=5, verify=False)
            if response.status_code != 200:
                print('Did not get a good response')
                sleep(20)
                continue
            response = response.json()
            status = response.get('response', None)
            if status is not None:
                break
            else:
                print('Did not get a good response')
                sleep(20)
                continue
        return status



