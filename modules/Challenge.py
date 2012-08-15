# -*- coding: utf-8 -*-
import sys
import requests
from lxml import html
class Challenge:
	def do_request(self,url) :
		response = requests.get(url)
		if ( (len(response.history) > 0) and (response.history[0].status_code == 301)):
			#Moved to home
			print u'This product doesn\'t exist. Impossible to get price!'
		return html.fromstring(response.text)
	def get_url_from_command_line(self) :
 		url = ""
        	for param in sys.argv[1:2] :
       			url = param
		return url
