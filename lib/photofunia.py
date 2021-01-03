from requests import Session
from bs4 import BeautifulSoup as bs

r = Session()

class tp:
    def __init__(self):
        self.BaseUrl = 'https://photofunia.com{}'
        self.theme = {
            'beachsign': '/categories/all_effects/beach-sign'
            }

    def beachsign(self, text):
        '''
        text = rainbow
        '''
        try:
            url = self.BaseUrl.format(self.theme['beachsign'])
            token = bs(r.get(url).text, 'html.parser').find('input', id='token')['value']
            data = {u'text[]': [u'%s' % text], 'submit': 'Go', 'token': token}
            result = self.BaseUrl.format(bs(r.post(url, data).text, 'html.parser').find('div', class_='btn-group').a['href'])
            return {
                'result': result
            }
        except Exception as e:
            print(e)
            return {
                'error': 'ERROR'
            }

