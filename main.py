#from lib.pytube import YouTube
from lib.dewa import cari
from lib.anime import *
from lib.brainly import *
from lib.manga import *
from lib.resize import *
from lib.search import *
from lib.nulis import *
from lib.textpro import tp
from urllib.parse import *
from urllib.request import *
from flask import *
from flask import Flask, request, abort, redirect, jsonify
from kbbi import KBBI, AutentikasiKBBI
from werkzeug.exceptions import *
#from werkzeug.utils import *
from bs4 import BeautifulSoup as bs
from requests import get, post
import os, math, json, random, re, html_text, pytesseract, base64, time, smtplib, html5lib, kbbi

ua_ig = 'Mozilla/5.0 (Linux; Android 10; Redmi Note 9 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.127 Mobile Safari/537.36'

tp = tp()
app = Flask(__name__)
app.config['MEDIA'] = 'result'
app.secret_key = b'BB,^z\x90\x88?\xcf\xbb'
abc = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
User_Agent_Instagram = 'Mozilla/5.0 (Linux; Android 9; SM-A102U Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/74.0.3729.136 Mobile Safari/537.36 Instagram 155.0.0.37.107 Android (28/9; 320dpi; 720x1468; samsung; SM-A102U; a10e; exynos7885; en_US; 239490550)'
abc = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'

#========[INFO (Kumpulan Def)]========#
ua = ['Mozilla/5.0 (X11; CrOS x86_64 13310.76.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.108 Safari/537.36','Mozilla/5.0 (X11; CrOS x86_64 11895.118.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.159 Safari/537.36','Mozilla/5.0 (X11; CrOS x86_64 12239.92.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.136 Safari/537.36','Mozilla/5.0 (X11; CrOS x86_64 13099.110.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.136 Safari/537.36','Mozilla/5.0 (X11; CrOS x86_64 13099.102.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.127 Safari/537.36','Mozilla/5.0 (X11; CrOS x86_64 13020.87.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.119 Safari/537.36','Mozilla/5.0 (X11; CrOS x86_64 12871.102.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.141 Safari/537.36','Mozilla/5.0 (X11; CrOS x86_64 12499.66.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.106 Safari/537.36','Mozilla/5.0 (X11; CrOS x86_64 13310.59.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.84 Safari/537.36','Mozilla/5.0 (X11; CrOS x86_64 12739.111.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Safari/537.36','Mozilla/5.0 (X11; CrOS x86_64 12607.82.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.123 Safari/537.36','Mozilla/5.0 (X11; CrOS x86_64 13099.85.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.110 Safari/537.36','Mozilla/5.0 (X11; CrOS x86_64 12607.58.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.86 Safari/537.36']
usr_agent = {
	'User-Agent': random.choice(ua)
	}
def p(text):return text.rstrip('\n').lstrip('\n')
def get_size(url):return convert_size(int(urlopen(url).headers['content-length']))
def now_date():l_bln = ['Jan','Feb','Mar','Apr','Mei','Jun','Jul','Agt','Sep','Okt','Nov','Dec'];waktu = datetime.now(utc).astimezone(timezone('Asia/Jakarta'));tgl = waktu.day;bln = l_bln[waktu.month-1];thn = waktu.year;return '%s - %s - %s' % (tgl, bln, thn)
def convert_size(size_bytes):
    if size_bytes == 0:return '0B'
    size_name = ('B', 'KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB')
    i = int(math.floor(math.log(size_bytes, 1024)))
    p = math.pow(1024, i)
    s = round(size_bytes / p, 2)
    return '%s %s' % (s, size_name[i])
def bsoup(link,hdr=True):
    CustomHeader = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0"}
    if hdr == False:return BeautifulSoup(requests.get(link).content, "html.parser")
    else:return BeautifulSoup(requests.get(link,headers=CustomHeader).content, "html.parser")
def shorturl(link):return get("https://tinyurl.com/api-create.php?url="+link).text
#========[INFO (Router List)]========#

def convert_size(size_bytes):
	if size_bytes == 0:
		return '0B'
	size_name = ('B', 'KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB')
	i = int(math.floor(math.log(size_bytes, 1024)))
	p = math.pow(1024, i)
	s = round(size_bytes / p, 2)
	return '%s %s' % (s, size_name[i])

#def allowed_file(filename):
#    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSION

@app.route('/api/textpro', methods=['GET','POST'])
def textpro():
    if request.args.get('theme'):
        theme = request.args.get('theme')
        if theme.lower() in tp.theme:
            if theme.lower() == 'glitch':
                text = request.args.get('text1')
                text2 = request.args.get('text2')
                result = tp.glitchz(text, text2)
                return result
            elif theme.lower() == 'blood':
                text = request.args.get('text')
                result = tp.blood(text)
                return result
            elif theme.lower() == 'dropwater':
                text = request.args.get('text')
                result = tp.dropwater(text)
                return result
            elif theme.lower() == 'jokerlogo':
                text = request.args.get('text')
                result = tp.jokerlogo(text)
                return result
            elif theme.lower() == 'neon_light':
                text = request.args.get('text')
                result = tp.neon_light(text)
                return result
            elif theme.lower() == 'lionlogo':
                text = request.args.get('text1')
                text2 = request.args.get('text2')
                result = tp.lionlogo(text, text2)
                return result
            elif theme.lower() == 'wolflogo1':
                text = request.args.get('text1')
                text2 = request.args.get('text2')
                result = tp.wolflogo1(text, text2)
                return result
            elif theme.lower() == 'wolflogo2':
                text = request.args.get('text1')
                text2 = request.args.get('text2')
                result = tp.wolflogo2(text, text2)
                return result
            elif theme.lower() == 'ninjalogo':
                text = request.args.get('text1')
                text2 = request.args.get('text2')
                result = tp.ninjalogo(text, text2)
                return result
            else:return {'error': 'Theme tersebut tidak ditemukan'}
        else:return {'error': 'Theme tersebut tidak ditemukan'}
    else:return {'message': 'Anda belum memasukan parameter theme'}


@app.route('/tts/<path:filename>', methods=['GET','POST'])
def sendTts(filename):
	return send_from_directory(app.config['MEDIA'], filename, as_attachment=True)

@app.route('/api/layer', methods=['GET','POST'])
def layer():
	if request.args.get('base64image'):
		try:
			open('piw.jpg','w').write(request.args.get('base64image'))
			os.system('base64 -i -d piw.jpg > paw.jpg')
			hehe = resizeTo('paw.jpg')
			huhu = layer(hehe, 'black')
			os.system('base64 result.jpg > pow.jpg')
			return {
				'status': 200,
				'result': '`data:image/jpg;base64,%s`' % open('pow.jpg').read()
			}
		except Exception as e:
			print(e)
			#os.remove('piw.jpg')
			return {
				'status': False,
				'error': '[!] Invalid base64 image!'
			}
	else:
		return {
			'status': False,
			'msg': '[!] Masukkan parameter base64image'
		}

