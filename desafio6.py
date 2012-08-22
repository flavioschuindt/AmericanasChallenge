# -*- coding: utf-8 -*-
#!/usr/bin/python
import sys; sys.path.append('modules')
from Challenge import *

challenge = Challenge()
url = "http://hughes.sieve.com.br:9090/level5/"
location = challenge.quote_url(challenge.do_request(url,None,None)['history'][0].headers['location'])
data = challenge.do_request(location,None,None)['response']
results = data.xpath("//p/text()")
print "Preço: "+str(challenge.get_float_price(results[0]))