from requests import Session
from bs4 import BeautifulSoup as bs

r = Session()

class tp:
    def __init__(self):
        self.BaseUrl = 'https://textpro.me{}'
        self.theme = {
            'neon_light': '/neon-light-text-effect-with-galaxy-style-981.html',
            'glitch': '/create-glitch-text-effect-style-tik-tok-983.html',
            'jokerlogo': '/create-logo-joker-online-934.html',
            'lionlogo': '/create-lion-logo-mascot-online-938.html',
            'ninjalogo': '/create-ninja-logo-online-935.html',
            'wolflogo1': '/create-wolf-logo-black-white-937.html',
            'wolflogo2': '/create-wolf-logo-galaxy-online-936.html',
            'blood': '/blood-text-on-the-frosted-glass-941.html',
            'dropwater': '/dropwater-text-effect-872.html'
            }

    def neon_light(self, text):
        '''
        text = rainbow
        '''
        try:
            url = self.BaseUrl.format(self.theme['neon_light'])
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

    def blood(self, text):
        '''
        text = rainbow
        '''
        try:
            url = self.BaseUrl.format(self.theme['blood'])
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

    def dropwater(self, text):
        '''
        text = rainbow
        '''
        try:
            url = self.BaseUrl.format(self.theme['dropwater'])
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

    def glitchz(self, text, text2):
        '''
        text = white text
        text2 = white text
        '''
        try:
            url = self.BaseUrl.format(self.theme['glitch'])
            token = bs(r.get(url).text, 'html.parser').find('input', id='token')['value']
            data = {u'text[]': [u'%s' % text,u'%s' % text2], 'submit': 'Go', 'token': token}
            result = self.BaseUrl.format(bs(r.post(url, data).text, 'html.parser').find('div', class_='btn-group').a['href'])
            return {
                'result': result
            }
        except Exception as e:
            print(e)
            return {
                'error': 'ERROR'
            }

    def jokerlogo(self, text):
        '''
        text = rainbow
        '''
        try:
            url = self.BaseUrl.format(self.theme['jokerlogo'])
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

    def lionlogo(self, text, text2):
        '''
        text = white text
        text2 = white text
        '''
        try:
            url = self.BaseUrl.format(self.theme['lionlogo'])
            token = bs(r.get(url).text, 'html.parser').find('input', id='token')['value']
            data = {u'text[]': [u'%s' % text,u'%s' % text2], 'submit': 'Go', 'token': token}
            result = self.BaseUrl.format(bs(r.post(url, data).text, 'html.parser').find('div', class_='btn-group').a['href'])
            return {
                'result': result
            }
        except Exception as e:
            print(e)
            return {
                'error': 'ERROR'
            }

    def wolflogo1(self, text, text2):
        '''
        text = white text
        text2 = white text
        '''
        try:
            url = self.BaseUrl.format(self.theme['wolflogo1'])
            token = bs(r.get(url).text, 'html.parser').find('input', id='token')['value']
            data = {u'text[]': [u'%s' % text,u'%s' % text2], 'submit': 'Go', 'token': token}
            result = self.BaseUrl.format(bs(r.post(url, data).text, 'html.parser').find('div', class_='btn-group').a['href'])
            return {
                'result': result
            }
        except Exception as e:
            print(e)
            return {
                'error': 'ERROR'
            }

    def wolflogo2(self, text, text2):
        '''
        text = white text
        text2 = white text
        '''
        try:
            url = self.BaseUrl.format(self.theme['wolflogo2'])
            token = bs(r.get(url).text, 'html.parser').find('input', id='token')['value']
            data = {u'text[]': [u'%s' % text,u'%s' % text2], 'submit': 'Go', 'token': token}
            result = self.BaseUrl.format(bs(r.post(url, data).text, 'html.parser').find('div', class_='btn-group').a['href'])
            return {
                'result': result
            }
        except Exception as e:
            print(e)
            return {
                'error': 'ERROR'
            }

    def ninjalogo(self, text, text2):
        '''
        text = white text
        text2 = white text
        '''
        try:
            url = self.BaseUrl.format(self.theme['ninjalogo'])
            token = bs(r.get(url).text, 'html.parser').find('input', id='token')['value']
            data = {u'text[]': [u'%s' % text,u'%s' % text2], 'submit': 'Go', 'token': token}
            result = self.BaseUrl.format(bs(r.post(url, data).text, 'html.parser').find('div', class_='btn-group').a['href'])
            return {
                'result': result
            }
        except Exception as e:
            print(e)
            return {
                'error': 'ERROR'
            }