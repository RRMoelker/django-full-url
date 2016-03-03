django-full-url
===================

Getting specific parts of an URL for the current page in Django can be quite tedious. This small package makes it easy to get parts of the URL by providing python helpers and a context processor. All the information is gathered from a RequestContext object, no error prone 'Site' config needed!

Some of the URL parts you can extract:

* domain
* http or https
* port
* path
* query (get parameters)

There are some situations where you might want to get specific URL parts:

* Add the domain name for including images on your domain in an email.
* Get the full URL (protocol, domain, path and query) for sharing the page on social networks.
* Get a link to same page using 'http' or 'https'.

## Installation

Either install directly:

`pip install -e git+https://github.com/RRMoelker/django-full-url.git#egg=django-full-url`

Or add the following line to your requirements file:

`-e git+https://github.com/RRMoelker/django-full-url.git#egg=django_full_url`


## Usage

There are currently two ways to get the URL information. One method uses a context processor to make the different URL parts data available in all [templates](#context-processor). The second method provides helpers to get the information directly from within a view or another place where you have access to a RequestObject in the [python code](#python-code). For available parameters see [RequestGrabber](#grabber)

### <a href="context-processor"></a>Context processor

You can add a context processor that will add the variable `url_parts` to all templates.
The processor can be added anywhere in the `TEMPLATE_CONTEXT_PROCESSORS` list:

```
TEMPLATE_CONTEXT_PROCESSORS = (
  # ...
  'full_url.context_processors.UrlParts',
  # ...
)
```

The `url_parts` variable is a [RequestGrabber](#grabber) object. To actually insert part of the url into the template you can do:
```
...
{{url_parts.domain}}
...
```


### <a href="#python-code"></a>Python code

To get URL information in python use the [RequestGrabber](#grabber).
```
from full_url.grabber import RequestGrabber
```

Create an instance of the RequestGrabber object using:

```
url_parts = RequestGrabber(request)
```

To get a part use: `url_parts.domain()`. See [RequestGrabber](#grabber) for available URL parts.


## <a name="grabber"></a>RequestGrabber

Say we are looking at the following view: `http://localhost:8000/news/2014/?sort=ascending#item2`

The RequestGrabber has the following functions available:

* protocol: http://
* domain: localhost:8000
* port: 8000
* path: /news/2014/
* query: sort=ascending
* full_url: /news/2014/?sort=ascending
* absolute_uri: http://localhost:8000/news/2014/?sort=ascending

Note that we cannot get the fragment part of the URL (#item2).
During normal operations a browser should never send this information so no functionality to get it is provided at this time.

## Requirements
Django
(Tested with Django 1.6 and 1.7. Please let me know if it works in other versions setups)

## Uninstall
Nothing fancy here:

```
pip uninstall django-full-url
```

Encountered a bug or missing a feature? Please create a ticket to help improve this tool!
