import requests

from Datafile import Creatuser, URLS


class Test_Logout():

    def test_Logout(self):
        payload = ""
        print(payload)
        req = requests.post(URLS.allurl.Logout(), json=payload)
        print(req.json())