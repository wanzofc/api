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
from datetime import datetime
from kbbi import KBBI, AutentikasiKBBI
from wikipedia import wikipedia
from flask import Flask, request, abort, redirect, jsonify
from werkzeug.exceptions import *
#from werkzeug.utils import *
from bs4 import BeautifulSoup as bs
from requests import get, post
import os, math, json, random, re, html_text, pytesseract, base64, time, smtplib, convertapi, kbbi

ua_ig = 'Mozilla/5.0 (Linux; Android 10; Redmi Note 9 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.127 Mobile Safari/537.36'

app = Flask(__name__)
keyMe = json.loads(open('ApiKey.json').read())
app.config['MEDIA'] = 'result'
app.secret_key = b'BB,^z\x90\x88?\xcf\xbb'

tp = tp()
abc = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
User_Agent_Instagram = 'Mozilla/5.0 (Linux; Android 9; SM-A102U Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/74.0.3729.136 Mobile Safari/537.36 Instagram 155.0.0.37.107 Android (28/9; 320dpi; 720x1468; samsung; SM-A102U; a10e; exynos7885; en_US; 239490550)'
abc = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'

#========[INFO (Kumpulan Def)]========#
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
def arere(kyun, limit):
	ky = keyMe[kyun]
	a = limit
	b = ky['from']
	c = ky['exp']
	d = ky['status']
	return a, b, c, d
def arara(apikey):
	ky = keyMe[apikey]
	if ky['limit'] < 1:
		return {'creator':'Tobz','status': False, 'error': 'APIKEY LU DAH MAX HARI INI'}
	else:
		ntapz = {'limit': ky['limit'] -1,'from': ky['from'],'exp': ky['exp'],'status': ky['status']}
		keyMe.update({apikey: ntapz})
		return {'creator':'Tobz','status': True}
def now_date():
	l_bln = ['Jan','Feb','Mar','Apr','Mei','Jun','Jul','Agt','Sep','Okt','Nov','Dec']
	waktu = datetime.now(utc).astimezone(timezone('Asia/Jakarta'))
	tgl = waktu.day
	bln = l_bln[waktu.month-1]
	thn = waktu.year
	return '%s - %s - %s' % (tgl, bln, thn)
def next_date():
	l_bln = ['Jan','Feb','Mar','Apr','Mei','Jun','Jul','Agt','Sep','Okt','Nov','Dec']
	waktu = datetime.now(utc).astimezone(timezone('Asia/Jakarta'))
	tgl = waktu.day
	bln = l_bln[waktu.month-12]
	thn = waktu.year+1
	return '%s - %s - %s' % (tgl, bln, thn)
def next1_date():
	l_bln = ['Jan','Feb','Mar','Apr','Mei','Jun','Jul','Agt','Sep','Okt','Nov','Dec']
	waktu = datetime.now(utc).astimezone(timezone('Asia/Jakarta'))
	tgl = waktu.day
	bln = l_bln[waktu.month-11]
	thn = waktu.year+1
	return '%s - %s - %s' % (tgl, bln, thn)
#========[INFO (Router List)]========#
@app.route('/api/refresh')
def refreshcvk():
	for i in keyMe:
		if keyMe[i]['limit'] < 800:
			keyMe.update({i: {
				"from": keyMe[i]['from'],
				"exp": keyMe[i]['exp'],
				"limit": 800,
				"status": keyMe[i]['status']
			}})
		elif keyMe[i]['limit'] > 99999:
			keyMe.update({i: {
				"from": keyMe[i]['from'],
				"exp": keyMe[i]['exp'],
				"limit": 99999999999,
				"status": keyMe[i]['status']
			}})
		else:pass
	return keyMe
@app.route('/api/generatekey', methods=['GET','POST'])
def addNewApi():
	if request.args.get('type') == '1month':
		kya = ''.join(random.choice(abc) for _ in range(20))
		keyMe.update({kya:{
			"limit": 800,
			"from": now_date(),
			"exp": next_date(),
			"status": "Normal"
		}})
		return {
			'status':200,
			'message': 'New api was created : %s' % kya
		}
	elif request.args.get('type') == '2month':
		kya = ''.join(random.choice(abc) for _ in range(20))
		keyMe.update({kya:{
			"limit": 800,
			"from": now_date(),
			"exp": next1_date(),
			"status": "Normal"
		}})
		return {
			'status': 200,
			'message': 'New api was created : %s' % kya
		}
	elif request.args.get('type') == '3month':
		kya = ''.join(random.choice(abc) for _ in range(20))
		keyMe.update({kya:{
			"limit": 800,
			"from": now_date(),
			"exp": next2_date(),
			"status": "Normal"
		}})
		return {
			'status': 200,
			'message': 'New api was created : %s' % kya
		}
	elif request.args.get('type') == 'custom1':
		if request.args.get('key'):
			key = request.args.get('key')
			keyMe.update({key:{
				"limit": 800,
				"from": now_date(),
				"exp": next_date(),
				"status": "Normal"
			}})
			return {
				'status': 200,
				'message': 'New api was created : %s' % key
			}
	elif request.args.get('type') == 'custom2':
		if request.args.get('key'):
			key = request.args.get('key')
			keyMe.update({key:{
				"limit": 800,
				"from": now_date(),
				"exp": next1_date(),
				"status": "Normal"
			}})
			return {
				'status': 200,
				'message': 'New api was created : %s' % key
			}
	elif request.args.get('type') == 'custom3':
		if request.args.get('key'):
			key = request.args.get('key')
			keyMe.update({key:{
				"limit": 800,
				"from": now_date(),
				"exp": next2_date(),
				"status": "Normal"
			}})
			return {
				'status': 200,
				'message': 'New api was created : %s' % key
			}
	elif request.args.get('type') == 'premium1':
		kya = ''.join(random.choice(abc) for _ in range(20))
		keyMe.update({kya: {
			"limit": 9999999999,
			"from": now_date(),
			"exp": next_date(),
			"status": "Premium"
		}})
		return {
			'status': 200,
			'message': 'New api was created : %s' % kya
		}
	elif request.args.get('type') == 'premium2':
		kya = ''.join(random.choice(abc) for _ in range(20))
		keyMe.update({kya: {
			"limit": 999999999,
			"from": now_date(),
			"exp": next1_date(),
			"status": "Premium"
		}})
		return {
			'status': 200,
			'message': 'New api was created : %s' % kya
		}
	elif request.args.get('type') == 'premium3':
		kya = ''.join(random.choice(abc) for _ in range(20))
		keyMe.update({kya: {
			"limit": 999999999,
			"from": now_date(),
			"exp": next2_date(),
			"status": "Premium"
		}})
		return {
			'status': 200,
			'message': 'New api was created : %s' % kya
		}
	elif request.args.get('type') == 'master':
		if request.args.get('custom'):
			kya = request.args.get('custom')
		else:
			kya = ''.join(random.choice(abc) for _ in range(20))
			keyMe.update({kya: {
			"limit": 9999999999,
			"from": now_date(),
			"exp": "No Expired",
			"status": "VVIP"
		}})
		return {
			'status': 200,
			'message': 'New api was created : %s' % kya
		}
	else:
		return {
			"msg": "Lo ngentod!"
		}
@app.route('/api/apikeystatus', methods=['GET','POST'])
def check_limit():
	if request.args.get('apikey'):
		if request.args.get('apikey') in keyMe:
			key = keyMe[request.args.get('apikey')]
			return {
				'status': 200,
				'apikey': request.args.get('apikey'),
				'limit_count': key['limit'],
				'created_date': key['from'],
				'expired_date': key['exp'],
				'apikey_status': key['status']
			}
		else:return {'status': False,'message': 'APIKEY LU INVALID TOD'}
	else:return {'status': False,'message': 'Input param apikey'}

@app.route('/deleto', methods=['GET','POST'])
def deleto():
	os.system('rm result/*')
	return {
		'message': 'Sukses mamank'
	}
@app.route('/result/<path:filename>', methods=['GET','POST'])
def sendFile(filename):
	return send_from_directory(app.config['MEDIA'], filename, as_attachment=True)

def convert_size(size_bytes):
	if size_bytes == 0:
		return '0B'
	size_name = ('B', 'KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB')
	i = int(math.floor(math.log(size_bytes, 1024)))
	p = math.pow(1024, i)
	s = round(size_bytes / p, 2)
	return '%s %s' % (s, size_name[i])

#def allowed_file(filename):
#	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSION

