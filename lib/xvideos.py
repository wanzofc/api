from bs4 import BeautifulSoup
import requests,json

search = "handjob"
r = requests.get("https://mnazria.herokuapp.com/api/porn?search={}".format(search))
raflyRTB = r.text
raflyRTB = json.loads(raflyRTB)
anu = raflyRTB["result"]
result = {"creator":"Rafly","result": anu}
print(json.dumps(result,indent=4,ensure_ascii=False))