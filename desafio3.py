# -*- coding: utf-8 -*-
#!/usr/bin/python
import sys; sys.path.append('modules')
from Challenge import *

challenge = Challenge()
url = "http://hughes.sieve.com.br:9090/level2/"
cookie = dict(d53db4de415c4e858dc761595623a898='+')
data = challenge.do_request(url,None,cookie)['response']
results = data.xpath("//div/text()")
print "Preço: "+str(challenge.get_float_price(results[0]))