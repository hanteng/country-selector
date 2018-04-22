# -*- coding: utf-8 -*-
#歧視無邊，回頭是岸。鍵起鍵落，情真情幻。
from string import Template
import os.path, os, glob
import shutil
import codecs

import requests
import json
locale_select = requests.get("https://raw.githubusercontent.com/unicode-cldr/cldr-core/master/availableLocales.json").json()['availableLocales']['modern']

# Partial Selected Construction
#locale_select = ['en-GB','my', 'zh-Hant'] # Can be extended in the future  'zh-Hant-HK', 'zh-Hant-MO', 'zh-Hans', 'zh-Hans-SG'

## Outpuing Lists

path_data = u'../data'
path_demo = u'../demo'

directory = path_demo
if not os.path.exists(directory):
    os.makedirs(directory)

######## MSG for future locale translation ############
MSG=dict()
MSG['Country Selector']     ="Country Selector: Unicode CLDR resource application"
MSG['Country Selector_Q']   ="Select a country"
MSG['Country Selector_Q_AJAX']="Select a country (using AJAX)"

                   #COUNTRY_SEL, COUNTRY_SEL_Q, COUNTRY_SEL_Q_AJAX, PLACEHOLDER, DATALIST
output_DEMO_HTML=\
'''<!DOCTYPE html>  
<html>  
  <head>
  <meta charset="UTF-8">
    <title>COUNTRY_SEL</title>
    <style>
		body{
			font-size:18px;
		}
	    #default{
			font-size:18px;
		}
		input[name="browsers"] {
		  border: 2px solid orange;
		  border-radius: 10px 10px 10px 10px;
		  font-size: 18px;
		  padding: 5px;
		  height: 35px;
		  width: 350px;
		}
		input::-webkit-calendar-picker-indicator {
		/*   display: none; */
		}
    </style>
  </head>
  <body>
    <div id="page-wrapper">
      <label for="default">$COUNTRY_SEL_Q</label>
      <input type="text" id="default" list="countries" placeholder="$PLACEHOLDER"> 
      $DATALIST
    </div>
  </body>
</html>  
'''
########################################################


for l in locale_select:
    inputfn_HTML = os.path.join(path_data, l, "territories_snippet.htm")
    outputfn_HTML = os.path.join(path_demo, "{lang}.htm".format(lang=l))

    with codecs.open(inputfn_HTML, "r", "utf-8") as file:
        snippet = file.read()

    output=Template(output_DEMO_HTML).safe_substitute(COUNTRY_SEL = MSG['Country Selector'] , \
                                                      COUNTRY_SEL_Q = l, \
                                                      PLACEHOLDER = "e.g. CN", \
                                                      DATALIST = snippet)    

    with codecs.open(outputfn_HTML, "w", "utf-8") as file:
        file.write(output)











