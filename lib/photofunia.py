from requests import Session
from bs4 import BeautifulSoup as bs

r = Session()

class px:
    def __init__(self):
        self.BaseUrl = 'https://photooxy.com{}'
        self.theme = {
            'shadow': '/logo-and-text-effects/shadow-text-effect-in-the-sky-394.html',
        }

    def shadow(self, text):
        '''
        text = rainbow
        '''
        try:
            url = self.BaseUrl.format(self.theme['shadow'])
            login = bs(r.get(url).text, 'html.parser').find('input', id='login')['value']
            data = {u'text[]': [u'%s' % text], 'submit': 'OK', 'login': login}
            result = self.BaseUrl.format(bs(r.post(url, data).text, 'html.parser').find('div', class_='btn-group').a['href'])
            return {
                'result': result
            }
        except Exception as e:
            print(e)
            return {
                'error': 'ERROR'
            }