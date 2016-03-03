# -*- coding: utf-8 -*-
from __future__ import absolute_import
from .grabber import RequestGrabber

def UrlParts(request):
	"""
	Adds url part grabber to context
	"""
	return {
		'url_parts': RequestGrabber(request)
	}
