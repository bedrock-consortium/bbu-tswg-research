#!/usr/bin/python3

import json, requests, time, datetime, urllib.parse, urllib.request, qrcode, pymongo, cgi, cgitb
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
  return render_template('hola2.html')

@app.route('/boogs')
def my_link():

    myclient = pymongo.MongoClient("mongodb://192.168.0.18:27017/")
    mydb = myclient["bedrock"]
    fmem = mydb["lifeco"]
    agent_url = 'http://192.168.0.18:8001'
    proof_send_req = '/present-proof/send-request'

    form = cgi.FieldStorage()
    memnum =  form.getvalue('memids')
    print("memnum is", memnum)

    ## aca-py endorser connection
    headers={"x-api-key" : 'booger'}
    conn_url = 'http://192.168.0.18:8001/connections/create-invitation?auto_accept=true'

    conn_meta = {
            #"metadata": {
            #        "memid": {
            #                "idnum": "123456",
            #                "hashnum": "abcdef"

            #            }
            #        },


            "my_label": "Kibbles",
            "service_endpoint": "http://192.168.0.18:8000"
    }

    connreq = requests.post(conn_url, headers = conn_meta)

##  db.createCollection("lifeco")
## db.lifeco.insert({memid:"12345", connid:"123456"})

    xus = fmem.find_one({"memid": memnum})
    print (xus)

    if xus:
        #for m in fmem.find():
        memnumo = ['memid']
        memconno = ['connid']

        print (memnumo, memconno)

        return render_template('qr.html')

    if not xus:

        connresp = connreq.json()

        conn_id = connresp['connection_id']
        inv_url = connresp['invitation_url']
        rec_keys = connresp['invitation']['recipientKeys']

        g = { "memid": memnumo, "connid": conn_id }
        gi = { "memid": memnumo }
        h = { "$set": { "connid": conn_id } }

        #if memnumo in memnum:

        #    fmem.update_one(gi, h)

        #else:

        fmem.insert_one(g)

        img = qrcode.make(inv_url)
        img.save('/var/www/beds/static/imgs/qrcode1.png')

        return render_template('qr.html')

if __name__ == '__main__':
  app.run(debug=True)
