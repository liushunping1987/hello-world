import urllib.request


def get_html(url):
    page = urllib.request.urlopen(url)
    