@app.route('/api/textpro', methods=['GET','POST'])
def textpro():
	if request.args.get('theme'):
		theme = request.args.get('theme')
		if theme.lower() in tp.theme:
			if theme.lower() == 'glitch':
				if request.args.get('apikey') in keyMe:
					key = request.args.get('apikey')
					hee = arara(key)
					if hee['status'] != True:return hee
					text = request.args.get('text1')
					text2 = request.args.get('text2')
					result = tp.glitchz(text, text2)
					return result
				else:return {'creator': 'Tobz','status': False,'message': 'APIKEY LU INVALID TOD'}
			elif theme.lower() == 'jokerlogo':
				if request.args.get('apikey') in keyMe:
					key = request.args.get('apikey')
					hee = arara(key)
					if hee['status'] != True:return hee
					text = request.args.get('text')
					result = tp.jokerlogo(text)
					return result
				else:return {'creator': 'Tobz','status': False,'message': 'APIKEY LU INVALID TOD'}
			elif theme.lower() == 'blood':
				if request.args.get('apikey') in keyMe:
					key = request.args.get('apikey')
					hee = arara(key)
					if hee['status'] != True:return hee
					text = request.args.get('text')
					result = tp.blood(text)
					return result
				else:return {'creator': 'Tobz','status': False,'message': 'APIKEY LU INVALID TOD'}
			elif theme.lower() == 'snow':
				if request.args.get('apikey') in keyMe:
					key = request.args.get('apikey')
					hee = arara(key)
					if hee['status'] != True:return hee
					text = request.args.get('text')
					result = tp.snow(text)
					return result
				else:return {'creator': 'Tobz','status': False,'message': 'APIKEY LU INVALID TOD'}
			elif theme.lower() == 'dropwater':
				if request.args.get('apikey') in keyMe:
					key = request.args.get('apikey')
					hee = arara(key)
					if hee['status'] != True:return hee
					text = request.args.get('text')
					result = tp.dropwater(text)
					return result
				else:return {'creator': 'Tobz','status': False,'message': 'APIKEY LU INVALID TOD'}
			elif theme.lower() == 'neon_technology':
				if request.args.get('apikey') in keyMe:
					key = request.args.get('apikey')
					hee = arara(key)
					if hee['status'] != True:return hee
					text = request.args.get('text')
					result = tp.neon_technology(text)
					return result
				else:return {'creator': 'Tobz','status': False,'message': 'APIKEY LU INVALID TOD'}
			elif theme.lower() == 'neon_light':
				if request.args.get('apikey') in keyMe:
					key = request.args.get('apikey')
					hee = arara(key)
					if hee['status'] != True:return hee
					text = request.args.get('text')
					result = tp.neon_light(text)
					return result
				else:return {'creator': 'Tobz','status': False,'message': 'APIKEY LU INVALID TOD'}
			elif theme.lower() == 'lionlogo':
				if request.args.get('apikey') in keyMe:
					key = request.args.get('apikey')
					hee = arara(key)
					if hee['status'] != True:return hee
					text = request.args.get('text1')
					text2 = request.args.get('text2')
					result = tp.lionlogo(text, text2)
					return result
				else:return {'creator': 'Tobz','status': False,'message': 'APIKEY LU INVALID TOD'}
			elif theme.lower() == 'wolflogo1':
				if request.args.get('apikey') in keyMe:
					key = request.args.get('apikey')
					hee = arara(key)
					if hee['status'] != True:return hee
					text = request.args.get('text1')
					text2 = request.args.get('text2')
					result = tp.wolflogo1(text, text2)
					return result
				else:return {'creator': 'Tobz','status': False,'message': 'APIKEY LU INVALID TOD'}
			elif theme.lower() == 'wolflogo2':
				if request.args.get('apikey') in keyMe:
					key = request.args.get('apikey')
					hee = arara(key)
					if hee['status'] != True:return hee
					text = request.args.get('text1')
					text2 = request.args.get('text2')
					result = tp.wolflogo2(text, text2)
					return result
				else:return {'creator': 'Tobz','status': False,'message': 'APIKEY LU INVALID TOD'}
			elif theme.lower() == 'ninjalogo':
				if request.args.get('apikey') in keyMe:
					key = request.args.get('apikey')
					hee = arara(key)
					if hee['status'] != True:return hee
					text = request.args.get('text1')
					text2 = request.args.get('text2')
					result = tp.ninjalogo(text, text2)
					return result
			else:return {'error': 'Themma tersebut tidak ditemukan'}
		else:return {'error': 'Themma tersebut tidak ditemukan'}
	else:return {'message': 'Anda belum memasukan parameter : theme'}


@app.route('/tts/<path:filename>', methods=['GET','POST'])
def sendTts(filename):
	return send_from_directory(app.config['MEDIA'], filename, as_attachment=True)

@app.route('/api/spamgmail', methods=['GET','POST'])
def spamgimel():
	if request.args.get('target'):
		if request.args.get('jum'):
			if request.args.get('apikey') in keyMe:
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
			else:return {'creator': 'Tobz','status': False,'message': 'APIKEY LU INVALID TOD'}
		else:return {'status': False,'msg': 'Masukkan parameter jum'}
	else:return {'status': False,'msg': 'Masukkan parameter target'}

@app.route('/api/spamcall', methods=['GET','POST'])
def spamcall():
	if request.args.get('no'):
		no = request.args.get('no')
		if str(no).startswith('8'):
			if request.args.get('apikey') in keyMe:
				q = request.args.get('query')
				kekeyi = request.args.get('apikey')
				if keyMe[kekeyi]['limit'] < 1:return {'creator':'Tobz','status': False,'error': 'APIKEY LU DAH MAX HARI INI'}
				a = keyMe[kekeyi]['limit'] -1
				wkwk = arere(kekeyi, a)
				keyMe.update({kekeyi: {'limit': wkwk[0], 'from': wkwk[1], 'exp': wkwk[2], 'status': wkwk[3]}})
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
			else:return {'creator': 'Tobz','status': False,'message': 'APIKEY LU INVALID TOD'}
		else:return {'status': False,'msg': '[!] Tolong masukkan nomor dengan awalan 8'}
	else:return {'status': False,'msg': '[!] Masukkan parameter no' }

@app.route('/api/spamsms', methods=['GET','POST'])
def spamming():
	if request.args.get('no'):
		if request.args.get('jum'):
			if request.args.get('apikey') in keyMe:
				no = request.args.get('no')
				jum = int(request.args.get('jum'))
				q = request.args.get('query')
				kekeyi = request.args.get('apikey')
				if keyMe[kekeyi]['limit'] < 1:return {'creator':'Tobz','status': False,'error': 'APIKEY LU DAH MAX HARI INI'}
				a = keyMe[kekeyi]['limit'] -1
				wkwk = arere(kekeyi, a)
				keyMe.update({kekeyi: {'limit': wkwk[0], 'from': wkwk[1], 'exp': wkwk[2], 'status': wkwk[3]}})
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
		else:return {'status': False,'msg': '[!] Masukkin parameter jum juga ganteng'}
	else:return {'status': False,'msg': '[!] Masukkan parameter no'}

@app.route('/api/nulis', methods=['POST','GET'])
def nulis_maker():
	if request.args.get('text'):
		text = request.args.get('text')
		if request.args.get('apikey') in keyMe:
			try:
				kekeyi = request.args.get('apikey')
				if keyMe[kekeyi]['limit'] < 1:return {'creator':'Tobz','status': False,'error': 'APIKEY LU DAH MAX HARI INI'}
				a = keyMe[kekeyi]['limit'] -1
				wkwk = arere(kekeyi, a)
				keyMe.update({kekeyi: {'limit': wkwk[0], 'from': wkwk[1], 'exp': wkwk[2], 'status': wkwk[3]}})
				hihi = f'result/{str(random.random())[10:]}.jpg'
				nulis(text)
				return {
					'creator': 'Tobz',
					'status': 200,
					"result": 'https://tobz-api.herokuapp.com/%s' % hihi
					}
			except Exception as e:print (e);return {'creator':'Tobz','status': False,'error': '[!] Upss, terjadi kesalahan'}
		else:return {'creator': 'Tobz','status': False,'message': 'APIKEY LU INVALID TOD'}
	else:return {'creator': 'Tobz','status': False,'message': '[!] Masukkan parameter text'}

@app.route('/api/katahilih', methods=['GET','POST'])
def hilih():
	if request.args.get('kata'):
		if request.args.get('apikey') in keyMe:
			try:
				kekeyi = request.args.get('apikey')
				if keyMe[kekeyi]['limit'] < 1:return {'creator':'Tobz','status': False,'error': 'APIKEY LU DAH MAX HARI INI'}
				a = keyMe[kekeyi]['limit'] -1
				wkwk = arere(kekeyi, a)
				keyMe.update({kekeyi: {'limit': wkwk[0], 'from': wkwk[1], 'exp': wkwk[2], 'status': wkwk[3]}})
				kya = request.args.get('kata')
				pesan=[]
				for i in chat:
					if i.lower() in ['a','u','e','o']:
						if i.isupper():
							pesan.append('I')
						elif i.islower():
							pesan.append('i')
						else:
							pesan.append(i)
					else:
						pesan.append(i)
						result = ''.join(pesan)
					return {
						'creator': 'Tobz',
						'status': 200,
						'kata': result
					}
			except Exception as e:print(e);return {'status': False,'error': '[❗] Yang anda cari tidak bisa saya temukan di wikipedia!'}
		else:return {'creator': 'Tobz','status': False,'message': 'APIKEY LU INVALID TOD'}
	else:return {'status': False,'msg': '[!] Masukkan param q'}

