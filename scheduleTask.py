import requests
import json
from requests.api import request
import schedule
import requests
def get_row(request) :
    print("this is wrong project")



def get_tabel_2(request):
    url ='http://127.0.0.1:8000/get'
    body = ''
    h = {'Content-Type':'application/json'}
    res = requests.get( url , header=h )
    print(res.text)

info=views.inforApi()
schedule.every(1).seconds.do(inforApi(request.method=='GET'))
schedule.every(1).seconds.do(get_row(request.method=='GET'))
while True:
    schedule.run_pending()
