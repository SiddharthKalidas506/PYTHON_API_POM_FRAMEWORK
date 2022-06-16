import requests

import Datafile.Creatuser
from Datafile import URLS
from USER import Readwrite


class Test_Register():
    global token


    def test_Registers(self):
        payload = Datafile.Creatuser.dataread.createuser()
        print(payload)
        req=requests.post(URLS.allurl.createurl(),json=payload)
        print(req.json())
        token=req.json()['token']
        print(token)
        email=req.json()['user']['email']
        print(email)
        # password=req.json()['user']['password']
        name=req.json()['user']['age']
        age=req.json()['user']['name']
        path = "/Users/sikalidas/PycharmProjects/Python_API_Main/XL/API.xlsx"
        Readwrite.writeData(path,'Sheet1',2,1,token)
        Readwrite.writeData(path,'Sheet1',3,1,email)
        # Readwrite.writeData(path,'Sheet1',4,1,password)
        Readwrite.writeData(path, 'Sheet1', 5, 1, name)
        Readwrite.writeData(path, 'Sheet1', 6, 1, age)