@app.route('/api/wiki', methods=['GET','POST'])
def wikipedia():
	if request.args.get('q'):
		if request.args.get('apikey') in keyMe:
			try:
				kekeyi = request.args.get('apikey')
				if keyMe[kekeyi]['limit'] < 1:return {'creator':'Tobz','status': False,'error': 'APIKEY LU DAH MAX HARI INI'}
				a = keyMe[kekeyi]['limit'] -1
				wkwk = arere(kekeyi, a)
				keyMe.update({kekeyi: {'limit': wkwk[0], 'from': wkwk[1], 'exp': wkwk[2], 'status': wkwk[3]}})
				kya = request.args.get('q')
				cih = f'https://id.wikipedia.org/w/api.php?format=json&action=query&prop=extracts&exintro&explaintext&redirects=1&titles={kya}'
				heuh = get(cih).json()
				heuh_ = heuh['query']['pages']
				hueh = re.findall(r'(\d+)', str(heuh_))
				result = heuh_[hueh[0]]['extract']
				return {
					'creator': 'Tobz',
					'status': 200,
					'result': result
				}
			except Exception as e:print(e);return {'status': False,'error': '[❗] Yang anda cari tidak bisa saya temukan di wikipedia!'}
		else:return {'creator': 'Tobz','status': False,'message': 'APIKEY LU INVALID TOD'}
	else:return {'status': False,'msg': '[!] Masukkan param q'}

@app.route('/api/tts', methods=['GET','POST'])
def tts():
	if request.args.get('text'):
		if request.args.get('apikey') in keyMe:
			try:
				kekeyi = request.args.get('apikey')
				if keyMe[kekeyi]['limit'] < 1:return {'creator':'Tobz','status': False,'error': 'APIKEY LU DAH MAX HARI INI'}
				a = keyMe[kekeyi]['limit'] -1
				wkwk = arere(kekeyi, a)
				keyMe.update({kekeyi: {'limit': wkwk[0], 'from': wkwk[1], 'exp': wkwk[2], 'status': wkwk[3]}})
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
						Tts = get(f'{url}{apikey}').content
						open('tts/tts.mp3','wb').write(Tts)
						return {
							'status': 200,
							'creator': 'Tobz',
							'msg': 'Success convert text to speech!',
							'file': 'https://tobz-api.herokuapp.com/tts/tts.mp3'
						}
					else:
						Tts = get(f'{url}{apikey}').content
						open('tts/tts.mp3','wb').write(Tts)
						return {
							'status': 200,
							'msg': 'Success convert text to speech!',
							'file': 'https://tobz-api.herokuapp.com/tts/tts.mp3'
						}
			except Exception as e:print(e);return {'status': False,'msg': '[!] Upss, terjadi kesalahan'}
		else:return {'creator': 'Tobz','status': False,'message': 'APIKEY LU INVALID TOD'}
	else:return {'status': 200,'msg': '[!] Masukkan parameter text'}

@app.route('/api/ytv', methods=['GET','POST'])
def ytv():
	if request.args.get('url'):
		if request.args.get('apikey') in keyMe:
			try:
				kekeyi = request.args.get('apikey')
				if keyMe[kekeyi]['limit'] < 1:return {'creator':'Tobz','status': False,'error': 'APIKEY LU DAH MAX HARI INI'}
				a = keyMe[kekeyi]['limit'] -1
				wkwk = arere(kekeyi, a)
				keyMe.update({kekeyi: {'limit': wkwk[0], 'from': wkwk[1], 'exp': wkwk[2], 'status': wkwk[3]}})
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
			except Exception as e:print(e);return {'status': False,'error': '[❗] Terjadi kesalahan, mungkin link yang anda kirim tidak valid!'}
		else:return {'creator': 'Tobz','status': False,'message': 'APIKEY LU INVALID TOD'}
	else:return {'status': False,'msg': 'Masukkan parameter url'}

@app.route('/api/yta', methods=['GET','POST'])
def yta():
	if request.args.get('url'):
		if request.args.get('apikey') in keyMe:
			try:
				kekeyi = request.args.get('apikey')
				if keyMe[kekeyi]['limit'] < 1:return {'creator':'Tobz','status': False,'error': 'APIKEY LU DAH MAX HARI INI'}
				a = keyMe[kekeyi]['limit'] -1
				wkwk = arere(kekeyi, a)
				keyMe.update({kekeyi: {'limit': wkwk[0], 'from': wkwk[1], 'exp': wkwk[2], 'status': wkwk[3]}})
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
			except Exception as e:print('Error : %s' % e);return {'status': False,'error': '[❗] Terjadi kesalahan mungkin link yang anda kirim tidak valid!'}
		else:return {'creator': 'Tobz','status': False,'message': 'APIKEY LU INVALID TOD'}
	else:return {'status': False,'msg': '[!] Masukkan parameter url'}

@app.route('/api/chord', methods=['GET','POST'])
def chord():
	if request.args.get('q'):
		if request.args.get('apikey') in keyMe:
			try:
				kekeyi = request.args.get('apikey')
				if keyMe[kekeyi]['limit'] < 1:return {'creator':'Tobz','status': False,'error': 'APIKEY LU DAH MAX HARI INI'}
				a = keyMe[kekeyi]['limit'] -1
				wkwk = arere(kekeyi, a)
				keyMe.update({kekeyi: {'limit': wkwk[0], 'from': wkwk[1], 'exp': wkwk[2], 'status': wkwk[3]}})
				q = request.args.get('q').replace(' ','+')
				id = get('http://app.chordindonesia.com/?json=get_search_results&exclude=date,modified,attachments,comment_count,comment_status,thumbnail,thumbnail_images,author,excerpt,content,categories,tags,comments,custom_fields&search=%s' % q).json()['posts'][0]['id']
				chord = get('http://app.chordindonesia.com/?json=get_post&id=%s' % id).json()
				result = html_text.parse_html(chord['post']['content']).text_content()
				return {
					'status': 200,
					'result': result
				}
			except Exception as e:print(e);return {'status': False,'error': '[❗] Maaf chord yang anda cari tidak dapat saya temukan!'}
		else:return {'creator': 'Tobz','status': False,'message': 'APIKEY LU INVALID TOD'}
	else:return {'status': False,'msg': '[!] Masukkan parameter q'}

@app.route('/api/film2', methods=['GET','POST'])
def zfilm2():
	if request.args.get('q'):
		if request.args.get('apikey') in keyMe:
			try:
				kekeyi = request.args.get('apikey')
				if keyMe[kekeyi]['limit'] < 1:return {'creator':'Tobz','status': False,'error': 'APIKEY LU DAH MAX HARI INI'}
				a = keyMe[kekeyi]['limit'] -1
				wkwk = arere(kekeyi, a)
				keyMe.update({kekeyi: {'limit': wkwk[0], 'from': wkwk[1], 'exp': wkwk[2], 'status': wkwk[3]}})
				query = request.args.get('q')
				url = f'https://rest.farzain.com/api/film.php?id={query}&apikey=fckveza'
				film2 = get(url, headers={'User-Agent': 'Mozilla/5.0 (Linux; Android 8.1.0; CPH1909) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.81 Mobile Safari/537.36'}).json()
				thumb =  film2['Poster']
				thumbnail = shorturl(thumb)
				return {
					'status': 200,
					'creator': 'Tobz',
					'result': {
							'judul': film2['Title'],
							'tahun': film2['Year'],
							'rating': film2['Rated'],
							'dirilis': film2['Released'],
							'durasi': film2['Runtime'],
							'kategori': film2['Genre'],
							'penulis': film2['Writer'],
							'aktor': film2['Actors'],
							'sinopsis': film2['Plot'],
							'bahasa': film2['Language'],
							'negara': film2['Country'],
							'penghargaan': film2['Awards'],
							'thumbnail': thumbnail,
							'metascore': film2['Metascore'],
							'rating_imdb': film2['imdbRating'],
							'voting_imdb': film2['imdbVotes'],
							'tipe': film2['Type'],
							'produksi': film2['Production'],
							'boxoffice': film2['BoxOffice']
						}
					}
			except:
				return {
					'status': False,
					'error': '[❗] Maaf, Text yang anda masukan salah!'
				}
	else:
		return {
			'status': False,
			'msg': '[!] Masukkan parameter wilayah'
		}

