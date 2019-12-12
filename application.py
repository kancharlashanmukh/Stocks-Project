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

DATABASE_URL =  'postgres://noxthjmjrdzasn:76ff1ab5fd7f09c73f6fe82ee4a7a2b5fa8920f75f3ef32679a1186ea743f359@ec2-107-21-122-38.compute-1.amazonaws.com:5432/defdshlvvo279k'
conn = psycopg2.connect(DATABASE_URL, sslmode='require')

print("Connection established")
cursor = conn.cursor()
cursor1 = conn.cursor()
cursor2 = conn.cursor()
cursor3 = conn.cursor()
@app.route("/")
def hello():
   return render_template('index.html')

@app.route('/check',methods = ['POST'])
def check():
    
    try:

        cmp1 = request.form['cmp1']
        cmp2 = request.form['cmp2']
        print(cmp1+" "+cmp2)

        data=requests.get('https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol='+cmp1+'&outputsize=compact&apikey=X81QUECTPQC802ES')
        data=data.json()
        dat=(data['Time Series (Daily)'])
        keys = (dat.keys())
        cursor.execute("select csymbol from stock where csymbol like '"+cmp1+"' fetch first row only")
        rows=cursor.fetchone()
        print(rows)
            
        if rows is None:
            for k in keys:
                open1=dat[k]['1. open']
                high= dat[k]['2. high']
                low=dat[k]['3. low']
                close=dat[k]['4. close']      
                cursor.execute("INSERT INTO public.stock(open, close, high, low, cname, csymbol, date) VALUES (%s, %s,%s, %s,%s, %s,%s);", (open1,close,high,low,cmp1,cmp1,k))
                print("inserted")
                conn.commit()   
                    
        else:
            for k in keys:
                open1=dat[k]['1. open']
                high= dat[k]['2. high']
                low=dat[k]['3. low']
                close=dat[k]['4. close']
                sql=("UPDATE public.stock SET open="+open1+", high="+high+",close="+close+", low="+low+" WHERE date='"+k+"' and csymbol='"+cmp1+"';")
                print(sql)        
                cursor.execute(sql)
                print("row updated")
                break
        cursor.execute("select * from stock where csymbol like '"+cmp1+"' fetch first row only")
        rows=cursor.fetchone()
        print(str(rows[4]))
        cursor1.execute("select open,close,to_char(date,'YYYY-MM-DD') from stock where csymbol like '"+cmp1+"' order by date desc limit 22")
        chartrows=cursor1.fetchall()
        openlist=[]
        closelist=[]
        datelist=[]
        for chr in chartrows:
            openlist.append(chr[0])
            closelist.append(chr[1])
            datelist.append(chr[2])
    
        
        conn.commit()
        data1=requests.get('https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol='+cmp2+'&outputsize=compact&apikey=X81QUECTPQC802ES')
        data1=data1.json()
        dat1=(data1['Time Series (Daily)'])
        
        keys1 = (dat1.keys())
        print(keys1)
        cursor3.execute("select csymbol from stock where csymbol like '"+cmp2+"' fetch first row only")
        rows1=cursor3.fetchone()
        
            
        if rows1 is None:
            for k1 in keys1:
                open1=dat1[k1]['1. open']
                high= dat1[k1]['2. high']
                low=dat1[k1]['3. low']
                close=dat1[k1]['4. close']      
                cursor.execute("INSERT INTO public.stock(open, close, high, low, cname, csymbol, date) VALUES (%s, %s,%s, %s,%s, %s,%s);", (open1,close,high,low,cmp2,cmp2,k1))
                print("inserted")
                conn.commit()   
                    
        else:
            for k1 in keys1:
                copen1=dat1[k1]['1. open']
                chigh= dat1[k1]['2. high']
                clow=dat1[k1]['3. low']
                cclose=dat1[k1]['4. close']
                sql=("UPDATE public.stock SET open="+copen1+", high="+chigh+",close="+cclose+", low="+clow+" WHERE date='"+k1+"' and csymbol='"+cmp2+"';")
                print(sql)        
                cursor.execute(sql)
                print("row updated")
                break
        cursor.execute("select * from stock where csymbol like '"+cmp2+"' fetch first row only")
        rows1=cursor.fetchone()
        
        cursor2.execute("select open,close,to_char(date,'YYYY-MM-DD') from stock where csymbol like '"+cmp2+"' order by date desc limit 22")
        chartrows1=cursor2.fetchall()
        copenlist=[]
        ccloselist=[]
        cdatelist=[]
        for chr1 in chartrows1:
            copenlist.append(chr1[0])
            ccloselist.append(chr1[1])
            cdatelist.append(chr1[2])

        conn.commit()
        boo=1
        return render_template("index.html",boo=boo,open=str(rows[0]),close=str(rows[1]),high=str(rows[2]),low=str(rows[3]),cname=str(rows[4]),csymbol=str(rows[5]),openlist=openlist,closelist=closelist,open1=str(rows1[0]),close1=str(rows1[1]),high1=str(rows1[2]),low1=str(rows1[3]),cname1=str(rows1[4]),csymbol1=str(rows1[5]),copenlist=copenlist,ccloselist=ccloselist)
    except IOError:
        return print("Please contatct admin")


if __name__ == '__main__':
    app.run()