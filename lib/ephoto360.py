from requests import Session
from bs4 import BeautifulSoup as bs

r = Session()

class ep:
    def __init__(self):
        self.BaseUrl = 'https://ephoto360.com{}'
        self.theme = {
            'pubglogo': '/tao-logo-pubg-truc-tuyen-nhieu-mau-sac-717.html',
        }

    def pubglogo(self, text):
        '''
        text = rainbow
        '''
        try:
            url = self.BaseUrl.format(self.theme['pubglogo'])
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