@app.route('/api/ig', methods=['GET','POST'])
def igeh():
	if request.args.get('url'):
		if request.args.get('apikey') in keyMe:
			try:
				kekeyi = request.args.get('apikey')
				if keyMe[kekeyi]['limit'] < 1:return {'creator':'Tobz','status': False,'error': 'APIKEY LU DAH MAX HARI INI'}
				a = keyMe[kekeyi]['limit'] -1
				wkwk = arere(kekeyi, a)
				keyMe.update({kekeyi: {'limit': wkwk[0], 'from': wkwk[1], 'exp': wkwk[2], 'status': wkwk[3]}})
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
			except Exception as e:print(e);return {'status': False,'result': 'https://c4.wallpaperflare.com/wallpaper/976/117/318/anime-girls-404-not-found-glowing-eyes-girls-frontline-wallpaper-preview.jpg','error': True}
		else:return {'creator': 'Tobz','status': False,'message': 'APIKEY LU INVALID TOD'}
	else:return {'status': False,'msg': '[!] Masukkan parameter url'}

@app.route('/api/ttp', methods=['GET','POST'])
def ttpz():
	if request.args.get('text'):
		if request.args.get('apikey') in keyMe:
			try:
				kekeyi = request.args.get('apikey')
				if keyMe[kekeyi]['limit'] < 1:return {'creator':'Tobz','status': False,'error': 'APIKEY LU DAH MAX HARI INI'}
				a = keyMe[kekeyi]['limit'] -1
				wkwk = arere(kekeyi, a)
				keyMe.update({kekeyi: {'limit': wkwk[0], 'from': wkwk[1], 'exp': wkwk[2], 'status': wkwk[3]}})
				query = request.args.get('text')
				link = f'https://api.areltiyan.site/sticker_maker?text={query}'
				ttp = get(link).json()
				print(ttp)
				return {
					'status': 200,
					'base64': ttp['base64'],
					'creator': 'Tobz'
				}
			except:return {'status': False,'error': '[❗] Maaf, Text yang anda masukan salah!'}
		else:return {'creator': 'Tobz','status': False,'message': 'APIKEY LU INVALID TOD'}
	else:return {'status': False,'msg': '[!] Masukkan parameter text'}

@app.route('/api/facebook', methods=['GET','POST'])
def zfb():
	if request.args.get('url'):
		if request.args.get('apikey') in keyMe:
			try:
				kekeyi = request.args.get('apikey')
				if keyMe[kekeyi]['limit'] < 1:return {'creator':'Tobz','status': False,'error': 'APIKEY LU DAH MAX HARI INI'}
				a = keyMe[kekeyi]['limit'] -1
				wkwk = arere(kekeyi, a)
				keyMe.update({kekeyi: {'limit': wkwk[0], 'from': wkwk[1], 'exp': wkwk[2], 'status': wkwk[3]}})
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
			except:return {'status': False,'error': '[❗] Maaf, Url yang anda masukan salah!'}
		else:return {'creator': 'Tobz','status': False,'message': 'APIKEY LU INVALID TOD'}
	else:return {'status': False,'msg': '[!] Masukkan parameter url'}

@app.route('/api/artinama', methods=['GET','POST'])
def artin():
	if request.args.get('nama'):
		if request.args.get('apikey') in keyMe:
			try:
				kekeyi = request.args.get('apikey')
				if keyMe[kekeyi]['limit'] < 1:return {'creator':'Tobz','status': False,'error': 'APIKEY LU DAH MAX HARI INI'}
				a = keyMe[kekeyi]['limit'] -1
				wkwk = arere(kekeyi, a)
				keyMe.update({kekeyi: {'limit': wkwk[0], 'from': wkwk[1], 'exp': wkwk[2], 'status': wkwk[3]}})
				query = request.args.get('nama')
				link = f'https://mnazria.herokuapp.com/api/arti?nama={query}'
				art = get(link).json()
				print(art)
				return {
					'status': 200,
					'result': art['result'],
					'creator': 'Tobz'
				}
			except:return {'status': False,'error': '[❗] Maaf, Text yang anda masukan salah!'}
		else:return {'creator': 'Tobz','status': False,'message': 'APIKEY LU INVALID TOD'}
	else:return {'status': False,'msg': '[!] Masukkan parameter text'}

@app.route('/api/kbbi', methods=['GET','POST'])
def kbbz():
	if request.args.get('kata'):
		if request.args.get('apikey') in keyMe:
			try:
				kekeyi = request.args.get('apikey')
				if keyMe[kekeyi]['limit'] < 1:return {'creator':'Tobz','status': False,'error': 'APIKEY LU DAH MAX HARI INI'}
				a = keyMe[kekeyi]['limit'] -1
				wkwk = arere(kekeyi, a)
				keyMe.update({kekeyi: {'limit': wkwk[0], 'from': wkwk[1], 'exp': wkwk[2], 'status': wkwk[3]}})
				query = request.args.get('kata')
				url = get('https://mnazria.herokuapp.com/api/kbbi?search={}'.format(query)).json()['result']
				return {
					'status': 200,
					'result': url,
					'creator': 'Tobz'
				}
			except:return {'status': False,'error': '[❗] Maaf, Kata yang anda masukan salah!'}
		else:return {'creator': 'Tobz','status': False,'message': 'APIKEY LU INVALID TOD'}
	else:return {'status': False,'msg': '[!] Masukkan parameter kata'}

@app.route('/api/jadwalshalat', methods=['GET','POST'])
def jshalat():
	if request.args.get('q'):
		if request.args.get('apikey') in keyMe:
			try:
				kekeyi = request.args.get('apikey')
				if keyMe[kekeyi]['limit'] < 1:return {'creator':'Tobz','status': False,'error': 'APIKEY LU DAH MAX HARI INI'}
				a = keyMe[kekeyi]['limit'] -1
				wkwk = arere(kekeyi, a)
				keyMe.update({kekeyi: {'limit': wkwk[0], 'from': wkwk[1], 'exp': wkwk[2], 'status': wkwk[3]}})
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
			except:return {'status': False,'error': '[❗] Maaf, Daerah yang anda masukan salah!'}
		else:return {'creator': 'Tobz','status': False,'message': 'APIKEY LU INVALID TOD'}
	else:return {'status': False,'msg': '[!] Masukkan parameter daerah'}

@app.route('/api/joox', methods=['GET','POST'])
def zjoox():
	if request.args.get('q'):
		if request.args.get('apikey') in keyMe:
			try:
				kekeyi = request.args.get('apikey')
				if keyMe[kekeyi]['limit'] < 1:return {'creator':'Tobz','status': False,'error': 'APIKEY LU DAH MAX HARI INI'}
				a = keyMe[kekeyi]['limit'] -1
				wkwk = arere(kekeyi, a)
				keyMe.update({kekeyi: {'limit': wkwk[0], 'from': wkwk[1], 'exp': wkwk[2], 'status': wkwk[3]}})
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
			except:return {'status': False,'error': '[❗] Maaf, Query yang anda masukan salah!'}
		else:return {'creator': 'Tobz','status': False,'message': 'APIKEY LU INVALID TOD'}
	else:return {'status': False,'msg': '[!] Masukkan parameter q'}

@app.route('/api/lirik', methods=['GET','POST'])
def zlirik():
	if request.args.get('q'):
		if request.args.get('apikey') in keyMe:
			try:
				kekeyi = request.args.get('apikey')
				if keyMe[kekeyi]['limit'] < 1:return {'creator':'Tobz','status': False,'error': 'APIKEY LU DAH MAX HARI INI'}
				a = keyMe[kekeyi]['limit'] -1
				wkwk = arere(kekeyi, a)
				keyMe.update({kekeyi: {'limit': wkwk[0], 'from': wkwk[1], 'exp': wkwk[2], 'status': wkwk[3]}})
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
			except:return {'status': False,'error': '[❗] Maaf, Query yang anda masukan salah!'}
		else:return {'creator': 'Tobz','status': False,'message': 'APIKEY LU INVALID TOD'}
	else:return {'status': False,'msg': '[!] Masukkan parameter q'}

@app.route('/api/simsimi', methods=['GET','POST'])
def simi():
	if request.args.get('text'):
		if request.args.get('apikey') in keyMe:
			try:
				kekeyi = request.args.get('apikey')
				if keyMe[kekeyi]['limit'] < 1:return {'creator':'Tobz','status': False,'error': 'APIKEY LU DAH MAX HARI INI'}
				a = keyMe[kekeyi]['limit'] -1
				wkwk = arere(kekeyi, a)
				keyMe.update({kekeyi: {'limit': wkwk[0], 'from': wkwk[1], 'exp': wkwk[2], 'status': wkwk[3]}})
				query = request.args.get('text')
				url = f'http://simsumi.herokuapp.com/api?text={query}&lang=id'
				sim = get(url).json()
				print(sim)
				return {
					'status': 200,
					'result': sim['success'],
					'creator': 'Tobz'
				}
			except:return {'status': False,'error': '[❗] Maaf, Text yang anda masukan salah!'}
		else:return {'creator': 'Tobz','status': False,'message': 'APIKEY LU INVALID TOD'}
	else:return {'status': False,'msg': '[!] Masukkan parameter text'}

