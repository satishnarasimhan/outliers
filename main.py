# -*- coding: utf-8 -*-
"""
Created on Thu May 20 16:21:46 2021

@author: Satish Narasimhan
This script will generate the list of securities / instruments which have ITM selling
"""
from datetime import datetime
import pandas as pd

# Determine current date
day = datetime.now()
date = day.strftime("%d%m%y")

#date = '170621'
print(date)

column_names = []

sourcePath = 'C:\\Users\\Path\\To\\Raw\\Files' 
#Historical: \\Apr-2021\\ .. Raw Files\\
fileName = 'op'+date+'.csv'
csvfile = (sourcePath+fileName) 

df = pd.DataFrame(columns = column_names)
df = pd.read_csv(csvfile)

# PE - ITM Selling
pe_res = df.query("")

# Processed file path
pe_res.to_csv(r'')
print("PE file generated successfully")

# CE -ITM Selling
ce_res = df.query("")

ce_res.to_csv(r'')
print("CE file generated successfully")