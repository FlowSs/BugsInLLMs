def _reset_logging(cls):
	"""
	Reset the logging system
	"""
	logging.basicConfig(level=logging.DEBUG)
	
	for handler in logging.root.handlers[:]:
		logging.root.removeHandler(handler)
	logging.disable(logging.CRITICAL)

class _Fetcher(object):
	"""
	A class that is used to retrieve and process a list of URLs.
	"""
	def __init__(self, start_url):
		self.start_url = start_url
		self.url_list = self._create_url_list()
		
	def _create_url_list(self):
		"""
		Create a list of URL's that will be retrieved
		"""
		return [url.strip() for url in open(self.start_url, 'r').readlines()]

	def _fetch_url(self, url):
		"""
		Fetch the requested URL
		"""
		return requests.get(url, allow_redirects=False)

	def _process_url(self, url):
		"""
		Process the requested URL
		"""
		if url.startswith('http://'):
			return self._fetch_url(url)
		elif url.startswith('https://'):
			return self._fetch_url(url[5:])
		else:
			raise ValueError('URL is not a valid URL')

	def _process_urls(self):
		"""
		Process all the URLs in the list
		"""
		for url in self.url_list:
			yield self._process_url(url)

	def __iter__(self):
		"""
		Iterate over the fetched URL's
		"""
		for url in self.url_list:
			yield self._process_url(url)

class _Crawler(object):
	"""
	A class that is used to process the URLs and do the crawling.
	"""
	def __init__(self, start_url, fetch_url, process_urls):
		self.start_url = start_url
		self.fetch_url = fetch_url
		self.process_urls = process_urls
		self.crawl_url_list = self._create_crawl_url_list()

	def _create_crawl_url_list(self):
		"""
		Create a list of URLs that will be crawled
		"""
		return [url.strip() for url in open(self.start_url, 'r').readlines()]

	def _process_crawl_url(self, url):
		"""
		Process the requested URL
		"""
		if url.startswith('http://'):
			return self._fetch_url(url)
		elif url.startswith('https://'):
			return self._fetch_url(url[5:])
		else:
			raise ValueError('URL is not a valid URL')

	def _process_crawl_urls(self):
		"""
		Process all the URLs in the list
		"""
		for url in self.crawl_url_list:
			yield self._process_crawl_url(url)

	def __iter__(self):
		"""
		Iterate over the crawled URLs
		"""
		for url in self.crawl_url_list:
			yield self._process_crawl_url(url)

	def crawl(self):
		"""
		Crawl the URLs from the start URL
		"""
		for url in self.start_url.split(','):
			for next_url in self.process_urls():
				yield next_url

class Crawler(object):
	"""
	A class that is used to process the URLs and do the crawling.
	"""
	def __init__(self, start_url, fetch_url, process_urls, crawl_url_list):
		self.start_url = start_url
		self.fetch_url = fetch_url
		self.process_urls = process_urls
		self.crawl_url_list = crawl_url_list
		self.crawl_crawler = _Crawler(start_url, fetch_url, process_urls)

	def _process_