@app.route('/api/cuaca', methods=['GET','POST'])
def zcuaca():
	if request.args.get('wilayah'):
		if request.args.get('apikey') in keyMe:
			try:
				kekeyi = request.args.get('apikey')
				if keyMe[kekeyi]['limit'] < 1:return {'creator':'Tobz','status': False,'error': 'APIKEY LU DAH MAX HARI INI'}
				a = keyMe[kekeyi]['limit'] -1
				wkwk = arere(kekeyi, a)
				keyMe.update({kekeyi: {'limit': wkwk[0], 'from': wkwk[1], 'exp': wkwk[2], 'status': wkwk[3]}})
				query = request.args.get('wilayah')
				url = f'https://rest.farzain.com/api/cuaca.php?id={query}&apikey=fckveza'
				weather = get(url, headers={'User-Agent': 'Mozilla/5.0 (Linux; Android 8.1.0; CPH1909) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.81 Mobile Safari/537.36'}).json()
				return {
					'status': 200,
					'creator': 'Tobz',
					'result': {
							'tempat': weather['respon']['tempat'],
							'cuaca': weather['respon']['cuaca'],
							'desk': weather['respon']['deskripsi'],
							'suhu': weather['respon']['suhu'],
							'kelembapan': weather['respon']['kelembapan'],
							'udara': weather['respon']['udara'],
							'angin': weather['respon']['angin']
						}
					}
			except:
				return {
					'status': False,
					'error': '[❗] Maaf, Text yang anda masukan salah!'
				}
	else:
		return {
			'status': False,
			'msg': '[!] Masukkan parameter wilayah'
		}

@app.route('/api/film', methods=['GET','POST'])
def zfilm():
	if request.args.get('q'):
		if request.args.get('apikey') in keyMe:
			try:
				kekeyi = request.args.get('apikey')
				if keyMe[kekeyi]['limit'] < 1:return {'creator':'Tobz','status': False,'error': 'APIKEY LU DAH MAX HARI INI'}
				a = keyMe[kekeyi]['limit'] -1
				wkwk = arere(kekeyi, a)
				keyMe.update({kekeyi: {'limit': wkwk[0], 'from': wkwk[1], 'exp': wkwk[2], 'status': wkwk[3]}})
				query = request.args.get('q')
				data = []
				result = {"creator":"Tobz","result": data}
				url = bsoup("http://167.99.71.200/?s={}&post_type%5B%5D=post&post_type%5B%5D=tv".format(query))
				for tobz in url.findAll('article', attrs={'itemscope':'itemscope'}):
					title = tobz.a['title']
					link = tobz.a['href']
					img = tobz.img['src']
					image = shorturl(img)
					rating = tobz.find('div', class_='gmr-rating-item').text.replace('Rating: ','')+'/10'
					genre_negara = tobz.find('div', class_='gmr-movie-on').text
					hasil = data.append({"judul":title,"thumb":image,"link":link,"rating":rating,"genre_negara":genre_negara})
				return {
					'status': 200,
					'creator':'Tobz',
					'result': data
				}
			except Exception as e:print(e);return {'status': False,'error': 'Url %s Tidak di temukan!' % unquote(query)}
		else:return {'creator': 'Tobz','status': False,'message': 'APIKEY LU INVALID TOD'}
	else:return {'status': False,'msg': 'input parameter q'}

@app.route('/api/film2', methods=['GET','POST'])
def zfilmzs():
	if request.args.get('q'):
		if request.args.get('apikey') in keyMe:
			try:
				kekeyi = request.args.get('apikey')
				if keyMe[kekeyi]['limit'] < 1:return {'creator':'Tobz','status': False,'error': 'APIKEY LU DAH MAX HARI INI'}
				a = keyMe[kekeyi]['limit'] -1
				wkwk = arere(kekeyi, a)
				keyMe.update({kekeyi: {'limit': wkwk[0], 'from': wkwk[1], 'exp': wkwk[2], 'status': wkwk[3]}})
				query = request.args.get('q')
				url = f'https://rest.farzain.com/api/film.php?id={query}&apikey=fckveza'
				film2 = get(url, headers={'User-Agent': 'Mozilla/5.0 (Linux; Android 8.1.0; CPH1909) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.81 Mobile Safari/537.36'}).json()
				thumb =  film2['Poster']
				thumbnail = shorturl(thumb)
				return {
					'status': 200,
					'creator': 'Tobz',
					'result': {
							'judul': film2['Title'],
							'tahun': film2['Year'],
							'rating': film2['Rated'],
							'dirilis': film2['Released'],
							'durasi': film2['Runtime'],
							'kategori': film2['Genre'],
							'penulis': film2['Writer'],
							'aktor': film2['Actors'],
							'sinopsis': film2['Plot'],
							'bahasa': film2['Language'],
							'negara': film2['Country'],
							'penghargaan': film2['Awards'],
							'thumbnail': thumbnail,
							'metascore': film2['Metascore'],
							'rating_imdb': film2['imdbRating'],
							'voting_imdb': film2['imdbVotes'],
							'tipe': film2['Type'],
							'produksi': film2['Production'],
							'boxoffice': film2['BoxOffice']
						}
					}
			except:
				return {
					'status': False,
					'error': '[❗] Maaf, Text yang anda masukan salah!'
				}
	else:
		return {
			'status': False,
			'msg': '[!] Masukkan parameter wilayah'
		}

@app.route('/api/jamdunia', methods=['GET','POST'])
def zjamdunia():
	if request.args.get('lokasi'):
		if request.args.get('apikey') in keyMe:
			try:
				kekeyi = request.args.get('apikey')
				if keyMe[kekeyi]['limit'] < 1:return {'creator':'Tobz','status': False,'error': 'APIKEY LU DAH MAX HARI INI'}
				a = keyMe[kekeyi]['limit'] -1
				wkwk = arere(kekeyi, a)
				keyMe.update({kekeyi: {'limit': wkwk[0], 'from': wkwk[1], 'exp': wkwk[2], 'status': wkwk[3]}})
				query = request.args.get('lokasi')
				data = []
				result = {"creator":"Tobz","result": data}
				url = bsoup("https://time.is/id/{}".format(query))
				for Tobz in url.findAll('div', attrs={'id':'time_section'}):
					title = Tobz.h1.text
					time = Tobz.find('div', attrs={'id':'clock0_bg'}).text
					date = Tobz.find('div', class_='w90 tr clockdate').text
					sun = Tobz.find('span', class_='nw').text
					hasil = data.append({"title":title,"time":time,"date":date,"sun":sun})
				return {
					'status': 200,
					'creator':'Tobz',
					'result': data
				}
			except Exception as e:print(e);return {'status': False,'error': 'Url %s Tidak di temukan!' % unquote(query)}
		else:return {'creator': 'Tobz','status': False,'message': 'APIKEY LU INVALID TOD'}
	else:return {'status': False,'msg': 'input parameter q'}

@app.route('/api/bitly', methods=['GET','POST'])
def bitzly():
	if request.args.get('url'):
		if request.args.get('apikey') in keyMe:
			try:
				kekeyi = request.args.get('apikey')
				if keyMe[kekeyi]['limit'] < 1:return {'creator':'Tobz','status': False,'error': 'APIKEY LU DAH MAX HARI INI'}
				a = keyMe[kekeyi]['limit'] -1
				wkwk = arere(kekeyi, a)
				keyMe.update({kekeyi: {'limit': wkwk[0], 'from': wkwk[1], 'exp': wkwk[2], 'status': wkwk[3]}})
				query = request.args.get('url')
				url = get("https://api-ssl.bitly.com/v3/shorten?access_token=eeed32b267a6f473e0e824aa685527cf1e18a5e6&longUrl={}".format(query)).json()
				data = url['data']['url']
				return {
					'status': 200,
					'creator':'Tobz',
					'result': data
				}
			except Exception as e:print(e);return {'status': False,'error': 'Url %s Tidak di temukan!' % unquote(query)}
		else:return {'creator': 'Tobz','status': False,'message': 'APIKEY LU INVALID TOD'}
	else:return {'status': False,'msg': 'input parameter url'}

@app.route('/api/tinyurl', methods=['GET','POST'])
def tinyurlz():
	if request.args.get('url'):
		if request.args.get('apikey') in keyMe:
			try:
				kekeyi = request.args.get('apikey')
				if keyMe[kekeyi]['limit'] < 1:return {'creator':'Tobz','status': False,'error': 'APIKEY LU DAH MAX HARI INI'}
				a = keyMe[kekeyi]['limit'] -1
				wkwk = arere(kekeyi, a)
				keyMe.update({kekeyi: {'limit': wkwk[0], 'from': wkwk[1], 'exp': wkwk[2], 'status': wkwk[3]}})
				query = request.args.get('url')
				url = requests.get("https://tinyurl.com/api-create.php?url={}".format(query))
				data = url.text
				print(data)
				return {
					'status': 200,
					'creator':'Tobz',
					'result': data
				}
			except Exception as e:print(e);return {'status': False,'error': 'Url %s Tidak di temukan!' % unquote(query)}
		else:return {'creator': 'Tobz','status': False,'message': 'APIKEY LU INVALID TOD'}
	else:return {'status': False,'msg': 'input parameter url'}

