import requests

class URequests:

    @staticmethod
    def getUserId(email, password):
        if email == password:
            userid = 1
        else:
            userid = -1
        return userid

