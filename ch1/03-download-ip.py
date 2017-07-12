import urllib.request

# read data from http://, ftp://
url = "http://api.aoikujira.com/ip/ini"
res = urllib.request.urlopen(url)
data = res.read()

# decode binary to string
text = data.decode("utf-8")
print(text)

