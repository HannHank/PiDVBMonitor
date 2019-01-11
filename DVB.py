#!/usr/bin/env python
# coding=utf-8
from flask import Flask, render_template
import datetime
import requests
import json
app = Flask(__name__)
@app.route("/DVB/<Ort>/<station>/")
def index(Ort,station): 
       url = "http://widgets.vvo-online.de/abfahrtsmonitor/Abfahrten.do?ort={0}&hst={1}".format(Ort,station)
       response = requests.get(url)
       HTL = json.loads(response.content)  
       linie = HTL[0]
       linie2 = HTL[1]
       linie3 = HTL[2]
       linie4 = HTL[3]
                                         
       return render_template('index.html',linie = linie,linie2 = linie2,linie3 = linie3,linie4 = linie4)

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=80, debug=True)
