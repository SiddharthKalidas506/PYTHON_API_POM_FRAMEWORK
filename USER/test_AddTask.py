import requests

from Datafile import Creatuser
from USER import Readwrite
from Utilities.customLogger import logger


class Test_UserUpdate():

    def test_UserProfile(self):
        path = "/Users/sikalidas/PycharmProjects/Python_API_Main/XL/API.xlsx"
        rw = Readwrite.getworcount(path, 'Sheet2')
        print(rw)
        ids=[]
        for i in range(1,rw):
            tex = Readwrite.readData(path, 'Sheet2', i, 2)
            print(tex)
            payloadtask = {
                "description": tex
            }
            payload = Creatuser.dataread.createuser()
            req = requests.post("https://api-nodejs-todolist.herokuapp.com/user/login", json=payload)
            tok = req.json()['token']
            print(tok)
            header = {"Authorization": "Bearer " + tok}
            req = requests.post("https://api-nodejs-todolist.herokuapp.com/task", json=payloadtask,
                                headers=header)
            print(req.json())
            ids.append(req.json()['data']['_id'])
        print(ids)

        header= {"Authorization": "Bearer " + tok}
        req = requests.get("https://api-nodejs-todolist.herokuapp.com/task", headers=header)
        print(req.json()['count'])
        # assert req.json()['count'] == var
        header = {"Authorization": "Bearer " + tok}
        var = "5"
        skip = "0"
        req = requests.get("https://api-nodejs-todolist.herokuapp.com/task?limit=" + var + "&skip=" + skip,
                           headers=header)
        print(req.json())
        assert req.json()['count'] == int(var)-int(skip)
        assert req.status_code == 200
        logger.info("**** get task success code verification****")