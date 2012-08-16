# -*- coding: utf-8 -*-

import unittest
import sys; sys.path.append('../../modules')
from Challenge import *
class UnitTest(unittest.TestCase):
	def test_get_unavailable_product_should_return_empty_price_list(self):
		challenge = Challenge()
		url = '''http://www.americanas.com.br/produto/6991162/utilidadesdomesticas/aparelhodejantar/20pecas/para4pessoas/conjunto-de-jantar-ipanema-c/-20-pecas-porto-fino'''
		data = challenge.do_request(url)['response']
		results = data.xpath("//span[@class='amount']/text()")
		unavailable = data.xpath("//div[@class='unavailProd']/text()")
		self.assertTrue(len(unavailable) > 0 and len(results) == 0)
	def test_get_unavailable_product_with_related_products_should_return_empty_price_list(self):
        	challenge = Challenge()
        	url = '''http://www.americanas.com.br/produto/6991162/utilidadesdomesticas/aparelhodejantar/20pecas/para4pessoas/conjunto-de-jantar-ipanema-c/-20-pecas-porto-fino'''
        	data = challenge.do_request(url)['response']
		results = data.xpath("//span[@class='amount']/text()")
        	unavailable = data.xpath("//div[@class='unavailProd']/text()")
        	self.assertTrue(len(unavailable) > 0 and len(results) == 0)
	def test_get_available_product_should_return_price(self):
		challenge = Challenge()
		url = '''http://www.americanas.com.br/produto/110595674/informatica/notebooks/notebooks/notebook-gateway-nv55c12b-com-intel-core-i3-2gb-320gb-led-156-windows-7-home-basic'''
		data = challenge.do_request(url)['response']
		results = data.xpath("//span[@class='amount']/text()")
		unavailable = data.xpath("//div[@class='unavailProd']/text()")
		self.assertTrue(len(unavailable) == 0 and len(results) > 0)
	def test_get_inexistent_product_should_return_301_in_status_code(self):
		challenge = Challenge()
		url = '''http://www.americanas.com.br/produto/7262040/chromalin-(120-caps)-+-brinde-ripped-extreme-yellow-caps-(20-caps'''
		data = challenge.do_request(url)['status_code']
		self.assertTrue(data == 301)

unittest.main()