@app.route('/api/spamgmail', methods=['GET','POST'])
def spamgimel():
    if request.args.get('target'):
        if request.args.get('jum'):
            abece = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
            target_imel = request.args.get('target')
            jumlah = int(request.args.get('jum'))
            if jumlah > 10:
                return {
                    'status': False,
                    'msg': '[!] Max 10 tod!'
                }
            try:
                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.ehlo()
                server.starttls()
                server.login('spamz.barbar@gmail.com', 'Barbar05')
                hasil = ''
                for i in range(jumlah):
                    mess = ''.join(random.choice(abece) for _ in range(4))
                    msg = f'From: {random.randint(1, 100)}<Hacker>\nSubject: Anonymous ~ Hacker\n{mess}'
                    server.sendmail('spamz.barbar@gmail.com', target_imel, msg)
                    hasil += '[!] Sukses\n'
                server.quit()
                return {
                    'status': 200,
                    'logs': hasil
                }
            except Exception as e:
                print(e)
                hasil = '[!] Gagal'
                return {
                    'status': False,
                    'logs': hasil
                }
        else:
            return {
                'status': False,
                'msg': 'Masukkan parameter jum'
            }
    else:
        return {
            'status': False,
            'msg': 'Masukkan parameter target'
        }

@app.route('/api/spamcall', methods=['GET','POST'])
def spamcall():
    if request.args.get('no'):
        no = request.args.get('no')
        if str(no).startswith('8'):
            hasil = ''
            kyaa = post('https://id.jagreward.com/member/verify-mobile/%s' % no).json()
            print(kyaa['message'])
            if 'Anda akan menerima' in kyaa['message']:
                hasil += '[!] Berhasil mengirim spam call ke nomor : 62%s' % no
            else:
                hasil += '[!] Gagal mengirim spam call ke nomor : 62%s' % no
            return {
                'status': 200,
                'logs': hasil
            }
        else:
            return {
                'status': False,
                'msg': '[!] Tolong masukkan nomor dengan awalan 8'
            }
    else:
        return {
            'status': False,
            'msg': '[!] Masukkan parameter no' 
        }
@app.route('/api/spamsms', methods=['GET','POST'])
def spamming():
    if request.args.get('no'):
        if request.args.get('jum'):
            no = request.args.get('no')
            jum = int(request.args.get('jum'))
            if jum > 20: return {
                'status': 200,
                'msg': '[!] Max 20 ganteng'
            }
            url = 'https://www.lpoint.co.id/app/member/ESYMBRJOTPSEND.do'
            head = {'UserAgent': 'Mozilla/5.0 (Linux; Android 8.1.0; CPH1853) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36'}
            data = {'pn': '',
                'bird': '',
                'webMbrId': '',
                'webPwd': '',
                'maFemDvC': '',
                'cellNo': no,
                'otpNo': '',
                'seq': '',
                'otpChk': 'N',
                'count': ''
            }
            hasil = ''
            for i in range(jum):
                kyaa = post(url, headers=head, data=data).text
                if 'error' in kyaa:
                    hasil += '[!] Gagal\n'
                else:
                    hasil += '[!] Sukses\n'
            return {
                'status': 200,
                'logs': hasil
            }
        else:
            return {
                'status': False,
                'msg': '[!] Masukkin parameter jum juga ganteng'
            }
    else:
        return {
            'status': False,
            'msg': '[!] Masukkan parameter no'
        }
@app.route('/api/nulis', methods=['POST','GET'])
def nulis_maker():
    if request.args.get('text'):
        text = request.args.get('text')
        try:
            hihi = f'result/{str(random.random())[10:]}.jpg'
            nulis(text)
            return {
                'creator': 'Tobz',
                'status': 200,
                "result": 'https://tobz-api.herokuapp.com/%s' % hihi
                }
        except Exception as e:
        	print (e);
        return {
	        'creator':'Tobz',
	        'status': False,
	        'error': '[!] Upss, terjadi kesalahan'
        }
    else:
    	return {
	    	'creator': 'Tobz',
	    	'status': False,
	    	'message': '[!] Masukkan parameter text'
    	}

@app.route('/api/wiki', methods=['GET','POST'])
def wikipedia():
	if request.args.get('q'):
		try:
			kya = request.args.get('q')
			cih = f'https://id.wikipedia.org/w/api.php?format=json&action=query&prop=extracts&exintro&explaintext&redirects=1&titles={kya}'
			heuh = get(cih).json()
			heuh_ = heuh['query']['pages']
			hueh = re.findall(r'(\d+)', str(heuh_))
			result = heuh_[hueh[0]]['extract']
			return {
				'status': 200,
				'result': result
			}
		except Exception as e:
			print(e)
			return {
				'status': False,
				'error': '[❗] Yang anda cari tidak bisa saya temukan di wikipedia!'
			}
	else:
		return {
			'status': False,
			'msg': '[!] Masukkan param q'
		}

@app.route('/api/tts', methods=['GET','POST'])
def tts():
	if request.args.get('text'):
		try:
			teks = request.args.get('text')
			print(teks)
			if int(len(teks)) - int(len(teks.split(' '))) == 250:
				return {
					'status': 200,
					'msg': '[❗] Maaf teks terlalu panjang!!',
				}
			else:
				url = f'https://rest.farzain.com/api/tts.php?id={teks}&apikey='
				if os.path.isfile('./tts/tts.mp3') == True:
					os.remove('./tts/tts.mp3')
					Tts = get(f'{url}{apiKey}').content
					open('tts/tts.mp3','wb').write(Tts)
					return {
						'status': 200,
						'msg': 'Success convert text to speech!',
						'file': 'https://tobz-api.herokuapp.com/tts/tts.mp3'
					}
				else:
					Tts = get(f'{url}{apiKey}').content
					open('tts/tts.mp3','wb').write(Tts)
					return {
						'status': 200,
						'msg': 'Success convert text to speech!',
						'file': 'https://tobz-api.herokuapp.com/tts/tts.mp3'
					}
		except Exception as e:
			print(e)
			return {
				'status': False,
				'msg': '[!] Upss, terjadi kesalahan'
			}
	else:
		return {
			'status': 200,
			'msg': '[!] Masukkan parameter text'
		}

@app.route('/api/ytv', methods=['GET','POST'])
def ytv():
	if request.args.get('url'):
		try:
			url = request.args.get('url').replace('[','').replace(']','')
			ytv = post('https://www.y2mate.com/mates/en60/analyze/ajax',data={'url':url,'q_auto':'0','ajax':'1'}).json()
			yaha = bs(ytv['result'], 'html.parser').findAll('td')
			filesize = yaha[len(yaha)-23].text
			id = re.findall('var k__id = "(.*?)"', ytv['result'])
			thumb = bs(ytv['result'], 'html.parser').find('img')['src']
			title = bs(ytv['result'], 'html.parser').find('b').text
			dl_link = bs(post('https://www.y2mate.com/mates/en60/convert',data={'type':url.split('/')[2],'_id':id[0],'v_id':url.split('/')[3],'ajax':'1','token':'','ftype':'mp4','fquality':'360p'}).json()['result'],'html.parser').find('a')['href']
			return {
				'status': 200,
				'title': title,
				'thumb': thumb,
				'result': dl_link,
				'resolution': '360p',
				'filesize': filesize,
				'ext': 'mp4'
			}
		except Exception as e:
			print('Error : %s ' % e)
			return {
				'status': False,
				'error': '[❗] Terjadi kesalahan, mungkin link yang anda kirim tidak valid!'
			}
	else:
		return {
			'status': False,
			'msg': 'Masukkan parameter url'
		}

