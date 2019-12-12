from flask import Flask,render_template, request
import requests
import json
import psycopg2
app = Flask(__name__)

# host = "myserverkyc.postgres.database.azure.com"
# dbname = "kyc"
# user = "kycadmin@myserverkyc"
# password = "Shan12345"
# sslmode = "require"

# # Construct connection string
# conn_string = "host={0} user={1} dbname={2} password={3} sslmode={4}".format(host, user, dbname, password, sslmode)
# conn = psycopg2.connect(conn_string) 
# print("Connection established")
# cursor = conn.cursor()
@app.route("/")
def hello():
   return render_template('home.html')

@app.route("/check",methods = ['POST'])
def check():
   cmp1 = request.form['cmp']
   print(cmp1) 
   return render_template('home.html',cmp1=cmp1)
# @app.route('/check',methods = ['POST'])
# def check():
#     cmp1 = request.form['cmp']
#     data=requests.get('https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol='+cmp1+'&outputsize=compact&apikey=X81QUECTPQC802ES')
#     data=data.json()

#     dat=(data['Time Series (Daily)'])
#     keys = (dat.keys())
#     cursor.execute("select csymbol from stock where csymbol like '"+cmp1+"' fetch first row only")
#     rows=cursor.fetchone()
#     print(rows)
        
#     if rows is None:
#         for k in keys:
#             print(k+" "+ dat[k]['2. high'] + " " + dat[k]['5. volume'])
#             ss=str(k)
#             print(ss)
#             open1=dat[k]['1. open']
#             high= dat[k]['2. high']
#             low=dat[k]['3. low']
#             close=dat[k]['4. close']      
#             cursor.execute("INSERT INTO public.stock(open, close, high, low, cname, csymbol, date) VALUES (%s, %s,%s, %s,%s, %s,%s);", (open1,close,high,low,"Apple",cmp1,k))
#             print("inserted")
#             conn.commit()   
                
#     else:
#         for k in keys:
#             print(k+" "+ dat[k]['2. high'] + " " + dat[k]['5. volume'])
#             open1=dat[k]['1. open']
#             high= dat[k]['2. high']
#             low=dat[k]['3. low']
#             close=dat[k]['4. close']
#             sql=("UPDATE public.stock SET open="+open1+", high="+high+",close="+close+", low="+low+" WHERE date='"+k+"' and csymbol='"+cmp1+"';")
#             print(sql)        
#             cursor.execute(sql)
#             print("row updated")
#             break
#     cursor.execute("select * from stock where csymbol like 'AAPL' fetch first row only")
#     rows=cursor.fetchone()
#     print(rows)
#     # print("open-------"+str(rows[0]))
#     # print("high-------"+str(rows[0]))
#     # print("low-------"+str(rows[0]))
#     # print("close-------"+str(rows[0]))
   
#     conn.commit()
    
#     msg="hello"
#     return render_template("index.html",msg = msg, open=str(rows[0]),high=str(rows[1]),low=str(rows[2]),close=str(rows[3]))



# if __name__ == '__main__':
#     app.run()