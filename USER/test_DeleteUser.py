import requests

from Datafile import Creatuser, URLS
from USER import Readwrite


class Test_UserUpdate():

    def test_UserProfile(self):
        path = "/Users/sikalidas/PycharmProjects/Python_API_Main/XL/API.xlsx"
        toke = Readwrite.readData(path, 'Sheet1', 2, 1)
        print(toke)
        header = {"Authorization": "Bearer " + toke}
        req = requests.post(URLS.allurl.Updateprofile(), headers=header)