@app.route('/api/yta', methods=['GET','POST'])
def yta():
	if request.args.get('url'):
		try:
			url = request.args.get('url').replace('[','').replace(']','')
			yta = post('https://www.y2mate.com/mates/en60/analyze/ajax',data={'url':url,'q_auto':'0','ajax':'1'}).json()
			yaha = bs(yta['result'], 'html.parser').findAll('td')
			filesize = yaha[len(yaha)-10].text
			id = re.findall('var k__id = "(.*?)"', yta['result'])
			thumb = bs(yta['result'], 'html.parser').find('img')['src']
			title = bs(yta['result'], 'html.parser').find('b').text
			dl_link = bs(post('https://www.y2mate.com/mates/en60/convert',data={'type':url.split('/')[2],'_id':id[0],'v_id':url.split('/')[3],'ajax':'1','token':'','ftype':'mp3','fquality':'128'}).json()['result'],'html.parser').find('a')['href']
			return {
				'status': 200,
				'title': title,
				'thumb': thumb,
				'filesize': filesize,
				'result': dl_link,
				'ext': 'mp3'
			}
		except Exception as e:
			print('Error : %s' % e)
			return {
				'status': False,
				'error': '[❗] Terjadi kesalahan mungkin link yang anda kirim tidak valid!'
			}
	else:
		return {
			'status': False,
			'msg': '[!] Masukkan parameter url'
		}

@app.route('/api/chord', methods=['GET','POST'])
def chord():
	if request.args.get('q'):
		try:
			q = request.args.get('q').replace(' ','+')
			id = get('http://app.chordindonesia.com/?json=get_search_results&exclude=date,modified,attachments,comment_count,comment_status,thumbnail,thumbnail_images,author,excerpt,content,categories,tags,comments,custom_fields&search=%s' % q).json()['posts'][0]['id']
			chord = get('http://app.chordindonesia.com/?json=get_post&id=%s' % id).json()
			result = html_text.parse_html(chord['post']['content']).text_content()
			return {
				'status': 200,
				'result': result
			}
		except Exception as e:
			print(e)
			return {
				'status': False,
				'error': '[❗] Maaf chord yang anda cari tidak dapat saya temukan!'
			}
	else:
		return {
			'status': False,
			'msg': '[!] Masukkan parameter q'
		}

@app.route('/api/dewabatch', methods=['GET','POST'])
def dewabatch():
	if request.args.get('q'):
		try:
			q = request.args.get('q')
			he=search_dewabatch(quote(q))
			dewabatch=cari(he)
			if he != '':
				return {
					'status': 200,
					'sinopsis': dewabatch['result'],
					'thumb': dewabatch['cover'],
					'result': dewabatch['info']
				}
		except Exception as e:
			print(e)
			return {
				'status': False,
				'error': 'Anime %s Tidak di temukan!' % unquote(q)
			}
	else:
		return {
			'status': False,
			'msg': '[!] Masukkan parameter q'
		}

@app.route('/api/komiku', methods=['GET','POST'])
def komiku():
    if request.args.get('q'):
        try:
            q = request.args.get('q')
            komi = search_komiku(q)
            if 'Tidak di temukan' not in komi:
                manga = scrap_komiku(komi)
                return {
                    'status': 200,
                    'info': manga['info'],
                    'genre': manga['genre'],
                    'sinopsis': manga['sinopsis'],
                    'thumb': manga['thumb'],
                    'link_dl': manga['dl_link']
                }
        except Exception as e:
            print(e)
            return {
                'status': False,
                'error': 'Manga %s Tidak di temukan' % unquote(q)
            }
    else:
        return {
            'status': False,
            'msg': '[!] Masukkan parameter q'
        }

@app.route('/api/kuso', methods=['GET','POST'])
def kusonime():
	if request.args.get('q'):
		try:
			q = request.args.get('q')
			he=search_kusonime(quote(q))
			kuso=scrap_kusonime(he)
			if he != '':
				return {
					'status': 200,
					'sinopsis': kuso['sinopsis'],
					'thumb': kuso['thumb'],
					'info': kuso['info'],
					'title': kuso['title'],
					'link_dl': kuso['link_dl']
				}
		except Exception as e:
			print(e)
			return {
				'status': False,
				'error': 'Anime %s Tidak di temukan' % unquote(q)
			}
	else:
		return {
			'status': False,
			'msg': '[!] Masukkan parameter q'
		}
            
@app.route('/api/brainly', methods=['GET','POST'])
def brainly_scraper():
	if request.args.get('q'):
		try:
			query = request.args.get('q')
			br=brainly(gsearch('"%s" site:brainly.co.id' % quote(query), lang='id')[0])
			return {
				'status': 200,
				'result': br
			}
		except Exception as e:
			print(e)
			return {
				'status': False,
				'error': '[❗] Pertanyaan %s tidak dapat saya temukan di brainly' % unquote(query)
			}
	else:
		return {
			'status': False,
			'msg': '[!] Masukkan parameter q'
		}

@app.route('/api/nekonime', methods=['GET','POST'])
def nekonimek():
	try:
		neko = get('https://waifu.pics/api/sfw/neko').json()
		nimek = neko['url']
		return {
			'status': 200,
			'result': nimek
		}
	except:
		neko = get('https://waifu.pics/api/sfw/neko').json()
		nimek = neko['url']
		return {
			'status': 200,
			'result': nimek
		}

@app.route('/api/cry', methods=['GET','POST'])
def crynime():
	try:
		cryz = get('https://waifu.pics/api/sfw/cry').json()
		ncry = cryz['url']
		return {
			'status': 200,
			'result': ncry
		}
	except:
		cryz = get('https://waifu.pics/api/sfw/cry').json()
		ncry = cryz['url']
		return {
			'status': 200,
			'result': cryz
		}

@app.route('/api/kiss', methods=['GET','POST'])
def kissnime():
	try:
		rkiss = get('https://waifu.pics/api/sfw/kiss').json()
		nkiss = rkiss['url']
		return {
			'status': 200,
			'result': nkiss
		}
	except:
		rkiss = get('https://waifu.pics/api/sfw/kiss').json()
		nkiss = rkiss['url']
		return {
			'status': 200,
			'result': nkiss
		}

