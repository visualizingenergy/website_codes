#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 11:06:14 2023

@author: hcliffo
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
from monday import MondayClient

def wordpress_png_code_output(viz_link):
    page = requests.get(viz_link)


    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find("title")
    title = results.prettify()
    viz_title = title.split(' ')[1]

    viz_number = viz_link.split('/')[4]
    viz_type = viz_link.split('/')[3]


    spacer_10 = '''
<!-- wp:spacer {"height":"10px"} -->
<div style="height:10px" aria-hidden="true" class="wp-block-spacer"></div>
<!-- /wp:spacer -->
'''

    embed_viz = '''
<!-- wp:html -->
<div class="flourish-embed" data-src="{viz_type}/{viz_number}"><script src="https://public.flourish.studio/resources/embed.js"></script></div>
<!-- /wp:html -->
'''.format(**locals())

       
    align_data = '''
<!-- wp:columns {"verticalAlignment":"center","UAGHideMob":true,"UAGHideTab":true,"UAGResponsiveConditions":true} -->
<div class="wp-block-columns are-vertically-aligned-center uag-hide-tab uag-hide-mob"><!-- wp:column {"verticalAlignment":"center","width":"12%"} -->
<div class="wp-block-column is-vertically-aligned-center" style="flex-basis:12%"><!-- wp:paragraph {"align":"center"} -->
'''

    data_link = '''
    
<p class="has-text-align-center"><a href="https://visualizingenergy.org/wp-content/uploads/{viz_title}.csv" data-type="attachment" data-id="2512">Data</a></p>
<!-- /wp:paragraph --></div>
<!-- /wp:column -->
'''.format(**locals())



    align_meta = '''
<!-- wp:column {"verticalAlignment":"center","width":"12%"} -->
<div class="wp-block-column is-vertically-aligned-center" style="flex-basis:12%"><!-- wp:paragraph {"align":"center"} -->
'''

    meta_link = '''
<p class="has-text-align-center"><a href="https://visualizingenergy.org/wp-content/uploads/{viz_title}_meta.txt" data-type="attachment" data-id="2512" target="_blank">Metadata</a></p>
<!-- /wp:paragraph --></div>
<!-- /wp:column -->
'''.format(**locals())

    align_media = '''
<!-- wp:column {"verticalAlignment":"center","width":"12%"} -->
<div class="wp-block-column is-vertically-aligned-center" style="flex-basis:12%"><!-- wp:paragraph {"align":"center"} -->
'''

    media_link='''
<p class="has-text-align-center"><a href="https://visualizingenergy.org/wp-content/uploads/{viz_title}.png" data-type="attachment" data-id="2562">PNG</a></p>
<!-- /wp:paragraph --></div>
<!-- /wp:column -->
'''.format(**locals())

    align_embed = '''
<!-- wp:column {"verticalAlignment":"center","width":"64%"} -->
<div class="wp-block-column is-vertically-aligned-center" style="flex-basis:64%"><!-- wp:code {"style":{"typography":{"fontSize":"8px"}}} -->
'''

    embed_link = '''
<pre class="wp-block-code" style="font-size:8px"><code>&lt;div class="flourish-embed" data-src="{viz_type}/{viz_number}"&gt;&lt;script src="https://public.flourish.studio/resources/embed.js"&gt;&lt;/script&gt;&lt;/div&gt;</code></pre>
<!-- /wp:code --></div>
<!-- /wp:column --></div>
<!-- /wp:columns -->
'''.format(**locals())

    spacer_20 ='''
<!-- wp:spacer {"height":"20px"} -->
<div style="height:20px" aria-hidden="true" class="wp-block-spacer"></div>
<!-- /wp:spacer -->
'''


    final_code = " ".join([spacer_10,embed_viz,align_data,
                              data_link,align_meta,meta_link,
                              align_media,media_link,align_embed,
                              embed_link,spacer_20])

    return final_code