#===[ANIME & MANGA]===#

@app.route('/api/bacakomik', methods=['GET','POST'])
def zbacakimik():
	if request.args.get('q'):
		if request.args.get('apikey') in keyMe:
			try:
				kekeyi = request.args.get('apikey')
				if keyMe[kekeyi]['limit'] < 1:return {'creator':'Tobz','status': False,'error': 'APIKEY LU DAH MAX HARI INI'}
				a = keyMe[kekeyi]['limit'] -1
				wkwk = arere(kekeyi, a)
				keyMe.update({kekeyi: {'limit': wkwk[0], 'from': wkwk[1], 'exp': wkwk[2], 'status': wkwk[3]}})
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
				dilihat = txt[9].text.replace('Dilihat: ','')
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
					'result':hasilnya
				}
			except Exception as e:print(e);return {'status': False,'error': 'Anime %s Tidak di temukan!' % unquote(query)}
		else:return {'creator': 'Tobz','status': False,'message': 'APIKEY LU INVALID TOD'}
	else:return {'status': False,'msg': 'input parameter q'}

@app.route('/api/kiryuu', methods=['GET','POST'])
def zkiryuu():
	if request.args.get('q'):
		if request.args.get('apikey') in keyMe:
			try:
				kekeyi = request.args.get('apikey')
				if keyMe[kekeyi]['limit'] < 1:return {'creator':'Tobz','status': False,'error': 'APIKEY LU DAH MAX HARI INI'}
				a = keyMe[kekeyi]['limit'] -1
				wkwk = arere(kekeyi, a)
				keyMe.update({kekeyi: {'limit': wkwk[0], 'from': wkwk[1], 'exp': wkwk[2], 'status': wkwk[3]}})
				query = request.args.get('q')
				data = []
				result = {"creator":"Tobz","result": data}
				url = bsoup("https://kiryuu.co/?s={}".format(query))
				for Tobz in url.findAll('div',class_='bs'):
					title = "{}".format(str(Tobz.find('a')['title']))
					img = "{}".format(str(Tobz.find('img')['src']))
					image = shorturl(img)
					link = "{}".format(str(Tobz.find('a')['href']))
					format = Tobz.find('div', class_='limit').text.replace('\n','').replace(' ','')
					chapter = Tobz.find('div', class_='adds').text.replace('\n','')
					rating = Tobz.find('div', class_='numscore').text
					info = bsoup(link)
					gen = info.find('span', class_='mgen').text.replace(' ',', ')
					sinopsis = info.find('div', class_='entry-content entry-content-single').text.replace('\n','')
					follow = info.find('div', class_='bmc').text
					txtz = info.find('div', class_='tsinfo bixbox')
					status = txtz.findAll('div')[0].text.replace('\n','').replace('Status ','').replace('\t','')
					type = txtz.findAll('div')[1].text.replace('\n','').replace('Type ','').replace('\t','')
					hasil = data.append({"title":title,"image":image,"link":link,"format":format,"chapter":chapter,"rating":rating,"follow":follow,"status":status,"type":type,"sinopsis":sinopsis,"genre":gen})
				return {
					'status': 200,
					'creator':'Tobz',
					'result':data
				}
			except Exception as e:print(e);return {'status': False,'error': 'Anime %s Tidak di temukan!' % unquote(query)}
		else:return {'creator': 'Tobz','status': False,'message': 'APIKEY LU INVALID TOD'}
	else:return {'status': False,'msg': 'input parameter q'}

@app.route('/api/neonime', methods=['GET','POST'])
def zneonime():
	if request.args.get('q'):
		if request.args.get('apikey') in keyMe:
			try:
				kekeyi = request.args.get('apikey')
				if keyMe[kekeyi]['limit'] < 1:return {'creator':'Tobz','status': False,'error': 'APIKEY LU DAH MAX HARI INI'}
				a = keyMe[kekeyi]['limit'] -1
				wkwk = arere(kekeyi, a)
				keyMe.update({kekeyi: {'limit': wkwk[0], 'from': wkwk[1], 'exp': wkwk[2], 'status': wkwk[3]}})
				query = request.args.get('q')
				data = []
				url = requests.get("https://neonime.vip/?s={}".format(query))
				tbz = BeautifulSoup(url.content,'html.parser')
				desc = tbz.find('span', {'class': 'ttx'}).text
				for Tobz in tbz.find_all('div',class_='item episode-home'):
					link = "{}".format(str(Tobz.find('a')['href']))
					title = "{}".format(str(Tobz.find('img')['alt']))
					image = "{}".format(str(Tobz.find('img')['data-src'])).replace(' ',"")
					hasil = data.append({"title":title,"desc": desc,"image":image,"link":link})
				return {
					'status': 200,
					'creator':'Tobz',
					'result':data
				}
			except Exception as e:print(e);return {'status': False,'error': 'Anime %s Tidak di temukan!' % unquote(query)}
		else:return {'creator': 'Tobz','status': False,'message': 'APIKEY LU INVALID TOD'}
	else:return {'status': False,'msg': 'input parameter q'}

@app.route('/api/anoboy', methods=['GET','POST'])
def zanoboy():
	if request.args.get('q'):
		if request.args.get('apikey') in keyMe:
			try:
				kekeyi = request.args.get('apikey')
				if keyMe[kekeyi]['limit'] < 1:return {'creator':'Tobz','status': False,'error': 'APIKEY LU DAH MAX HARI INI'}
				a = keyMe[kekeyi]['limit'] -1
				wkwk = arere(kekeyi, a)
				keyMe.update({kekeyi: {'limit': wkwk[0], 'from': wkwk[1], 'exp': wkwk[2], 'status': wkwk[3]}})
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
			except Exception as e:print(e);return {'status': False,'error': 'Anime %s Tidak di temukan!' % unquote(query)}
		else:return {'creator': 'Tobz','status': False,'message': 'APIKEY LU INVALID TOD'}
	else:return {'status': False,'msg': 'input parameter q'}

@app.route('/api/dewabatch', methods=['GET','POST'])
def dewabatch():
	if request.args.get('q'):
		if request.args.get('apikey') in keyMe:
			try:
				kekeyi = request.args.get('apikey')
				if keyMe[kekeyi]['limit'] < 1:return {'creator':'Tobz','status': False,'error': 'APIKEY LU DAH MAX HARI INI'}
				a = keyMe[kekeyi]['limit'] -1
				wkwk = arere(kekeyi, a)
				keyMe.update({kekeyi: {'limit': wkwk[0], 'from': wkwk[1], 'exp': wkwk[2], 'status': wkwk[3]}})
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
			except Exception as e:print(e);return {'status': False,'error': 'Anime %s Tidak di temukan!' % unquote(q)}
		else:return {'creator': 'Tobz','status': False,'message': 'APIKEY LU INVALID TOD'}
	else:return {'status': False,'msg': '[!] Masukkan parameter q'}

@app.route('/api/kuso', methods=['GET','POST'])
def kusonime():
	if request.args.get('q'):
		if request.args.get('apikey') in keyMe:
			try:
				kekeyi = request.args.get('apikey')
				if keyMe[kekeyi]['limit'] < 1:return {'creator':'Tobz','status': False,'error': 'APIKEY LU DAH MAX HARI INI'}
				a = keyMe[kekeyi]['limit'] -1
				wkwk = arere(kekeyi, a)
				keyMe.update({kekeyi: {'limit': wkwk[0], 'from': wkwk[1], 'exp': wkwk[2], 'status': wkwk[3]}})
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
			except Exception as e:print(e);return {'status': False,'error': 'Anime %s Tidak di temukan' % unquote(q)}
		else:return {'creator': 'Tobz','status': False,'message': 'APIKEY LU INVALID TOD'}
	else:return {'status': False,'msg': '[!] Masukkan parameter q'}

@app.route('/api/nekonime', methods=['GET','POST'])
def nekonimek():
	if request.args.get('apikey') in keyMe:
		kekeyi = request.args.get('apikey')
		if keyMe[kekeyi]['limit'] < 1:return {'creator':'Tobz','status': False,'error': 'APIKEY LU DAH MAX HARI INI'}
		a = keyMe[kekeyi]['limit'] -1
		wkwk = arere(kekeyi, a)
		keyMe.update({kekeyi: {'limit': wkwk[0], 'from': wkwk[1], 'exp': wkwk[2], 'status': wkwk[3]}})
		neko = get('https://waifu.pics/api/sfw/neko').json()
		nimek = neko['url']
		return {
			'status': 200,
			'result': nimek
		}
	else:
		return {
			'creator': 'Tobz',
			'status': False,
			'message': 'APIKEY LU INVALID TOD'
		}

@app.route('/api/cry', methods=['GET','POST'])
def crynime():
	if request.args.get('apikey') in keyMe:
		kekeyi = request.args.get('apikey')
		if keyMe[kekeyi]['limit'] < 1:return {'creator':'Tobz','status': False,'error': 'APIKEY LU DAH MAX HARI INI'}
		a = keyMe[kekeyi]['limit'] -1
		wkwk = arere(kekeyi, a)
		keyMe.update({kekeyi: {'limit': wkwk[0], 'from': wkwk[1], 'exp': wkwk[2], 'status': wkwk[3]}})
		cryz = get('https://waifu.pics/api/sfw/cry').json()
		ncry = cryz['url']
		return {
			'status': 200,
			'result': ncry
		}
	else:
		return {
			'creator': 'Tobz',
			'status': False,
			'message': 'APIKEY LU INVALID TOD'
		}

@app.route('/api/kiss', methods=['GET','POST'])
def kissnime():
	if request.args.get('apikey') in keyMe:
		kekeyi = request.args.get('apikey')
		if keyMe[kekeyi]['limit'] < 1:return {'creator':'Tobz','status': False,'error': 'APIKEY LU DAH MAX HARI INI'}
		a = keyMe[kekeyi]['limit'] -1
		wkwk = arere(kekeyi, a)
		keyMe.update({kekeyi: {'limit': wkwk[0], 'from': wkwk[1], 'exp': wkwk[2], 'status': wkwk[3]}})
		rkiss = get('https://waifu.pics/api/sfw/kiss').json()
		nkiss = rkiss['url']
		return {
			'status': 200,
			'result': nkiss
		}
	else:
		return {
			'creator': 'Tobz',
			'status': False,
			'message': 'APIKEY LU INVALID TOD'
		}

@app.route('/api/hug', methods=['GET','POST'])
def hugnime():
	if request.args.get('apikey') in keyMe:
		kekeyi = request.args.get('apikey')
		if keyMe[kekeyi]['limit'] < 1:return {'creator':'Tobz','status': False,'error': 'APIKEY LU DAH MAX HARI INI'}
		a = keyMe[kekeyi]['limit'] -1
		wkwk = arere(kekeyi, a)
		keyMe.update({kekeyi: {'limit': wkwk[0], 'from': wkwk[1], 'exp': wkwk[2], 'status': wkwk[3]}})
		hugz = get('https://waifu.pics/api/sfw/hug').json()
		nhug = hugz['url']
		return {
			'status': 200,
			'result': nhug
		}
	else:
		return {
			'creator': 'Tobz',
			'status': False,
			'message': 'APIKEY LU INVALID TOD'
		}

@app.route('/api/randomanime', methods=['GET','POST'])
def randomanime():
	if request.args.get('apikey') in keyMe:
		kekeyi = request.args.get('apikey')
		if keyMe[kekeyi]['limit'] < 1:return {'creator':'Tobz','status': False,'error': 'APIKEY LU DAH MAX HARI INI'}
		a = keyMe[kekeyi]['limit'] -1
		wkwk = arere(kekeyi, a)
		keyMe.update({kekeyi: {'limit': wkwk[0], 'from': wkwk[1], 'exp': wkwk[2], 'status': wkwk[3]}})
		rnime = ['waifu','neko','shinobu','megumin']
		nnimee = get('https://waifu.pics/api/sfw/%s' % random.choice(rnime)).json()
		nimee = nnimee['url']
		return {
			'status': 200,
			'result': nimee
		}
	else:
		return {
			'creator': 'Tobz',
			'status': False,
			'message': 'APIKEY LU INVALID TOD'
		}

@app.route('/api/randomloli', methods=['GET','POST'])
def randomloli():
	if request.args.get('apikey') in keyMe:
		kekeyi = request.args.get('apikey')
		if keyMe[kekeyi]['limit'] < 1:return {'creator':'Tobz','status': False,'error': 'APIKEY LU DAH MAX HARI INI'}
		a = keyMe[kekeyi]['limit'] -1
		wkwk = arere(kekeyi, a)
		keyMe.update({kekeyi: {'limit': wkwk[0], 'from': wkwk[1], 'exp': wkwk[2], 'status': wkwk[3]}})
		hehe = ['kawaii','neko']
		loli = get('https://api.lolis.life/%s' % random.choice(hehe)).json()['url']
		return {
			'status': 200,
			'result': loli
		}
	else:
		return {
			'creator': 'Tobz',
			'status': False,
			'message': 'APIKEY LU INVALID TOD'
		}

@app.route('/api/nsfwblowjob', methods=['GET','POST'])
def blowjob():
	if request.args.get('apikey') in keyMe:
		kekeyi = request.args.get('apikey')
		if keyMe[kekeyi]['limit'] < 1:return {'creator':'Tobz','status': False,'error': 'APIKEY LU DAH MAX HARI INI'}
		a = keyMe[kekeyi]['limit'] -1
		wkwk = arere(kekeyi, a)
		keyMe.update({kekeyi: {'limit': wkwk[0], 'from': wkwk[1], 'exp': wkwk[2], 'status': wkwk[3]}})
		nblow = get('https://waifu.pics/api/nsfw/blowjob').json()
		bblow = nblow['url']
		return {
			'status': 200,
			'result': bblow
		}
	else:
		return {
			'creator': 'Tobz',
			'status': False,
			'message': 'APIKEY LU INVALID TOD'
		}

@app.route('/api/hentai', methods=['GET','POST'])
def hentai():
	if request.args.get('apikey') in keyMe:
		kekeyi = request.args.get('apikey')
		if keyMe[kekeyi]['limit'] < 1:return {'creator':'Tobz','status': False,'error': 'APIKEY LU DAH MAX HARI INI'}
		a = keyMe[kekeyi]['limit'] -1
		wkwk = arere(kekeyi, a)
		keyMe.update({kekeyi: {'limit': wkwk[0], 'from': wkwk[1], 'exp': wkwk[2], 'status': wkwk[3]}})
		nblow = get('https://waifu.pics/api/nsfw/waifu').json()
		bblow = nblow['url']
		return {
			'status': 200,
			'result': bblow
		}
	else:
		return {
			'creator': 'Tobz',
			'status': False,
			'message': 'APIKEY LU INVALID TOD'
		}

@app.route('/api/nsfwneko', methods=['GET','POST'])
def nsfwneko():
	if request.args.get('apikey') in keyMe:
		kekeyi = request.args.get('apikey')
		if keyMe[kekeyi]['limit'] < 1:return {'creator':'Tobz','status': False,'error': 'APIKEY LU DAH MAX HARI INI'}
		a = keyMe[kekeyi]['limit'] -1
		wkwk = arere(kekeyi, a)
		keyMe.update({kekeyi: {'limit': wkwk[0], 'from': wkwk[1], 'exp': wkwk[2], 'status': wkwk[3]}})
		nneko = get('https://waifu.pics/api/nsfw/neko').json()
		nekko = nneko['url']
		return {
			'status': 200,
			'result': nekko
		}
	else:
		return {
			'creator': 'Tobz',
			'status': False,
			'message': 'APIKEY LU INVALID TOD'
		}

@app.route('/api/nsfwtrap', methods=['GET','POST'])
def trapnime():
	if request.args.get('apikey') in keyMe:
		kekeyi = request.args.get('apikey')
		if keyMe[kekeyi]['limit'] < 1:return {'creator':'Tobz','status': False,'error': 'APIKEY LU DAH MAX HARI INI'}
		a = keyMe[kekeyi]['limit'] -1
		wkwk = arere(kekeyi, a)
		keyMe.update({kekeyi: {'limit': wkwk[0], 'from': wkwk[1], 'exp': wkwk[2], 'status': wkwk[3]}})
		trap = get('https://waifu.pics/api/nsfw/trap').json()
		ntrap = trap['url']
		return {
			'status': 200,
			'result': ntrap
		}
	else:
		return {
			'creator': 'Tobz',
			'status': False,
			'message': 'APIKEY LU INVALID TOD'
		}

@app.route('/api/neolast', methods=['GET','POST'])
def zneolast():
	if request.args.get('apikey') in keyMe:
		kekeyi = request.args.get('apikey')
		if keyMe[kekeyi]['limit'] < 1:return {'creator':'Tobz','status': False,'error': 'APIKEY LU DAH MAX HARI INI'}
		a = keyMe[kekeyi]['limit'] -1
		wkwk = arere(kekeyi, a)
		keyMe.update({kekeyi: {'limit': wkwk[0], 'from': wkwk[1], 'exp': wkwk[2], 'status': wkwk[3]}})
		data = []
		url = requests.get("https://neonime.vip")
		tbz = BeautifulSoup(url.content,'html.parser')
		desc = tbz.find('span', {'class': 'ttx'}).text
		for Tobz in tbz.findAll('div',class_='item episode-home'):
			link = "{}".format(str(Tobz.find('a')['href']))
			title = "{}".format(str(Tobz.find('img')['alt']))
			image = "{}".format(str(Tobz.find('img')['data-src'])).replace(' ',"")
			hasil = data.append({"title":title,"desc": desc,"image":image,"link":link})
		return {
			'status': 200,
			'creator': 'Tobz',
			'result': data
		}
	else:
		return {
			'creator': 'Tobz',
			'status': False,
			'message': 'APIKEY LU INVALID TOD'
		}