@app.route('/api/hug', methods=['GET','POST'])
def hugnime():
	try:
		hugz = get('https://waifu.pics/api/sfw/hug').json()
		nhug = hugz['url']
		return {
			'status': 200,
			'result': nhug
		}
	except:
		hugz = get('https://waifu.pics/api/sfw/hug').json()
		nhug = hugz['url']
		return {
			'status': 200,
			'result': nhug
		}

@app.route('/api/randomanime', methods=['GET','POST'])
def randomanime():
	try:
		rnime = ['waifu','neko','shinobu','megumin']
		nnimee = get('https://waifu.pics/api/sfw/%s' % random.choice(rnime)).json()
		nimee = nnimee['url']
		return {
			'status': 200,
			'result': nimee
		}
	except:
		rnime = ['waifu','neko','shinobu','megumin']
		nnimee = get('https://waifu.pics/api/sfw/%s' % random.choice(rnime)).json()
		nimee = nnimee['url']
		return {
			'status': 200,
			'result': nimee
		}

@app.route('/api/randomloli', methods=['GET','POST'])
def randomloli():
	try:
		hehe = ['kawaii','neko']
		loli = get('https://api.lolis.life/%s' % random.choice(hehe)).json()['url']
		return {
			'status': 200,
			'result': loli
		}
	except:
		return {
			'status': 200,
			'result': loli
		}

@app.route('/api/memes', methods=['GET','POST'])
def rmemes():
	try:
		hehe = ['kawaii','neko']
		loli = get('https://api.lolis.life/%s' % random.choice(hehe)).json()['url']
		return {
			'status': 200,
			'result': loli
		}
	except:
		return {
			'status': 200,
			'result': loli
		}

@app.route('/api/nsfwblowjob', methods=['GET','POST'])
def blowjob():
	try:
		nblow = get('https://waifu.pics/api/nsfw/blowjob').json()
		bblow = nblow['url']
		return {
			'status': 200,
			'result': bblow
		}
	except:
		nblow = get('https://waifu.pics/api/nsfw/blowjob').json()
		bblow = nblow['url']
		return {
			'status': 200,
			'result': bblow
		}

@app.route('/api/hentai', methods=['GET','POST'])
def hentaii():
	try:
		nblow = get('https://waifu.pics/api/nsfw/waifu').json()
		bblow = nblow['url']
		return {
			'status': 200,
			'result': bblow
		}
	except:
		nblow = get('https://waifu.pics/api/nsfw/waifu').json()
		bblow = nblow['url']
		return {
			'status': 200,
			'result': bblow
		}

@app.route('/api/nsfwneko', methods=['GET','POST'])
def nsfwneko():
	try:
		nneko = get('https://waifu.pics/api/nsfw/neko').json()
		nekko = nneko['url']
		return {
			'status': 200,
			'result': nekko
		}
	except:
		nneko = get('https://waifu.pics/api/nsfw/neko').json()
		nekko = nneko['url']
		return {
			'status': 200,
			'result': nekko
		}

@app.route('/api/nsfwtrap', methods=['GET','POST'])
def trapnime():
	try:
		trap = get('https://waifu.pics/api/nsfw/trap').json()
		ntrap = trap['url']
		return {
			'status': 200,
			'result': ntrap
		}
	except:
		trap = get('https://waifu.pics/api/nsfw/trap').json()
		ntrap = trap['url']
		return {
			'status': 200,
			'result': ntrap
		}

@app.route('/api/ig', methods=['GET','POST'])
def igeh():
	if request.args.get('url'):
		try:
			url = request.args.get('url')
			data = {'id': url}
			result = get('https://www.villahollanda.com/api.php?url=' + url).json()
			if result['descriptionc'] == None:
				return {
					'status': False,
					'result': 'https://c4.wallpaperflare.com/wallpaper/976/117/318/anime-girls-404-not-found-glowing-eyes-girls-frontline-wallpaper-preview.jpg',
				}
			else:
				return {
					'status': 200,
					'result': result['descriptionc'],
				}
		except Exception as e:
			print(e)
			return {
				'status': False,
				'result': 'https://c4.wallpaperflare.com/wallpaper/976/117/318/anime-girls-404-not-found-glowing-eyes-girls-frontline-wallpaper-preview.jpg',
				'error': True
			}
	else:
		return {
			'status': False,
			'msg': '[!] Masukkan parameter url'
		}

@app.route('/api/ttp', methods=['GET','POST'])
def ttpz():
	if request.args.get('text'):
		try:
			query = request.args.get('text')
			link = f'https://api.areltiyan.site/sticker_maker?text={query}'
			ttp = get(link).json()
			print(ttp)
			return {
				'status': 200,
				'base64': ttp['base64'],
				'creator': 'Tobz'
			}
		except:
			return {
				'status': False,
				'error': '[❗] Maaf, Text yang anda masukan salah!'
			}
	else:
		return {
			'status': False,
			'msg': '[!] Masukkan parameter text'
		}

@app.route('/api/facebook', methods=['GET','POST'])
def zfb():
	if request.args.get('url'):
		try:
			query = request.args.get('url')
			link = f'https://mnazria.herokuapp.com/api/fbdownloadervideo?url={query}'
			fb = get(link).json()
			print(fb)
			return {
				'status': 200,
				'creator': 'Tobz',
				'result':{
					'kualitasHD': fb['resultHD'],
					'kualitasSD': fb['resultSD']
				}
			}
		except:
			return {
				'status': False,
				'error': '[❗] Maaf, Url yang anda masukan salah!'
			}
	else:
		return {
			'status': False,
			'msg': '[!] Masukkan parameter url'
		}

@app.route('/api/artinama', methods=['GET','POST'])
def artin():
	if request.args.get('nama'):
		try:
			query = request.args.get('nama')
			link = f'https://mnazria.herokuapp.com/api/arti?nama={query}'
			art = get(link).json()
			print(art)
			return {
				'status': 200,
				'result': art['result'],
				'creator': 'Tobz'
			}
		except:
			return {
				'status': False,
				'error': '[❗] Maaf, Text yang anda masukan salah!'
			}
	else:
		return {
			'status': False,
			'msg': '[!] Masukkan parameter text'
		}

@app.route('/api/kbbi', methods=['GET','POST'])
def kbbz():
	if request.args.get('kata'):
		try:
			query = request.args.get('kata')
			auth = AutentikasiKBBI(path='./coki.txt')
			data = str(KBBI(query, auth))
			return {
				'creator': 'Tobz',
				'status': 200,
				'result': data
			}
		except:
			return {
				'status': False,
				'error': '[❗] Maaf, Kata yang anda masukan salah!'
			}
	else:
		return {
			'status': False,
			'msg': '[!] Masukkan parameter kata'
		}

