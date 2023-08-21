#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  4 09:33:34 2023

@author: hcliffo
"""

import gspread as gs
import pandas as pd
from datetime import date


gc = gs.service_account(filename='VE_key.json')

sh = gc.open_by_url('https://docs.google.com/spreadsheets/d/1as3ZNs07NKuT1uX6m_UfPUWLALHp_picGQcklcz_zTA/edit#gid=2126422537')

ws = sh.worksheet('Sheet1')

df = pd.DataFrame(ws.get_all_records())

today = date.today()
df = df.replace([''], [None])

df['Time span'].replace({'nan':'Not Applicable'}, inplace=True)

for n,row in df.iterrows():
    viz_id = row['Visualization ID']
    viz_title = row['Visualization Title']
    time_span = row['Time span']
    print(viz_id)
    
    text = """
================================
Visualizing Energy

visualizingenergy.org

================================

Title: {viz_title}

Time span: {time_span}
    """.format(today=today,viz_title=viz_title,time_span=time_span)
    
    var1 = row[4:10]
    var2 = row[10:16]
    var3 = row[16:22]
    var4 = row[22:28]
    
    list_var = []
    for n,var in enumerate([var1,var2,var3,var4]):
        if not var.isnull().all():
            var.fillna('None', inplace=True)
            var_name = var[0]
            source = var[2]
            source_link = var[3]
            if source_link != 'None':
                source_link = source_link.replace('<br> ','\n\n')
                source_link = source_link.replace('<br>','\n\n')
            var_accessed = var[1]

            if (var_accessed != 'None') & (var_accessed != 'not applicable'):
                var_accessed = pd.to_datetime(var_accessed)
                var_accessed = var_accessed.strftime('%Y-%m-%d')
            else:
                var_accessed = 'not applicable'
                    
            description = var[4]
            if description != 'None':
                description = description.replace('<br> ','\n\n')
                description = description.replace('<br>','\n\n')
                
            links = var[5]
            links = links.replace('<br>','\n\n')
            
            var_info ="""
================================

Variable: 
{var_name}

Source: 
{source}

Source link: 
{source_link}

Data accessed: 
{var_accessed}

Description: 
{description}

Additional links: 
{links}
            """.format(var_name=var_name,
                       source=source,
                       source_link=source_link,
                       var_accessed=var_accessed,
                       description=description,
                       links=links)
           
            text = text + var_info
            
    text_file = open("{viz_id}_meta.txt".format(viz_id=viz_id), "w")
    n = text_file.write(text)
    text_file.close()
    
    