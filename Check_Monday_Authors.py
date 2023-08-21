#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 21 10:14:38 2023

@author: hcliffo
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd
from monday import MondayClient

def extract_visualizations():
    
    monday = MondayClient('eyJhbGciOiJIUzI1NiJ9.eyJ0aWQiOjIwMjg0NzE0NSwidWlkIjozMDk0NDE5OCwiaWFkIjoiMjAyMi0xMi0wMVQwNzoxODoxOS43ODBaIiwicGVyIjoibWU6d3JpdGUiLCJhY3RpZCI6MTIyMTY1NDMsInJnbiI6InVzZTEifQ.Xk83t2dR3L01D679_WxfsVixFeXJJiCTKbRxY2dIIk0')
    cols = monday.boards.fetch_columns_by_board_id([3272211806])
    columns = [i['title'] for i in cols['data']['boards'][0]['columns']][1:]

    items = monday.boards.fetch_items_by_board_id(3272211806)
    ds = {}

    for n,i in enumerate(items.get('data').get('boards')[0]['items']):

        name = i['name']
        info = pd.DataFrame(items.get('data').get('boards')[0]['items'][n]['column_values'])
        info['value'] = columns
        info = info.set_index('value')
        info = info['text']
        ds[name] = info
        
    ds = pd.concat(ds,axis=1)

    ds = ds.T
    ds = ds.reset_index()
    ds = ds.rename(columns = {'index':'Name'})
    ds = ds[['Name','User Resources','User Resources Completed', 'Link','Article Overview','Status']]
    return ds

df = extract_visualizations()

for n,row in df.iterrows():
    if row['User Resources']=='Complete Resources':
        viz_link = row['Link']
        viz = row['Name']
    
        page = requests.get(viz_link)
        
        soup = BeautifulSoup(page.content, "html.parser")
        results = soup.find("h2")
        author = results.prettify()
        viz_author = author.split('\n ')[3][1:]
        if not viz_author == 'visual':
            print(viz)
            print(viz_author)


