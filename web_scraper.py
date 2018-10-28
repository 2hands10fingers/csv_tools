from bs4 import BeautifulSoup as bs
from requests import get

class Scraper:
	def __init__(self, url, parser=None, headers=None):
		self.url = url
		self.parser = parser if parser else 'lxml'
		self.headers = headers if headers else self.default_headers()
		self.status = get(self.url).status_code


	def default_headers(self):
	    ua_one = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) '
	    ua_two = 'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
	    headers = {'User-Agent': ua_one + ua_two}
	    
	    return headers


	def get_piece(self, element=None, attribute=None, attribute_name=None, operation=None):
		
		print("SCRAPING...") if self.status == 200 else print(f"RESPONSE resulted in a {self.status} status code.")
			
		soup = bs(get(self.url, headers=self.headers).text, self.parser)
		result = soup.find_all(element, { attribute : attribute_name })
		
		return operation(result) if operation != None else result