@app.route('/api/jadwalshalat', methods=['GET','POST'])
def jshalat():
	if request.args.get('q'):
		try:
			query = request.args.get('q')
			url = f'https://api.pray.zone/v2/times/today.json?city={query}'
			hslt = get(url).json()
			print(hslt)
			return {
				'status': 200,
				'creator': 'Tobz',
				'result':{
					'imsak': hslt['results']['datetime'][0]['times']['Imsak'],
					'sunrise': hslt['results']['datetime'][0]['times']['Sunrise'],
					'subuh': hslt['results']['datetime'][0]['times']['Fajr'],
					'dzuhur': hslt['results']['datetime'][0]['times']['Dhuhr'],
					'ashar': hslt['results']['datetime'][0]['times']['Asr'],
					'maghrib': hslt['results']['datetime'][0]['times']['Maghrib'],
					'sunset': hslt['results']['datetime'][0]['times']['Sunset'],
					'isha': hslt['results']['datetime'][0]['times']['Isha'],
					'midnight': hslt['results']['datetime'][0]['times']['Midnight']
				}
			}
		except:
			return {
				'status': False,
				'error': '[❗] Maaf, Daerah yang anda masukan salah!'
			}
	else:
		return {
			'status': False,
			'msg': '[!] Masukkan parameter daerah'
		}

@app.route('/api/joox', methods=['GET','POST'])
def zjoox():
	if request.args.get('q'):
		try:
			query = request.args.get('q')
			url = f'https://mnazria.herokuapp.com/api/jooxnich?search={query}'
			rsp = get(url).json()
			print(rsp)
			return {
				'status': 200,
				'creator': 'Tobz',
				'result':{
					'album': rsp['result']['msong'],
					'judul': rsp['result']['msinger'],
					'mp3': rsp['result']['r320Url'],
					'dipublikasi': rsp['result']['public_time'],
					'thumb': rsp['result']['album_url']
				}
			}
		except:
			return {
				'status': False,
				'error': '[❗] Maaf, Query yang anda masukan salah!'
			}
	else:
		return {
			'status': False,
			'msg': '[!] Masukkan parameter q'
		}

@app.route('/api/lirik', methods=['GET','POST'])
def zlirik():
	if request.args.get('q'):
		try:
			query = request.args.get('q')
			url = f'https://mnazria.herokuapp.com/api/jooxnich?search={query}'
			lrk = get(url).json()
			print(lrk)
			return {
				'status': 200,
				'creator': 'Tobz',
				'result':{
					'album': lrk['result']['msong'],
					'judul': lrk['result']['msinger'],
					'dipublikasi': lrk['result']['public_time'],
					'thumb': lrk['result']['album_url'],
					'lirik': lrk['lirik']
				}
			}
		except:
			return {
				'status': False,
				'error': '[❗] Maaf, Query yang anda masukan salah!'
			}
	else:
		return {
			'status': False,
			'msg': '[!] Masukkan parameter q'
		}

@app.route('/api/simsimi', methods=['GET','POST'])
def simi():
	if request.args.get('text'):
		try:
			query = request.args.get('text')
			url = f'http://simsumi.herokuapp.com/api?text={query}&lang=id'
			sim = get(url).json()
			print(sim)
			return {
				'status': 200,
				'result': sim['success'],
				'creator': 'Tobz'
			}
		except:
			return {
				'status': False,
				'error': '[❗] Maaf, Text yang anda masukan salah!'
			}
	else:
		return {
			'status': False,
			'msg': '[!] Masukkan parameter text'
		}

@app.route('/api/cuaca', methods=['GET','POST'])
def zcuaca():
	if request.args.get('wilayah'):
		try:
			query = request.args.get('wilayah')
			url = url = f'https://rest.farzain.com/api/cuaca.php?id={query}&apikey=fckveza'
			data = get(url, headers={'User-Agent': 'Mozilla/5.0 (Linux; Android 8.1.0; CPH1909) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.81 Mobile Safari/537.36'}).json()
			if data['respon']['deskripsi'] == 'null' or data['respon']['deskripsi'] == None:
				return {
					'creator':'Tobz',
					'status': 404,
					'error': 'Gagal mengambil informasi cuaca, mungkin tempat tidak terdaftar/salah!'
				}
			else:
				return {
					'creator':'Tobz',
					'status': 200,
					'result': {
						'tempat': data['respon']['tempat'],
						'cuaca': data['respon']['cuaca'],
						'desk': data['respon']['deskripsi'],
						'suhu': data['respon']['suhu'],
						'kelembapan': data['respon']['kelembapan'],
						'udara': data['respon']['udara'],
						'angin': data['respon']['angin']
					}
				}
		except Exception as e:
			print(e);
			return {
				'status': False,
				'message': 'Gagal mengambil informasi cuaca, mungkin tempat tidak terdaftar/salah!'
			}
	else:
		return {
			'status': False,
			'msg': '[!] Masukkan parameter text'
		}

@app.route('/api/bitly', methods=['GET','POST'])
def short2():
    if request.args.get('url'):
        try:
            query = request.args.get('url')
            url = get("https://api-ssl.bitly.com/v3/shorten?access_token=eeed32b267a6f473e0e824aa685527cf1e18a5e6&longUrl={}".format(query)).json()
            data = url['data']['url']
            print(data)
            return {
            	'status': 200,
	            'creator':'Tobz',
	            'result': data
            }
        except Exception as e:
            print(e)
            return {
                'status': False,
                'error': 'Url %s Tidak di temukan!' % unquote(query)
            }
    else:
        return {
            'status': False,
            'msg': 'input parameter url'
        }

@app.route('/api/tinyurl', methods=['GET','POST'])
def short():
    if request.args.get('url'):
        try:
            query = request.args.get('url')
            url = requests.get("https://tinyurl.com/api-create.php?url={}".format(query))
            data = url.text
            print(data)
            return {
            	'status': 200,
	            'creator':'Tobz',
	            'result': data
            }
        except Exception as e:
            print(e)
            return {
                'status': False,
                'error': 'Url %s Tidak di temukan!' % unquote(query)
            }
    else:
        return {
            'status': False,
            'msg': 'input parameter url'
        }

@app.route('/api/film', methods=['GET','POST'])
def zfilm():
    if request.args.get('q'):
        try:
            query = request.args.get('q')
            hasilnya = []
            result = {"creator":"Tobz","result": hasilnya}
            url = bsoup("http://149.56.24.226/?s={}#gsc.tab=0&gsc.q=frozen&gsc.page=1".format(query))
            for tobz in url.findAll('div', class_='search-item'):
                title = tobz.a['title']
                img = tobz.img['src']
                image = shorturl(img)
                link = tobz.a['href']
                info = tobz.findAll('p')
                sutradara = info[1].text.replace('Sutradara: ','')
                bintang = info[2].text.replace('Bintang: ','')
                data = bsoup(link)
                info2 = data.find('div', class_='col-xs-10 content')
                txt = info2.findAll('div')
                kualitas = txt[0].text.replace('Kualitas','')
                negara = txt[1].text.replace('Negara','')
                genre = txt[4].text.replace('Genre','')
                imdb = txt[5].findAll('h3')
                imdb0 = imdb[0].text+'/'
                imdb1 = imdb[1].text+' from '
                imdb2 = imdb[2].text+' users'
                terbit = txt[6].text.replace('Diterbitkan','')
                penerjemah = txt[7].text.replace('Penerjemah','').replace('Oleh','')
                dl = data.find('div', class_='download-movie')
                download = dl.a['href']
                hasil = hasilnya.append({"judul":title,"image":image,"link":link,"sutradara":sutradara,"bintang_film":bintang,"kualitas":kualitas,"negara":negara,"genre":genre,"imdb":imdb0+imdb1+imdb2,"diterbitkan":terbit,"penerjemah":penerjemah,"download":download})
            return {
				'status': 200,
				'creator':'Tobz',
				'result': hasilnya
			}
        except Exception as e:
            print(e)
            return {
                'status': False,
                'error': 'Film %s Tidak di temukan!' % unquote(query)
            }
    else:
        return {
            'status': False,
            'msg': 'input parameter q'
        }

