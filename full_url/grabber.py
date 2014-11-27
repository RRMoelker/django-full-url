# -*- coding: utf-8 -*-

def get_scheme(request):
	"""
	Get scheme used in request
	e.g.: 'http://' or 'https://'
	"""
	if request.is_secure():
		return "https://"
	else:
		return "http://"

def get_protocol(request):
	"""
	Get protocol used in request
	e.g.: 'http://' or 'https://'
	"""
	return get_scheme(request)

def get_domain(request):
	"""
	Get domain part of URL
	e.g.: 'example.com', 'www.example.com', 'localhost:8000'
	"""
	return request.get_host()

def get_host(request):
	"""
	Get host part of URL
	e.g.: 'example.com', 'www.example.com', 'localhost:8000'
	"""
	return get_domain()

def get_port(request):
	try:
		return request.META['SERVER_PORT']
	except KeyError:
		return None

def get_path(request):
	"""
	Get path part of URL
	e.g.: '/news/2014/01/02/some-item/', '/'
	"""
	return request.path

def get_query(request):
	"""
	Get query part of URL
	e.g.: 'var1=test&var2=324'
	"""
	try:
		return request.META['QUERY_STRING']
	except KeyError:
		return None

def get_full_url(request):
	"""
	Get whole URL without domain and protocol
	e.g.: '/someview/?query="test"'
	"""
	return request.get_full_path()

def get_absolute_uri(request):
	"""
	Get full URL with domain and protocol
	e.g.: 'http://example.com/someview/?query="test"'
	"""
	return request.build_absolute_uri()


class RequestGrabber():
	"""
	Wrapper around URL parts grabber functions. This class only requires the request to be passed once.
	"""
	def __init__(self, request):
		self.request = request

	def scheme(self):
		return get_scheme(self.request)

	def protocol(self):
		return get_protocol(self.request)

	def domain(self):
		return get_domain(self.request)

	def host(self):
		return get_host(self.request)

	def port(self):
		return get_port(self.request)

	def path(self):
		return get_path(self.request)

	def query(self):
		return get_query(self.request)

	def full_url(self):
		return get_full_url(self.request)

	def absolute_uri(self):
		return get_absolute_uri(self.request)