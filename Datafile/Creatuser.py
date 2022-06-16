

class dataread():

    @staticmethod
    def createuser():
        payload={
                "name": "Siddharth kalidas",
                "email": "Siddharth@gmail.com",
                "password": "12345678",
                "age": 24
        }
        return payload
    @staticmethod
    def userlong():
        payload={
                "email": "Siddharth@gmail.com",
                "password": "12345678"
        }
        return payload
    @staticmethod
    def updateprofile():
        payload={
                "age": 26
        }
        return payload
    @staticmethod
    def Verification():
        payload= {
            "email": "Siddharth@gmail.com",
            "password": "12345678"
        }
        return payload
    @staticmethod
    def addtask():
        payload={
                "description": "reading book"
        }