@app.route('/api/bacakomik', methods=['GET','POST'])
def zkomik():
    if request.args.get('q'):
        try:
            query = request.args.get('q')
            hasilnya = []
            result = {"creator":"Tobz","result": hasilnya}
            url = bsoup("https://bacakomik.co/?s={}".format(query))
            tobz = url.find('div', class_='animepost')
            link = tobz.a['href']
            soup = bsoup(link)
            info = soup.find("div",class_="infox")
            txt = info.findAll('span')
            status = txt[0].text.replace('Status: ','')
            format = txt[1].text.replace('Format: ','')
            rilis = txt[2].text.replace('Dirilis: ','')
            pengarang = txt[3].text.replace('Pengarang: ','')
            jenis = txt[4].text.replace('Jenis Komik: ','')
            umur = txt[5].text.replace('Umur Pembaca: ','')
            cara = txt[6].text.replace('Cara Baca ','')
            konsep = txt[7].text.replace('Konsep Cerita: ','')
            update = txt[8].text.replace('Update Terakhir: ','')
            diihat = txt[9].text.replace('Dilihat: ','')
            genres = soup.find('div', class_='genre-info').text.replace('\n',', ')
            rat = tobz.find('div', class_='rating')
            rate = rat.findAll('i')
            rating = rate[0].text
            for imgz in url.findAll('div', class_='animepost'):
                title = imgz.img['title']
                img = imgz.img['src']
                image = shorturl(img)
                hasil = hasilnya.append({"judul":title,"thumbnail":image,"rating":rating,"link":link,"status":status,"format":format,"dirilis":rilis,"pengarang":pengarang,"jenis_komik":jenis,"umur_pembaca":umur,"cara_baca":cara,"konsep_cerita":konsep,"update_terakhir":update,"genre":genres})
            return {
				'status': 200,
				'creator':'Tobz',
				'result': hasilnya
			}
        except Exception as e:
            print(e)
            return {
                'status': False,
                'error': 'Komik %s Tidak di temukan!' % unquote(query)
            }
    else:
        return {
            'status': False,
            'msg': 'input parameter q'
        }

# ERROR
@app.route('/api/otakudesu', methods=['GET','POST'])
def zotaku():
    if request.args.get('q'):
        try:
            query = request.args.get('q')
            url = bs(get('https://otakudesu.tv/?s=%s&post_type=anime' % query, headers=usr_agent).text, 'html.parser')
            for rafly in url.findAll('div', class_='venser'):
                image = rafly.img['src']
                imagez = shorturl(image)
                link = rafly.a['href']
                data = bs(get(link).text, 'html.parser')
                info = data.find('div', class_='infozingle')
                rafli = info.findAll('p')
                info2 = data.find('div', class_='sinopc')
                rafli2 = info2.findAll('p')
            return {
				'status': 200,
				'creator':'Tobz',
				'result': {
					"judul":rafli[0].text.replace("Judul: ",""),
					"judul_jepang":rafli[1].text.replace("Japanese: ",""),
					"rating":rafli[2].text.replace("Skor: ",""),
					"produser":rafli[3].text.replace("Produser: ",""),
					"tipe":rafli[4].text.replace("Tipe: ",""),
					"status":rafli[5].text.replace("Status: ",""),
					"total_episode":rafli[6].text.replace("Total Episode: ",""),
					"durasi":rafli[7].text.replace("Durasi: ",""),
					"tanggal_rilis":rafli[8].text.replace("Tanggal Rilis: ",""),
					"studio":rafli[9].text.replace("Studio: ",""),
					"genre":rafli[10].text.replace("Genre: ",""),
					"sinopsis":rafli2[0].text,
					"thumbnail":imagez,
					"link":link
				}
			}
        except Exception as e:
            print(e)
            return {
                'status': False,
                'error': 'Anime %s Tidak di temukan!' % unquote(query)
            }
    else:
        return {
            'status': False,
            'msg': 'input parameter q'
        }

@app.route('/api/neolast', methods=['GET','POST'])
def zneolast():
    data = []
    url = requests.get("https://neonime.vip")
    tbz = BeautifulSoup(url.content,'html.parser')
    desc = tbz.find('span', {'class': 'ttx'}).text
    for Tobz in tbz.find_all('div',class_='item episode-home'):
        link = "{}".format(str(Tobz.find('a')['href']))
        title = "{}".format(str(Tobz.find('img')['alt']))
        image = "{}".format(str(Tobz.find('img')['data-src'])).replace(' ',"")
        hasil = data.append({"title":title,"desc": desc,"image":image,"link":link})
    return {
        'status': 200,
        'creator': 'Tobz',
        'result': data
    }

@app.route('/api/neonime', methods=['GET','POST'])
def zneonime():
    if request.args.get('q'):
        try:
            query = request.args.get('q')
            hasilnya = []
            url = bsoup("https://neonime.vip/?s={}".format(query))
            desc = url.find('span', {'class': 'ttx'}).text
            for Tobz in url.find_all('div',class_='item episode-home'):
                link = "{}".format(str(Tobz.find('a')['href']))
                title = "{}".format(str(Tobz.find('img')['alt']))
                image = "{}".format(str(Tobz.find('img')['data-src'])).replace(' ',"")
                data = bsoup(link)
                info = data.find('div', class_='ladoA')
                upload = info.find('div', class_='meta-a').text
                data2 = info.find('div', class_='meta-b')
                info2 = data2.findAll('span', class_='metx')
                season = info2[0].text.replace(' Season ','')
                episode = info2[1].text.replace(' Episode ','')
                hasil = hasilnya.append({"title":title,"desc": desc,"image":image,"link":link,'diupload':upload,'season':season,'episode':episode})
            return {
				'status': 200,
				'creator':'Tobz',
				'result':hasilnya
			}
        except Exception as e:
            print(e)
            return {
                'status': False,
                'error': 'Anime %s Tidak di temukan!' % unquote(query)
            }
    else:
        return {
            'status': False,
            'msg': 'input parameter q'
        }

