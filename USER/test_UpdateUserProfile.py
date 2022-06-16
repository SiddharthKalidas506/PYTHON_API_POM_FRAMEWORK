import requests

from Datafile import Creatuser
from Datafile import URLS
from USER import Readwrite
from USER.test_Register_User import Test_Register


class Test_UserUpdate():

    def test_UserProfile(self):
        payload = Creatuser.dataread.updateprofile()
        print(payload)
        path = "/Users/sikalidas/PycharmProjects/Python_API_Main/XL/API.xlsx"
        toke = Readwrite.readData(path, 'Sheet1', 2, 1)
        print(toke)
        header = {"Authorization": "Bearer " + toke}
        print(header)
        req=requests.post(URLS.allurl.Updateprofile(),json=payload,headers=header)
        # print(req.json())