from bs4 import BeautifulSoup as bs
from requests import get
import os

class Scraper:

  DEFAULT_HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) "
        "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36"
    )
  }

  def __init__(self, url=None, parser=None, headers=None, www=False, ssl=False, domain=''):  #nopep8
    self.domain = "" if not domain else domain.replace(".", "")
    self.www = '' if not www else 'www.'
    self.ssl = "http://" if not ssl else "https://"
    self.url = None if not url else f'{self.ssl}{self.www}{url}{self.domain}' #nopep8
    self.parser = parser if parser else 'lxml'
    self.headers = headers if headers else self.DEFAULT_HEADERS
    self.status = get(self.url, headers=self.headers).status_code
    self.results = None
    self.images = None


  def lprint(self, prop=None):

    if prop and hasattr(self, prop):
      for i in getattr(self, prop, None):
        try:
          print(i)
        except TypeError:
          continue

    else:
      if self.results:
        for i in self.results:  # nopep8
          print(i)

    return self

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

  def download_images(self, file_path=None, sub_folder=None, msg=True):

    if self.images:
      folder = os.path.join(file_path, sub_folder) if sub_folder != None else file_path

      if not os.path.exists(folder):
          os.makedirs(folder)

      for img in self.images:
        img_name = img.split("/")[-1]

        if msg:
          print("DOWNLOADING: ", img_name)

        with open(f'{os.getcwd()}/{folder}/{img_name}', 'wb') as f:
          response = get(img, headers=self.headers)

          if not response.status_code == 200: #OK
            continue

          f.write(response.content)
    elif self.results:
      self.set_images().download_images(file_path, sub_folder)

  def each(self, func, prop=None):

    if prop and hasattr(self, prop):
      for i in getattr(self, prop, None):
        func(i)

    else:
      for i in self.results:
        func(i)


  def set_url(self, url):
    self.url = url

  def set_text(self):
    if self.results:
      self.text = map(lambda x: x.text, self.results)

      return self


  def set_links(self):
     if self.results:
      self.links = map(lambda x: x.a["href"], self.results)

      return self

  def set_images(self):
    if self.results:
      self.images = map(lambda x: x.img["src"], self.results)

      return self
