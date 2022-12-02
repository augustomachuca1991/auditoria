import requests
import urllib.parse


API_BASE_URL = "https://apis.datos.gob.ar/georef/api/"

def get_similar(endpoint, nombre, **kwargs):
    kwargs["nombre"] = nombre
    url = "{}{}?{}".format(API_BASE_URL, endpoint, urllib.parse.urlencode(kwargs))
    return requests.get(url).json()[endpoint]

input_provincia = input("Enter Location: " )
provincias = get_similar("provincias", input_provincia)

print(provincias)


#import urllib3
# http = urllib3.PoolManager()
# r = http.request('GET', 'http://httpbin.org/robots.txt')
# print(r.status)