@app.route('/api/anolast', methods=['GET','POST'])
def zanolast():
    data = []
    url = requests.get("https://anoboy.tube/")
    rtb = BeautifulSoup(url.content,'html.parser')
    for rafly in rtb.findAll('div', class_='amv'):
        title = "{}".format(str(rafly.find('h3', {'class':'ibox1'}).text))
        image = "{}".format(str(rafly.find('amp-img')['src']))
        date = "{}".format(str(rafly.find('div',class_='jamup').text))
        hasil = data.append({"title":title,"image":image,"date":date})
    return {
        'status': 200,
        'creator': 'Tobz',
        'result': data
    }

@app.route('/api/anoboy', methods=['GET','POST'])
def zanoboy():
    if request.args.get('q'):
        try:
            query = request.args.get('q')
            data = []
            result = {"creator":"Tobz","result": data}
            url = requests.get("https://anoboy.tube/?s={}".format(query))
            rtb = BeautifulSoup(url.content,'html.parser')
            for rafz in rtb.findAll('div', class_='column-content'):
	            link = rafz.a.get('href')
            for rafly in rtb.findAll('div', class_='amv'):
                title = "{}".format(str(rafly.find('h3', {'class':'ibox1'}).text))
                image = "{}".format(str(rafly.find('amp-img')['src']))
                date = "{}".format(str(rafly.find('div',class_='jamup').text))
                hasil = data.append({"title":title,"image":image,"link":link,"date":date})
            return {
				'status': 200,
				'creator':'Tobz',
				'result':data
			}
        except Exception as e:
            print(e)
            return {
                'status': False,
                'error': 'Anime %s Tidak di temukan!' % unquote(query)
            }
    else:
        return {
            'status': False,
            'msg': 'input parameter q'
        }

@app.route('/api/screenshotweb', methods=['GET','POST'])
def zssweb():
    if request.args.get('url'):
        try:
            query = request.args.get('url')
            link = get("https://screenshotapi.net/api/v1/screenshot?url={}&output=image".format(str(query)))
            data = ''.join(random.choice(abc) for _ in range(20)) + '.jpg'
            open('result/%s' % data, 'wb').write(link.content)
            return {
                'creator': 'Tobz',
                'status': 200,
                'result': {
                    'result': 'https://tobz-api.herokuapp.com/result/%s' % data
                }
            }
        except Exception as e:
            print(e)
            return {
                'status': False,
                'error': 'Website %s Tidak di temukan!' % unquote(query)
            }
    else:
        return {
            'status': False,
            'msg': 'input parameter q'
        }

@app.route('/api/githubprofile', methods=['GET','POST'])
def gprofile():
	if request.args.get('username'):
		try:
			username = request.args.get('username').replace('@','')
			link = requests.get("https://api.github.com/users/{}".format(username))
			jsonnya = link.text
			gitprof = json.loads(jsonnya)
			print(gitprof)
			return {
				'status': 200,
				'creator': 'Tobz',
				'result': {
					'username': gitprof['login'],
					'name': gitprof['name'],
					'follower': gitprof['followers'],
					'following': gitprof['following'],
					'biography': gitprof['bio'],
					'location': gitprof['location'],
					'avatar': gitprof['avatar_url'],
					'company': gitprof['company'],
					'email': gitprof['email'],
					'public_repository': gitprof['public_repos'],
					'public_gists': gitprof['public_gists'],
					'twitter_username': gitprof['twitter_username'],
					'url': gitprof['url']
				}
			}
		except Exception as e:
			print(e)
			return {
				'status': False,
				'error': '[❗] Username salah!!'
			}
	else:
		return {
			'status': False,
			'msg': '[!] Masukkan parameter username'
		}

@app.route('/api/stalk', methods=['GET','POST'])
def stalk():
	if request.args.get('username'):
		try:
			username = request.args.get('username').replace('@','')
			igestalk = bs(get('https://www.mystalk.net/profile/%s' % username, headers={'User-Agent':'Mozilla/5.0 (Linux; Android 8.1.0; CPH1909) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.101 Mobile Safari/537.36'}).text, 'html.parser').find('div', class_='user-profile-area')
			igestalk_ = igestalk.findAll('span')
			thumb = igestalk.find('img')['src']
			return {
				'status': 200,
				'Name': igestalk_[0].text.strip(),
				'Username': igestalk_[1].text.strip(),
				'Jumlah_Post': igestalk_[2].text.replace('\n',' ').strip(),
				'Jumlah_Followers': igestalk_[3].text.replace('\n',' ').strip(),
				'Jumlah_Following': igestalk_[4].text.replace('\n',' ').strip(),
				'Biodata': igestalk.find('p').text.strip(),
				'Profile_pic': thumb
			}
		except Exception as e:
			print(e)
			return {
				'status': False,
				'error': '[❗] Username salah!!'
			}
	else:
		return {
			'status': False,
			'msg': '[!] Masukkan parameter username'
		}

