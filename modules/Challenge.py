# -*- coding: utf-8 -*-
import sys
import requests
from lxml import html
class Challenge:
	def do_request(self,url) :
		response = requests.get(url)
		status_and_response = {}
		if (len(response.history) > 0):
			#Moved to home or departament page
			status_and_response = dict(status_code=response.history[0].status_code,response=html.fromstring(response.text))
		else:
			status_and_response = dict(status_code=response.status_code,response=html.fromstring(response.text))
		return status_and_response
	def get_url_from_command_line(self) :
 		url = ""
        	for param in sys.argv[1:2] :
       			url = param
		return url
