import requests
from bs4  import BeautifulSoup

_url_shsubway = "http://service.shmetro.com/axlcz{0}/index.htm"
_lines = ["01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","41"]

class Lines(object):
	def __init__(self,line):
		self.line = line

	def get_data_from_line():
		r = requests.get(_url.shsubway.format(self.line))
		try:
			soup = BeautifulSoup(r.content)
		except Exception as e:
