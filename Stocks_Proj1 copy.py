
"""
Created on Tue Jul 27 00:23:43 2021

@author: osahon
"""
import yfinance as y_fin
import datetime
from datetime import date

from yahoo_fin import stock_info
import turtle


window = turtle.Screen()
window.bgcolor('black')
logo = turtle.Turtle()
logo.color("grey")
font_i = ('SF Pro', 80, 'bold')
logo.write("OStock-bot", font=font_i, align='center')


stock = y_fin.Ticker("ABEV3.SA")
data = stock.info
startDate = datetime.datetime(2021, 7, 1)
today = date.today()
print("Welcome to the OStock-bot! \n Menu overview: \n 1. Current stock price!! \n 2. Should I sell? \n 3. Should I invest in __ company? \n 4. Top stock gainers :) \n 5. Top stock losses :( ")
 
print(" \n 1. Current stock price!!\nPlease input the symbol for the stock you are inquiring about:")

def get_current_price(symbol):
    ticker = y_fin.Ticker(symbol)
    
    print(" \n Here is the current stock price for the company you were inquiring about:", "$", ticker.info["currentPrice"])
    print("\n")
    
    
    print(" 2. Should I sell? [run/skip]: ")
    response = input()
    if response=="run":
        print(" \nPlease type in the symbol of the company: ")  
        symbol2 = input()
        
        print(" \nPlease type in the price you paid for the stock; express it as an integer value")         
        b_price = input()
        c_price = y_fin.Ticker(symbol2).info['currentPrice']
        g_l=(float(c_price) - float(b_price))
        
        if float(c_price) < float(b_price):
             print(" \nOStock-bot advises you to either closely monitor this stock or consider buying the dip. You have lost {} dollars so far.".format(g_l))
        else:
             print(" \nOStock-bot advises you to sell to secure a profit, or allow the stock to continue to grow. You have gained {} dollars so far.".format(g_l))            
    elif response=='skip':
        print()



    print(" \n 3. Should I invest? [run/skip]: ")
    response = input()
    if response=="run":
        print(" \nPlease type in the symbol of the company: ")  
        symbol3 = input()
        #print(y_fin.Ticker(symbol3).info)
        q_change = y_fin.Ticker(symbol3).info['revenueGrowth']
        per_change = (q_change*100)
        if float(per_change) < 50:
             print("OStock-bot does not advise buying this stock at the moment. Its current revenue growth rate is {}%".format(per_change))
        else:
             print("OStock-bot advises you to invest to secure a profit before it's too late. Its current revenue growth rate is {}%".format(per_change))            
    elif response=='skip':
        print()


    print(" \n 4. Top stock gainers :) [run/skip]")
    response=input()
    if response=="run":
        win=stock_info.get_day_gainers()
        w_vals=win.loc[:,"% Change"]
        w_name=win.loc[:,"Symbol"]
        print("\nCurrent winnings")
        print(" \nOver the past 20 minutes, ", w_name[0], "has received the most stock gains of", w_vals[0], "%")
    elif response=='skip':
        print()
    
    
    print("\n 5. Top stock losses :( [run/skip]")
    response=input()
    if response=="run":
        print("\nCurrent losses")
        loss=stock_info.get_day_losers()
        l_vals=loss.loc[:,"% Change"]
        l_name=loss.loc[:,"Symbol"]
        print(" \nOver the past 20 minutes, ", l_name[0], "has received the most stock losses of", l_vals[0], "%")
    elif response=='skip':
        print() 
    #   else: 
 #       print("Must type in all lowercase for the command to be read properly.")

#    return todays_data['Close'][0]
    print("\n \n    You'll make a lot of gains using OStock-bot!")

get_current_price(input())
