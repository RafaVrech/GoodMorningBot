import requests
import pandas as pd
import numpy as np
import datetime as dt
from pandas_datareader import data as pdr

def backtest():
    pair = input("Enter a pair symbol: ")

    finalDate = dt.datetime.now()
    initialDate = finalDate - pd.DateOffset(months=1)

    URL = "https://fxmarketapi.com/apipandas"
    params = {'currency' : pair,
    'start_date' : initialDate.strftime("%Y-%m-%d"),
    'end_date': finalDate.strftime("%Y-%m-%d"),
    'api_key':'tpLtcSkwFVK_JUbJbYlT',
    'interval':'hourly',
    'format':'ohlc'
    }

    response = requests.get("https://fxmarketapi.com/apipandas", params=params)
    df= pd.read_json(response.text)
    
    for i in df.index:
        time = dt.datetime.strptime(str(i), '%Y-%m-%d %H:%M:%S')
        
        if(str(time.hour) == '6'):
            high = 0
            low = 0
            high = df.iloc[:,2][i]
            low = df.iloc[:,3][i]
        elif(str(time.hour) == '7'):
            if(float(high) < float(df.iloc[:,2][i])):
                high = df.iloc[:,2][i]
            if(float(low) > float(df.iloc[:,3][i])):
                low = df.iloc[:,3][i]
                
            print('High: ' + str(high))
            print('Low: ' + str(low))
            print('Datetime: ' + str(time.day) + '-' + str(time.month))

        

backtest()