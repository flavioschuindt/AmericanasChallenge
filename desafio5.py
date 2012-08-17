# -*- coding: utf-8 -*-
#!/usr/bin/python
import sys; sys.path.append('modules')
from Challenge import *

challenge = Challenge()
url = "http://hughes.sieve.com.br:9090/level3/"
cookie = {'cade-meu-cookie':'esta aqui'}
data = challenge.do_request(url,None,cookie)['response']
results = data.xpath("//p/text()")
print "Preço: "+str(challenge.get_float_price(results[0]))