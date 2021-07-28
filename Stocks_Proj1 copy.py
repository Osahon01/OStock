#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 27 00:23:43 2021

@author: osahon
"""
import yfinance as y_fin
import datetime
from datetime import date

from yahoo_fin import stock_info

stock = y_fin.Ticker("ABEV3.SA")
data = stock.info
startDate = datetime.datetime(2021, 7, 1)
today = date.today()
 
def get_current_price(symbol):
    ticker = y_fin.Ticker(symbol)
    todays_data = ticker.history(period = '20mins')
    print("Welcome to the OStock-bot!")
    print("\n")
    print("Before we get to the stock you are asking about, check out what's going on in the stock market today! \n Please press 'enter' to skip a command, or press any letter to run a command")
    print("Commands: \n Current winnings \n Current losses \n Should I sell? \n Should I buy?")
    win=stock_info.get_day_gainers()
    w_vals=win.loc[:,"% Change"]
    w_name=win.loc[:,"Symbol"]
    if input("Current winnings"):
        print(get_current_price('tsla'))
        print("Over the past 20 minutes, ", w_name[0], "has received the most stock gains of", w_vals[0], "%")
    
    if input("Current losses"):
        loss=stock_info.get_day_losers()
        l_vals=loss.loc[:,"% Change"]
        l_name=loss.loc[:,"Symbol"]
        print("Over the past 20 minutes, ", l_name[0], "has received the most stock losses of", l_vals[0], "%")
 #   else: 
 #       print("Must type in all lowercase for the command to be read properly.")
    
    if input('Should I sell?'):
         print("Please type in the symbol of the company")        
         symbol = input()
         test2 = get_current_price(symbol)
         print(test2)
         print("Please type the price you paid for the stock; express it as an integer value")         
         test1 = input("Price: ")
         print(test1, test2)
         print("testing...")
         
         if int(test1) > int(test2):
             print("OStock-bot advises you not to sell")
         else:
             print("OStock-bot advises you to either sell or closely monitor this stock")
             
            
    if input('Should I buy?'):
         print("Please type in the symbol for the stock you are inquiring about")
         blue=(input())
         print(blue)
         if blue.loc[:,"% Change"] > 0:
            print("OStock-bot advises you to invest in this stock")
         else:
           print("OStock-bot advises you to not invest in this stock")        
 
    return todays_data['Close'][0]


print("Please input the symbol for the stock you are inquiring about:")
print(" \n Here is the current stock price for the company you were inquiring about:", get_current_price(input()))
