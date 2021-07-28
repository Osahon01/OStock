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
print("Welcome to the OStock-bot! \n Menu overview: \n 1. Current stock price!! \n 2. Should I sell? \n 3. Should I buy? \n 4. Top stock gainers :) \n 5. Top stock losses :( ")
 
print(" \n 1. Current stock price!! \n Please input the symbol for the stock you are inquiring about:")

def get_current_price(symbol):
    ticker = y_fin.Ticker(symbol)
    todays_data = ticker.history(period = '20mins')
    
    print(" \n Here is the current stock price for the company you were inquiring about:", "$", ticker.info["currentPrice"])
    print("\n")
    
    
    print("2. Should I sell? [run/skip]: ")
    response = input()
    if response=="run":
        print("Please type in the symbol of the company: ")  
        symbol2 = input()
        
        print("Please type the price you paid for the stock; express it as an integer value")         
        b_price = input()
        c_price = y_fin.Ticker(symbol2).info()
        g_l=(float(c_price) - float(b_price))
        
        if float(c_price) < float(b_price):
             print("\nOStock-bot advises you to either closely monitor this stock or consider buying the dip. You have lost {} dollars so far.".format(g_l))
        else:
             print("\nOStock-bot advises you to sell to secure a profit, or allow the stock to continue to grow. You have gained {} dollars so far.".format(g_l))            
    elif response=='skip':
        print()



    print(" \n Should I buy? [run/skip]: ")
    response = input()
    if response=="run":
        print("Please type in the symbol of the company: ")  
        symbol3 = input()
        
        b_price = input()
        c_price = y_fin.Ticker(symbol3).info[]
        if float(c_price) < float(b_price):
             print("OStock-bot advises you to either closely monitor this stock or consider buying the dip")
        else:
             print("OStock-bot advises you to sell to secure a profit, or allow the stock to continue to grow")            
    elif response=='skip':
        print()

    '''
    if input('Should I sell?'):
         symbol = input()
         test2 = get_current_price(symbol)
         print(test2)
         print("Please type the price you paid for the stock; express it as an integer value")         
         test1 = input("Price: ")
         print(test1, test2)
         print("testing...")
         if int(test1) > int(test2):
         else:
    '''             
    '''          
    if input('Should I buy?'):
         print("Please type in the symbol for the stock you are inquiring about")
         blue=(input())
         ticker2 = y_fin.Ticker(blue)

         print('ticker2.info')
    '''
    '''
       #  print(blue)
         if blue.loc[:,"% Change"] > 10:
            print("OStock-bot advises you to invest in this stock")
         else:
           print("OStock-bot advises you to not invest in this stock")        
    '''
    '''
    print("Want more! \n Check out what's going on in the stock market today! \n Please press 'enter' to skip a command, or press any letter to run a command")
    print("Commands: \n Current winnings \n Current losses \n Should I sell? \n Should I buy?")
    
    
    print("\n 4. Top stock gainers :)")
    win=stock_info.get_day_gainers()
    w_vals=win.loc[:,"% Change"]
    w_name=win.loc[:,"Symbol"]
    if input("Current winnings"):
        print("Over the past 20 minutes, ", w_name[0], "has received the most stock gains of", w_vals[0], "%")
    
    print("\n 5. Top stock losses :(")
    if input("Current losses"):
        loss=stock_info.get_day_losers()
        l_vals=loss.loc[:,"% Change"]
        l_name=loss.loc[:,"Symbol"]
        print("Over the past 20 minutes, ", l_name[0], "has received the most stock losses of", l_vals[0], "%")
 #   else: 
 #       print("Must type in all lowercase for the command to be read properly.")
     ''' 

#    return todays_data['Close'][0]

get_current_price(input())
