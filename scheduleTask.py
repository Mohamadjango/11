import requests
import json
from requests.api import request
import schedule
import requests
from



def get_tabel_2(request):
    url ='http://127.0.0.1:8000/get'
    body = ''
    h = {'Content-Type':'application/json'}
    res = requests.get( url , header=h )
    print(res.text)
#     listo = []
#     connect_sqlite = sqlite3.connect('resturant.sqlite3')
#     channel = connect_sqlite.cursor()
#     q_list = channel.execute('''select ingredients from ReqApis_quantities where total_quantity<1000''')
#     print('q_list=', q_list)
#     for row in q_list :
#         listo.append(row)
#         return json.dumps(listo)
info=views.inforApi()
schedule.every(1).seconds.do(inforApi(request.method=='GET'))
#
while True:
    schedule.run_pending()