from requests import Session, get, post
from urllib.parse import urlencode
r = Session()
 
class PF:
    def __init__(self):
            self.host = 'https://api.photofunia.com{}?access_key=e3084acf282e8323181caa61fa305b2a&lang=en'
                    self.effects = {
                                'sand_writing': '/2.0/effects/sand_writing',
                                        }
    def sand_writing(self, text):
            url = self.host.format(self.effects['sand_writing'])
                    data = {'text': text}
                            result = post(url, data=data).json()
                                    return result['response']