# -*- coding: utf-8 -*-
import sys
import requests
from lxml import html
class Challenge:
	def do_request(self,url) :
		response = requests.get(url)
		return html.fromstring(response.text)		
	def get_url_from_command_line(self) :
 		url = ""
        	for param in sys.argv[1:2] :
                	url = param
        	return url