@app.route('/api/anolast', methods=['GET','POST'])
def zanolast():
	if request.args.get('apikey') in keyMe:
		kekeyi = request.args.get('apikey')
		if keyMe[kekeyi]['limit'] < 1:return {'creator':'Tobz','status': False,'error': 'APIKEY LU DAH MAX HARI INI'}
		a = keyMe[kekeyi]['limit'] -1
		wkwk = arere(kekeyi, a)
		keyMe.update({kekeyi: {'limit': wkwk[0], 'from': wkwk[1], 'exp': wkwk[2], 'status': wkwk[3]}})
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
	else:
		return {
			'creator': 'Tobz',
			'status': False,
			'message': 'APIKEY LU INVALID TOD'
		}

#===[ANIME & MANGA]===#

@app.route('/api/screenshotweb', methods=['GET','POST'])
def zssweb():
	if request.args.get('url'):
		if request.args.get('apikey') in keyMe:
			try:
				kekeyi = request.args.get('apikey')
				if keyMe[kekeyi]['limit'] < 1:return {'creator':'Tobz','status': False,'error': 'APIKEY LU DAH MAX HARI INI'}
				a = keyMe[kekeyi]['limit'] -1
				wkwk = arere(kekeyi, a)
				keyMe.update({kekeyi: {'limit': wkwk[0], 'from': wkwk[1], 'exp': wkwk[2], 'status': wkwk[3]}})
				query = request.args.get('url')
				link = requests.get("https://screenshotapi.net/api/v1/screenshot?url={}&output=image".format(query))
				data = ''.join(random.choice(abc) for _ in range(20)) + '.jpg'
				open('result/%s' % data, 'wb').write(link.content)
				return {
					'creator': 'Tobz',
					'status': 200,
					'result': {
						'result': 'https://tobz-api.herokuapp.com/result/%s' % data
					}
				}
			except Exception as e:print(e);return {'status': False,'error': 'Website %s Tidak di temukan!' % unquote(query)}
		else:return {'creator': 'Tobz','status': False,'message': 'APIKEY LU INVALID TOD'}
	else:return {'status': False,'msg': 'input parameter q'}

@app.route('/api/githubprofile', methods=['GET','POST'])
def gprofile():
	if request.args.get('username'):
		if request.args.get('apikey') in keyMe:
			try:
				kekeyi = request.args.get('apikey')
				if keyMe[kekeyi]['limit'] < 1:return {'creator':'Tobz','status': False,'error': 'APIKEY LU DAH MAX HARI INI'}
				a = keyMe[kekeyi]['limit'] -1
				wkwk = arere(kekeyi, a)
				keyMe.update({kekeyi: {'limit': wkwk[0], 'from': wkwk[1], 'exp': wkwk[2], 'status': wkwk[3]}})
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
			except Exception as e:print(e);return {'status': False,'error': '[❗] Username salah!!'}
		else:return {'creator': 'Tobz','status': False,'message': 'APIKEY LU INVALID TOD'}
	else:return {'status': False,'msg': '[!] Masukkan parameter username'}

@app.route('/api/stalk', methods=['GET','POST'])
def stalk():
	if request.args.get('username'):
		if request.args.get('apikey') in keyMe:
			try:
				kekeyi = request.args.get('apikey')
				if keyMe[kekeyi]['limit'] < 1:return {'creator':'Tobz','status': False,'error': 'APIKEY LU DAH MAX HARI INI'}
				a = keyMe[kekeyi]['limit'] -1
				wkwk = arere(kekeyi, a)
				keyMe.update({kekeyi: {'limit': wkwk[0], 'from': wkwk[1], 'exp': wkwk[2], 'status': wkwk[3]}})
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
			except Exception as e:print(e);return {'status': False,'error': '[❗] Username salah!!'}
		else:return {'creator': 'Tobz','status': False,'message': 'APIKEY LU INVALID TOD'}
	else:return {'status': False,'msg': '[!] Masukkan parameter username'}

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
	else:
		return {
			'creator': 'Tobz',
			'status': False,
			'message': 'APIKEY LU INVALID TOD'
		}

@app.route('/api/waifu', methods=['GET','POST'])
def waifu():
	if request.args.get('apikey') in keyMe:
		kekeyi = request.args.get('apikey')
		if keyMe[kekeyi]['limit'] < 1:return {'creator':'Tobz','status': False,'error': 'APIKEY LU DAH MAX HARI INI'}
		a = keyMe[kekeyi]['limit'] -1
		wkwk = arere(kekeyi, a)
		keyMe.update({kekeyi: {'limit': wkwk[0], 'from': wkwk[1], 'exp': wkwk[2], 'status': wkwk[3]}})
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
	else:
		return {
			'creator': 'Tobz',
			'status': False,
			'message': 'APIKEY LU INVALID TOD'
		}

@app.route('/api/infogempa', methods=['GET','POST'])
def infogempa():
	if request.args.get('apikey') in keyMe:
		kekeyi = request.args.get('apikey')
		if keyMe[kekeyi]['limit'] < 1:return {'creator':'Tobz','status': False,'error': 'APIKEY LU DAH MAX HARI INI'}
		a = keyMe[kekeyi]['limit'] -1
		wkwk = arere(kekeyi, a)
		keyMe.update({kekeyi: {'limit': wkwk[0], 'from': wkwk[1], 'exp': wkwk[2], 'status': wkwk[3]}})
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
	else:
		return {
			'creator': 'Tobz',
			'status': False,
			'message': 'APIKEY LU INVALID TOD'
		}

@app.route('/api/randomquotes', methods=['GET','POST'])
def quotes():
	if request.args.get('apikey') in keyMe:
		kekeyi = request.args.get('apikey')
		if keyMe[kekeyi]['limit'] < 1:return {'creator':'Tobz','status': False,'error': 'APIKEY LU DAH MAX HARI INI'}
		a = keyMe[kekeyi]['limit'] -1
		wkwk = arere(kekeyi, a)
		keyMe.update({kekeyi: {'limit': wkwk[0], 'from': wkwk[1], 'exp': wkwk[2], 'status': wkwk[3]}})
		quotes_file = json.loads(open('quotes.json').read())
		result = random.choice(quotes_file)
		print(result)
		return {
			'status': 200,
			'author': result['author'],
			'quotes': result['quotes']
		}
	else:
		return {
			'creator': 'Tobz',
			'status': False,
			'message': 'APIKEY LU INVALID TOD'
		}

@app.route('/api/randomfmylife', methods=['GET','POST'])
def fml():
	if request.args.get('apikey') in keyMe:
		kekeyi = request.args.get('apikey')
		if keyMe[kekeyi]['limit'] < 1:return {'creator':'Tobz','status': False,'error': 'APIKEY LU DAH MAX HARI INI'}
		a = keyMe[kekeyi]['limit'] -1
		wkwk = arere(kekeyi, a)
		keyMe.update({kekeyi: {'limit': wkwk[0], 'from': wkwk[1], 'exp': wkwk[2], 'status': wkwk[3]}})
		url = requests.get("https://www.fmylife.com/random/spicy")
		tbz = BeautifulSoup(url.content, 'html.parser')
		res = tbz.find('span', class_='spicy-hidden').text
		return {
			'creator': 'Tobz',
			'status': 200,
			'result': res
		}
	else:
		return {
			'creator': 'Tobz',
			'status': False,
			'message': 'APIKEY LU INVALID TOD'
		}

@app.route('/api/quotesnime/random', methods=['GET','POST'])
def quotesnimerandom():
	if request.args.get('apikey') in keyMe:
		kekeyi = request.args.get('apikey')
		if keyMe[kekeyi]['limit'] < 1:return {'creator':'Tobz','status': False,'error': 'APIKEY LU DAH MAX HARI INI'}
		a = keyMe[kekeyi]['limit'] -1
		wkwk = arere(kekeyi, a)
		keyMe.update({kekeyi: {'limit': wkwk[0], 'from': wkwk[1], 'exp': wkwk[2], 'status': wkwk[3]}})
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
	else:
		return {
			'creator': 'Tobz',
			'status': False,
			'message': 'APIKEY LU INVALID TOD'
		}

@app.errorhandler(RequestURITooLarge)
def cuihh(e):
	"""Return JSON instead of HTML for HTTP errors."""
	# start with the correct headers and status code from the error
	response = e.get_response()
	# replace the body with JSON
	response.data = json.dumps({
		"code": e.code,
		"name": e.name,
		"description": e.description,
	})
	response.content_type = "application/json"
	return response
@app.route('/', methods=['GET','POST'])

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
