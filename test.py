# from flask import Flask,render_template, request
# import json
# import psycopg2
# import requests
# app = Flask(__name__)
# conn = psycopg2.connect(database="postgres", user = "postgres", password = "password", host = "127.0.0.1", port = "5432")
# print("Connection established")
# cursor = conn.cursor()
# cmp1="MSFT"
# data=requests.get('https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol='+cmp1+'&outputsize=compact&apikey=X81QUECTPQC802ES')
# data=data.json()

# dat=(data['Time Series (Daily)'])
# keys = (dat.keys())
# cursor.execute("select csymbol from stock where csymbol like 'MSFT' fetch first row only")
# rows=cursor.fetchone()
# print(rows)
    
# if rows is None:
#     for k in keys:
#         print(k+" "+ dat[k]['2. high'] + " " + dat[k]['5. volume'])
#         ss=str(k)
#         print(ss)
#         open1=dat[k]['1. open']
#         high= dat[k]['2. high']
#         low=dat[k]['3. low']
#         close=dat[k]['4. close']      
#         cursor.execute("INSERT INTO public.stock(open, high, date, cname, close, low, csymbol) VALUES (%s, %s,%s, %s,%s, %s,%s);", (open1,high,k,"Microsoft",close,low,"MSFT"))
#         print("inserted")   
            
# else:
#     for k in keys:
#         print(k+" "+ dat[k]['2. high'] + " " + dat[k]['5. volume'])
#         open1=dat[k]['1. open']
#         high= dat[k]['2. high']
#         low=dat[k]['3. low']
#         close=dat[k]['4. close']        
#         cursor.execute("UPDATE public.stock SET open="+open1+", high="+high+",close="+close+", low="+low+" WHERE date='"+k+"' and csymbol='MSFT';")
#         print("row updated")
#         break
# conn.commit()
# cursor.close()
# conn.close()




  