def wordpress_gif_code_output(viz_link):
    page = requests.get(viz_link)

    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find("title")
    title = results.prettify()
    viz_title = title.split(' ')[1]

    viz_number = viz_link.split('/')[4]
    viz_type = viz_link.split('/')[3]

    spacer_10 = '''
<!-- wp:spacer {"height":"10px"} -->
<div style="height:10px" aria-hidden="true" class="wp-block-spacer"></div>
<!-- /wp:spacer -->
'''

    embed_viz = '''
<!-- wp:html -->
<div class="flourish-embed" data-src="{viz_type}/{viz_number}"><script src="https://public.flourish.studio/resources/embed.js"></script></div>
<!-- /wp:html -->
'''.format(**locals())

    align_data = '''
<!-- wp:columns {"verticalAlignment":"center","UAGHideMob":true,"UAGHideTab":true,"UAGResponsiveConditions":true} -->
<div class="wp-block-columns are-vertically-aligned-center uag-hide-tab uag-hide-mob"><!-- wp:column {"verticalAlignment":"center","width":"12%"} -->
<div class="wp-block-column is-vertically-aligned-center" style="flex-basis:12%"><!-- wp:paragraph {"align":"center"} -->
'''

    data_link = '''
    
<p class="has-text-align-center"><a href="https://visualizingenergy.org/wp-content/uploads/{viz_title}.csv" data-type="attachment" data-id="2512">Data</a></p>
<!-- /wp:paragraph --></div>
<!-- /wp:column -->
'''.format(**locals())



    align_meta = '''
<!-- wp:column {"verticalAlignment":"center","width":"12%"} -->
<div class="wp-block-column is-vertically-aligned-center" style="flex-basis:12%"><!-- wp:paragraph {"align":"center"} -->
'''

    meta_link = '''
<p class="has-text-align-center"><a href="https://visualizingenergy.org/wp-content/uploads/{viz_title}_meta.txt" data-type="attachment" data-id="2512" target="_blank">Metadata</a></p>
<!-- /wp:paragraph --></div>
<!-- /wp:column -->
'''.format(**locals())

    align_media = '''
<!-- wp:column {"verticalAlignment":"center","width":"12%"} -->
<div class="wp-block-column is-vertically-aligned-center" style="flex-basis:12%"><!-- wp:paragraph {"align":"center"} -->
'''

    media_link='''
<p class="has-text-align-center"><a href="https://visualizingenergy.org/wp-content/uploads/{viz_title}.gif" data-type="attachment" data-id="2562">GIF</a></p>
<!-- /wp:paragraph --></div>
<!-- /wp:column -->
    '''.format(**locals())

    align_embed = '''
<!-- wp:column {"verticalAlignment":"center","width":"64%"} -->
<div class="wp-block-column is-vertically-aligned-center" style="flex-basis:64%"><!-- wp:code {"style":{"typography":{"fontSize":"8px"}}} -->
    '''

    embed_link = '''
<pre class="wp-block-code" style="font-size:8px"><code>&lt;div class="flourish-embed" data-src="{viz_type}/{viz_number}"&gt;&lt;script src="https://public.flourish.studio/resources/embed.js"&gt;&lt;/script&gt;&lt;/div&gt;</code></pre>
<!-- /wp:code --></div>
<!-- /wp:column --></div>
<!-- /wp:columns -->
    '''.format(**locals())

    spacer_20 ='''
<!-- wp:spacer {"height":"20px"} -->
<div style="height:20px" aria-hidden="true" class="wp-block-spacer"></div>
<!-- /wp:spacer -->
'''


    final_code = " ".join([spacer_10,embed_viz,align_data,
                              data_link,align_meta,meta_link,
                              align_media,media_link,align_embed,
                              embed_link,spacer_20])

    return final_code

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

def extract_article_overview():

    monday = MondayClient('eyJhbGciOiJIUzI1NiJ9.eyJ0aWQiOjIwMjg0NzE0NSwidWlkIjozMDk0NDE5OCwiaWFkIjoiMjAyMi0xMi0wMVQwNzoxODoxOS43ODBaIiwicGVyIjoibWU6d3JpdGUiLCJhY3RpZCI6MTIyMTY1NDMsInJnbiI6InVzZTEifQ.Xk83t2dR3L01D679_WxfsVixFeXJJiCTKbRxY2dIIk0')
    cols = monday.boards.fetch_columns_by_board_id([3268084825])
    columns = [i['title'] for i in cols['data']['boards'][0]['columns']][1:]

    items = monday.boards.fetch_items_by_board_id(3268084825)

    name = []

    ds = pd.DataFrame()

    for n,i in enumerate(items.get('data').get('boards')[0]['items']):

        name = i['name']
        info = pd.DataFrame(items.get('data').get('boards')[0]['items'][n]['column_values'])
        info['value'] = columns
        info = info.set_index('value')
        info = info['text']
        ds[name] = info

    ds = ds.T
    ds = ds.reset_index()
    ds = ds.rename(columns = {'index':'Name'})
    ds = ds[['Name','Title','Visualizations','Article Text','Status','VE Link']]
    
    
    doc_id_append = []
    for i in ds['Article Text']:

        try:
            di = i.split('/')[5]
            doc_id_append.append(di)
        except:
            doc_id_append.append('')
            
    ds['doc id'] = doc_id_append
    
    
    return ds

def get_viz_embeds(articles):
    df = extract_visualizations()
    
    wp_emb = {}
    
    for a in articles:
    
        df_ds = df[df['Article Overview']==a]
        
        for n,row in df_ds.iterrows():
        
            if (row['User Resources'] == 'Not Used') | (row['User Resources'] == 'In Story'):
                pass
            else:
                media_types = row['User Resources Completed'].split(', ')
                viz_link = row['Link']
    
                if 'GIF' in media_types:
                    code_output = wordpress_gif_code_output(viz_link)
                    wp_emb[row['Name']] = code_output
                elif 'PNG' in media_types:
                    code_output = wordpress_png_code_output(viz_link)
                    wp_emb[row['Name']] = code_output
    return wp_emb


