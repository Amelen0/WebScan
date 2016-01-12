import urllib request
import io

def get_robots_txt(url):
    if url.endswith('/'):
       path = url
    else:
       path = url + ('/')
    req = urlib.request.oprn.urlopen.

