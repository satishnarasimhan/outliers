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

column_names = ["CONTRACT_D","PREVIOUS_S","OPEN_PRICE","HIGH_PRICE","LOW_PRICE","CLOSE_PRIC","SETTLEMENT","NET_CHANGE","OI_NO_CON", "TRADED_QUA", "TRD_NO_CON", "UNDRLNG_ST", "NOTIONAL_V", "PREMIUM_TR", "SECURITY", "CEPE", "TEMP", "SERIES", "STRIKE", "OPT_CONTRACT", "DATE"]

sourcePath = 'C:\\Users\\Nithya\\Documents\\Python\\Projects\\Outliers\\Raw Files\\' 
#Historical: \\Apr-2021\\ .. Raw Files\\
fileName = 'op'+date+'.csv'
csvfile = (sourcePath+fileName) 

df = pd.DataFrame(columns = column_names)
df = pd.read_csv(csvfile)

# PE - ITM Selling
pe_res = df.query("CEPE=='PE' & (STRIKE > UNDRLNG_ST) & OI_NO_CON > 0 & TRD_NO_CON > 0 & HIGH_PRICE < (STRIKE - UNDRLNG_ST) & (SETTLEMENT > 0)")

# Processed file path
pe_res.to_csv(r'C:\\Users\\Nithya\\Documents\\Python\\Projects\\Outliers\\Processed Files\\PE-ITM'+'_'+date+'.csv')
print("PE file generated successfully")

# CE -ITM Selling
ce_res = df.query("CEPE=='CE' & (STRIKE < UNDRLNG_ST) & OI_NO_CON > 0 & TRD_NO_CON > 0 & HIGH_PRICE < (UNDRLNG_ST - STRIKE) & (SETTLEMENT > 0)")

ce_res.to_csv(r'C:\\Users\\Nithya\\Documents\\Python\\Projects\\Outliers\\Processed Files\\CE-ITM'+'_'+date+'.csv')
print("CE file generated successfully")