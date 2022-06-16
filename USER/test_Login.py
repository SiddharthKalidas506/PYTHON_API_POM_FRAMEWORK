import requests

from Datafile import Creatuser
from Datafile import URLS
from USER import Readwrite
from Utilities.customLogger import logger


class Test_login():

    def test_login(self):
        payload = Creatuser.dataread.userlong()
        req = requests.post(URLS.allurl.loginurl(), json=payload)
        token = req.json()['token']
        print(token)
        path = "/Users/sikalidas/PycharmProjects/Python_API_Main/XL/API.xlsx"
        Readwrite.writeData(path, 'Sheet1', 2, 1, token)
        print(req.json())

    def test_Negativelogin(self):
        path = "/Users/sikalidas/PycharmProjects/Python_API_Main/XL/API.xlsx"
        payload = Creatuser.dataread.userlong()
        req = requests.post(URLS.allurl.loginurl(), json=payload)
        assert req.json() != "Unable to login"
        logger.info("**** User  email able to login ****")
        assert req.status_code == 200
        logger.info("**** User to login success code verification ****")

