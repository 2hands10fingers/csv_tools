from bs4 import BeautifulSoup as bs
from requests import get, post, Session
import os
from datetime import datetime

class Scraper:
  def __init__(self, url=None, parser=None, headers=None, www=False, ssl=False, domain=''):  #nopep8
    self.domain = "" if not domain else domain.replace(".", "")
    self.www = '' if not www else 'www.'
    self.ssl = "http://" if not ssl else "https://"
    self.url = None if not url else f'{self.ssl}{self.www}{url}{self.domain}' #nopep8
    self.parser = parser if parser else 'lxml'
    self.headers = headers if headers else self.default_headers()
    self.status = get(self.url, self.headers).status_code
    self.results = None

  
  def lprint(self, prop=None):

    if prop and hasattr(self, f"get_{prop}"):
      for i in getattr(self, f"get_{prop}")():
        try:
          print(i)
        except TypeError:
          continue


    else:
      if self.results:
        for i in self.results:  # nopep8
          print(i)

    return self

  def default_headers(self):
      ua_one = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) '
      ua_two = 'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
      headers = {'User-Agent': ua_one + ua_two}

      return headers

  def scrape(self, element=None, attr=None, attr_name=None, style="", msg=True):
    
    if msg:
      print(f'SCRAPING {self.url}\n')
    
    if isinstance(attr, str) and attr_name == None or isinstance(attr_name, str) and attr == None:
       raise SystemExit('\nMake sure attr and attr_name are set.')

    def styled_request(style):
      request = get(self.url, headers=self.headers)
      if style == "json":
        return request.json()
      elif style == "content":
       return request.content
      
      return request.text

    soup = bs(styled_request(style), self.parser)
    self.results = soup.find_all(element, { attr : attr_name })
    return self

  def download_images(self, file_path, sub_folder=None):
    
    if self.images:
      folder = os.path.join(file_path, sub_folder) if sub_folder != None else file_path
      
      if not os.path.exists(folder):
          os.makedirs(folder)
      
      for img in self.images:
        img_name = img.split("/")[-1]
        print("DOWNLOADING: ", img_name)
        
        with open(f'{os.getcwd()}/{folder}/{img_name}', 'wb') as f:
          response = get(img, headers=self.headers)

          if not response.status_code == 200: #OK
            continue

          f.write(response.content) 

  def get(self, prop=None):
    if prop and hasattr(self, prop):
      print(getattr(self, prop))
      
  def get_links(self):
    if self.links:
      return list(self.links)

  def get_results(self):
    if self.results:
      return self.results
  
  def get_images(self):
    if not self.images:
      return self.images
       
  def set_links(self):
     if self.results != None:
      self.links = map(lambda x: x.a["href"], self.results)
      
      return self

  def set_images(self):
    if self.results != None:
      self.images = map(lambda x: x.img["src"], self.results)
      
      return self
