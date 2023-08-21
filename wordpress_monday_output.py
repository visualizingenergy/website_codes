#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 11:04:18 2023

@author: hcliffo
"""
from functions import *
from httplib2 import Http
from opengoogledoc import *
import re
from pydrive.drive import GoogleDrive
from pydrive.auth import GoogleAuth
import os
import sys


ds_input = input('Input data story for wordpress:')
wp_emb = get_viz_embeds([ds_input])
credentials =  get_credentials()
http = credentials.authorize(Http())


article_overview = extract_article_overview()

ds_info=article_overview.copy()

data_stories = article_overview[article_overview['Name'].isin([ds_input])]


ref_before,quote_after,quote_before, top_wp, bottom_wp, \
    spacer_20, spacer_10,list_before,list_after, \
    list_before_first,list_after_last = return_strings_for_wp()

for n,row in data_stories.iterrows():
    print(row['Name'])
    doc_id = row['doc id']
    doc_content = get_doc_content(doc_id,http)
    text = read_structural_elements(doc_content)
    sections = text.split('\n')
    ds_name = row['Name'].lower()
    
    separator = '''
<!-- wp:separator -->
<hr class="wp-block-separator has-alpha-channel-opacity" id="{}-ref"/>
<!-- /wp:separator -->
'''.format(ds_name)

    doc_string = ''
    
    is_ref = False
    list_count = 0
    for i in sections:   
        
        # visualization embed
        if i.startswith('<<'):
            i = i.replace('<', '')
            i = i.replace('>', '')
            i = i.strip()
            doc_string = doc_string + wp_emb[i]   
            
        #references
        elif i.startswith('['):
            if not is_ref:
                doc_string = doc_string + spacer_20 + separator + spacer_10    
                is_ref=True
            i = re.sub(r"[\[\]]", "", i)
            doc_string = doc_string + ref_before + i + bottom_wp
            
        # quotes
        elif i.startswith('(q)'):
            i = quote_before + i[3:] + quote_after
            i = check_for_reference(i,ds_name)
            doc_string = doc_string + i
            
        # bullet points
        
        elif i.startswith('(list)'):
            
            if list_count == 0:
                i = list_before_first + i[6:] + list_after
                i = check_for_reference(i,ds_name)
                doc_string = doc_string + spacer_10 + i
                list_count = list_count+1
            else:
                i = list_before + i[6:] + list_after
                i = check_for_reference(i,ds_name)
                doc_string = doc_string + i
                
        elif i.startswith('(endlist)'):
            doc_string = doc_string + list_after_last + spacer_20

        elif len(i) > 1:
            
            # check for ve data story links in section
            i = check_ve_links(i,ds_info)
            
            # check for other links in section
            i = check_other_links(i)
                    
            # find references in text
            i = check_for_reference(i,ds_name)
                        
            # find format in text
            for check_format in ['i','b','sup','sub']:
                i = replace_format(i,check_format)
      
            i = top_wp + i + bottom_wp
            doc_string = doc_string + i
            
    isExist = os.path.exists('WordpressText')
    
    if not isExist:
        os.makedirs('WordpressText')
        
    text_file = open("WordpressText/{}.txt".format(row['Name']), "w")
    text_file.write(doc_string)
    text_file.close()
    gauth = GoogleAuth()
    gauth.LocalWebserverAuth()       
    drive = GoogleDrive(gauth)
    file1 = drive.CreateFile({'parents': [{'id': '1uG48Kd8fmUyfyPecIqyhPloNnes93haT'}],'title': "{}.txt".format(row['Name'])})  
    file1.SetContentString(doc_string) 
    file1.Upload(param={'supportsTeamDrives': True})
           