def replace_format(i,formatted):
    
    format_dict = {
        'i':'em',
        'sup':'sup',
        'b':'strong',
        'sub':'sub',
        }
    
    f_wp = format_dict[formatted]
    
    fm_f = '('+formatted+')'
    fm_b = '(/'+formatted+')'
    
    if i.find(fm_f) != -1:
        num_ref = i.count(fm_f)
        while num_ref > 0:
            num_ref = num_ref-1
            it_text = i[i.find(fm_f)+3:i.find(fm_b)]
            f_pos = i.find(fm_f)
            b_pos = i.find(fm_b)+len(fm_b)-1
            i = i[:f_pos] + '<'+f_wp+'>' + it_text + '</'+f_wp+'>' + i[b_pos+ + 1:]
    return i


def return_strings_for_wp():
    ref_before = '''
<!-- wp:paragraph {"style":{"typography":{"fontSize":"15px","lineHeight":1.5}}} -->
<p style="font-size:15px;line-height:1.5">'''
    
    
    quote_before = '''
<!-- wp:columns -->
<div class="wp-block-columns"><!-- wp:column {"width":"5px"} -->
<div class="wp-block-column" style="flex-basis:5px"><!-- wp:spacer -->
<div style="height:100px" aria-hidden="true" class="wp-block-spacer"></div>
<!-- /wp:spacer --></div>
<!-- /wp:column -->

<!-- wp:column {"width":"90%"} -->
<div class="wp-block-column" style="flex-basis:90%"><!-- wp:paragraph -->
<p>'''

    quote_after = '''</p>
<!-- /wp:paragraph --></div>
<!-- /wp:column -->

<!-- wp:column {"width":"5px"} -->
<div class="wp-block-column" style="flex-basis:5px"></div>
<!-- /wp:column --></div>
<!-- /wp:columns -->'''
        
    top_wp = '''
<!-- wp:paragraph -->
<p>'''
        
    bottom_wp = '''</p>
<!-- /wp:paragraph -->
        
    '''
    
    spacer_20 ='''<!-- wp:spacer {"height":"20px"} -->
<div style="height:20px" aria-hidden="true" class="wp-block-spacer"></div>
<!-- /wp:spacer -->'''
    
    spacer_10 ='''<!-- wp:spacer {"height":"10px"} -->
<div style="height:10px" aria-hidden="true" class="wp-block-spacer"></div>
<!-- /wp:spacer -->'''


    list_before_first='''<!-- wp:list -->
<ul><!-- wp:list-item -->
<li>'''

    list_before = '''<!-- wp:list-item -->
<li>'''
    
    list_after = '''</li>
<!-- /wp:list-item -->'''
    
    list_after_last ='''</ul>
<!-- /wp:list -->'''

    return ref_before,quote_after,quote_before, top_wp, bottom_wp, \
            spacer_20, spacer_10,list_before,list_after,list_before_first,list_after_last


def check_for_reference(i,ds_name):
    
    cit_before = '<sup><a href="#{}-ref">'.format(ds_name)
    cit_after = '</a></sup>'
    
    len_before = len(i)
    
    if i.find('[') != -1:

        in_brackets = False

        add_len = None

        for pos, char in enumerate(i):
            if add_len:
                pos = pos+add_len
            if char == "[":
                in_brackets = True
            elif char == "]" and in_brackets:
                in_brackets = False
            elif in_brackets:
                i = i[:pos] + cit_before + char + cit_after + i[pos + 1:]
                len_after = len(i)
                add_len = (len_after-len_before)
                in_brackets = False
                
    i = re.sub(r"[\[\]]", "", i)
    return i

def check_ve_links(i,ds_info):            

    if i.find('{') != -1:
        
        num_ref = i.count('{')

        while num_ref > 0:

            start = i.index('{')
            end = i.index('}')
            
            substring = i[start+1:end]

            s_split = substring.split('^')
            text = s_split[0]

            link = ds_info.loc[ds_info['Name']==s_split[1],'VE Link'].values[0]
            add_link ='''<a href="{link}" data-type="URL" data-id="{link}" target="_blank" rel="noreferrer noopener">{text}</a>'''.format(text = text,link=link)
            i = i.replace('{'+substring+'}',add_link)
            num_ref = num_ref-1
    return i



def check_other_links(i):            

    if i.find('(l)') != -1:
        
        num_ref = i.count('(l)')

        while num_ref > 0:

            start = i.index('(l)')
            end = i.index('(/l)')
            
            substring = i[start+3:end]
            s_split = substring.split('^')

            text = s_split[0]
            link = s_split[1]
            add_link ='''<a href="{link}" data-type="URL" data-id="{link}" target="_blank" rel="noreferrer noopener">{text}</a>'''.format(text = text,link=link)

            i = i.replace('(l)'+substring+'(/l)',add_link)

            num_ref = num_ref-1
    return i



