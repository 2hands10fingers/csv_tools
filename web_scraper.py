from bs4 import BeautifulSoup as bs
from requests import get
import re


class Scraper:
	def __init__(self, url, parser=None, headers=None):
		self.url = url
		self.parser = parser if parser else 'lxml'
		self.headers = headers if headers else self.default_headers()
		self.status = get(self.url).status_code
		self.result = None 


	def default_headers(self):
	    ua_one = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) '
	    ua_two = 'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
	    headers = {'User-Agent': ua_one + ua_two}

	    return headers


	def download_all(self, write_bytes=True, parser=None):

		def download(file_name, file_url):
			with open(file_name, 'wb' if write_bytes else 'w') as file:
				print(f'Saving file name: {file_name}')
				file.write(get(file_url).content)


		if isinstance(self, (list, tuple, set)):
			for i in self:
				download(i.split('/')[-1] if not parser else parser(i), i)

	def get_piece(self, element=None, attribute=None, attribute_name=None, 
				  operation=None, download_all=False, parser=None, write_bytes=True):

		soup = bs(get(self.url, headers=self.headers).text, self.parser)
		result = soup.find_all(element, { attribute : attribute_name })
		self.result = operation(result) if operation != None else result

		return Scraper.download_all(self.result, parser=parser, write_bytes=write_bytes) if download_all else self.result

def parsed(soup_result):
	return [i.img["src"] for i in soup_result]
		


print(Scraper('https://podcastmovement.com/past-speakers/', parser='lxml').get_piece(element='div', attribute="class", attribute_name="link-box--img-container", operation=parsed))
