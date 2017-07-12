import urllib.request
import urllib.parse

"""
	stnId : location number
	seoul/gyeonggi : 109
"""
API = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp"

# encode params
values = {
	'stnId': '108'
}
params = urllib.parse.urlencode(values)

# create request url
url = API + "?" + params
print("url: ", url)

# download
data = urllib.request.urlopen(url).read()
text = data.decode('utf-8')
print(text)