@app.route('/api/daerah', methods=['GET','POST'])
def daerah():
	daerah = 'Andreas, Ambon, Amlapura, Alford, Argamakmur, Atambua, Babo, Bagan Siapiapi, Central Kalimantan, Birmingham, Samosir, Balikpapan, Banda Aceh, Bandar Lampung, Bandung, Bangkalan, Cianjur, Bangko, Bangli, Banjar, Banjar Baru, Banjarmasin, Corn, BANTAENG , Banten, Bantul, Banyuwangi, Barabai, Barito, Barru, Batam, Batang, Batu, Baturaja, Batusangkar, Baubau, Bekasi, Bengkalis, Bengkulu, Benteng, Biak, Bima, Binjai, Bireuen, Bitung, Blitar, Blora, Bogor, Bojonegoro , Bondowoso, Bontang, Boyolali, Brebes, Bukit Tinggi, Maluku, Bulukumba, Buntok, Cepu, Ciamis, Cianjur, Cibinong, Cilacap, Cilegon, Cimahi, Cirebon, Curup, Demak, Denpasar, Depok, Dili, Dompu, Donggala, Dumai, Ende, Enggano, Enrekang, Fakfak, Garut, Gianyar, Gombong, Gorontalo, Gresik, Gunung Sitoli, Indramayu, Jakarta Barat, Jakarta Pusat, Jakarta Selatan, Jakarta Timur, Jakarta Utara, Jambi,Jayapura, Jember, Jeneponto, Jepara, Jombang, Kabanjahe, Kalabahi, Kalianda, Kandangan, Karanganyar, Karawang, Kasungan, Kayuagung, Kebumen, Kediri, Kefamenanu, Kendal, Kendari, Kertosono, Ketapang, Kisaran, Klaten, Kolaka, Kota Baru Pulau Laut , Bumi Bumi, Kota Jantho, Kotamobagu, Kuala Kapuas, Kuala Kurun, Kuala Pembuang, Kuala Tungkal, Kudus, Kuningan, Kupang, Kutacane, Kutoarjo, Labuhan, Lahat, Lamongan, Langsa, Larantuka, Lawang, Lhoseumawe, Limboto, Lubuk Basung, Lubuk Linggau, Lubuk Pakam, Lubuk Sikaping, Lumajang, Luwuk, Madiun, Magelang, Magetan, Majalengka, Majene, Makale, Makassar, Malang, Mamuju, Manna, Manokwari, Marabahan, Maros, Martapura Kalsel, Sulsel, Masohi, Mataram, Maumere, Medan, Mempawah, Menado, Mentok, Merauke, Metro, Meulaboh, Mojokerto, Muara Bulian, Muara Bungo, Muara Enim, Muara Teweh, Muaro Sijunjung, Muntilan, Nabire,Negara, Nganjuk, Ngawi, Nunukan, Pacitan, Padang, Padang Panjang, Padang Sidempuan, Pagaralam, Painan, Palangkaraya, Palembang, Palopo, Palu, Pamekasan, Pandeglang, Pangka_, Pangkajene Sidenreng, Pangkalan Bun, Pangkalpinang, Panyabungan, Par_, Parepare, Pariaman, Pasuruan, Pati, Payakumbuh, Pekalongan, Pekan Baru, Pemalang, Pematangsiantar, Pendopo, Pinrang, Pleihari, Polewali, Pondok Gede, Ponorogo, Pontianak, Poso, Prabumulih, Praya, Probolinggo, Purbalingga, Purukcahu, Purwakarta, Purwodadigrobogan, Purwarta Purworejo, Putussibau, Raha, Rangkasbitung, Rantau, Rantauprapat, Rantepao, Rembang, Rengat, Ruteng, Sabang, Salatiga, Samarinda, Kalbar, Sampang, Sampit, Sanggau, Sawahlunto, Sekayu, Selong, Semarang, Sengkang, Serang, Serui, Sibolga, Sidikalang, Sidoarjo, Sigli, Singaparna, Singaraja, Singkawang, Sinjai, Sintang, Situbondo, Slawi,Sleman, Soasiu, Soe, Solo, Solok, Soreang, Sorong, Sragen, Stabat, Subang, Sukabumi, Sukoharjo, Sumbawa Besar, Sumedang, Sumenep, Sungai Liat, Sungai Penuh, Sungguminasa, Surabaya, Surakarta, Tabanan, Tahuna, Takalar, Takengon , Tamiang Layang, Tanah Grogot, Tangerang, Tanjung Balai, Tanjung Enim, Tanjung Pandan, Tanjung Pinang, Tanjung Redep, Tanjung Selor, Tapak Tuan, Tarakan, Tarutung, Tasikmalaya, Tebing Tinggi, Tegal, Temanggung, Tembilahan, Tenggarong, Ternate, Tolitoli , Tondano, Trenggalek, Tual, Tuban, Tulung Agung, Ujung Berung, Ungaran, Waikabubak, Waingapu, Wamena, Watampone, Watansoppeng, Wates, Wonogiri, Wonosari, Wonosobo, YogyakartaTakalar, Takengon, Tamiang Layang, Tanah Grogot, Tangerang, Tanjung Balai, Tanjung Enim, Tanjung Pandan, Tanjung Pinang, Tanjung Redep, Tanjung Selor, Tapak Tuan, Tarakan, Tarutung, Tasikmalaya, Tebing Tinggi, Tegal, Temanggung, Tembilahan, Tenggarong, Ternate, Tolitoli, Tondano, Trenggalek, Tual, Tuban, Tulung Agung, Ujung Berung, Ungaran, Waikabubak, Waingapu, Wamena, Watampone, Watansoppeng, Wates, Wonogiri, Wonosari, Wonosobo, YogyakartaTakalar, Takengon, Tamiang Layang, Tanah Grogot, Tangerang, Tanjung Balai, Tanjung Enim, Tanjung Pandan, Tanjung Pinang, Tanjung Redep, Tanjung Selor, Tapak Tuan, Tarakan, Tarutung, Tasikmalaya, Tebing Tinggi, Tegal, Temanggung, Tembilahan, Tenggarong, Ternate, Tolitoli, Tondano, Trenggalek, Tual, Tuban, Tulung Agung, Ujung Berung, Ungaran, Waikabubak, Waingapu, Wamena, Watampone, Watansoppeng, Wates, Wonogiri, Wonosari, Wonosobo, YogyakartaWonogiri, Wonosari, Wonosobo, YogyakartaWonogiri, Wonosari, Wonosobo, Yogyakarta'
	no = 1
	hasil = ''
	for i in daerah.split(','):
		hasil += '%s. %s\n' % (no, i)
		no += 1
	return {
		'status': 200,
		'result': hasil
	}

@app.route('/api/waifu', methods=['GET','POST'])
def waifu():
	scrap = bs(get('https://mywaifulist.moe/random').text, 'html.parser')
	a = json.loads(scrap.find('script', attrs={'type':'application/ld+json'}).string)
	desc = bs(get(a['url']).text, 'html.parser').find('meta', attrs={'property':'og:description'}).attrs['content']
	result = json.loads(bs(get(a['url']).text, 'html.parser').find('script', attrs={'type':'application/ld+json'}).string)
	if result['gender'] == 'female':
		return {
			'status': 200,
			'name': result['name'],
			'desc': desc,
			'image': result['image'],
			'source': result['url']
		}
	else:
		return {
			'status': 200,
			'name': '%s (husbu)' % result['name'],
			'desc': desc,
			'image': result['image'],
			'source': result['url']
		}

@app.route('/api/infogempa', methods=['GET','POST'])
def infogempa():
	be = bs(get('https://www.bmkg.go.id/').text, 'html.parser').find('div', class_="col-md-4 md-margin-bottom-10")
	em = be.findAll('li')
	img = be.find('a')['href']
	return {
		'status': 200,
		'map': img,
		'waktu': em[0].text,
		'magnitude': em[1].text,
		'kedalaman': em[2].text,
		'koordinat': em[3].text,
		'lokasi': em[4].text,
		'potensi': em[5].text
	}

@app.route('/api/randomquotes', methods=['GET','POST'])
def quotes():
	quotes_file = json.loads(open('quotes.json').read())
	result = random.choice(quotes_file)
	print(result)
	return {
		'status': 200,
		'author': result['author'],
		'quotes': result['quotes']
	}

@app.route('/api/quotesnime/random', methods=['GET','POST'])
def quotesnimerandom():
	quotesnime = get('https://animechanapi.xyz/api/quotes/random').json()['data'][0]
	print(quotesnime)
	return {
		'status': 200,
		'data': {
			'quote': quotesnime['quote'],
			'character': quotesnime['character'],
			'anime': quotesnime['anime']
		}
	}

@app.route('/', methods=['GET','POST'])
def index():
	return render_template('index.html')

@app.route('/api', methods=['GET','POST'])
def api():
	return render_template('api.html')

@app.errorhandler(404)
def error(e):
	return render_template('error.html'), 404
if __name__ == '__main__':
	app.run(host='0.0.0.0', port=int(os.environ.get('PORT','5000')),debug=True)
