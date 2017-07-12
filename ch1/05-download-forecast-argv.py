#!/usr/bin/env python3
import sys
import urllib.request as req
import urllib.parse as parse

# extract command params
if len(sys.argv) <= 1:
	print("Usage: download forecast argv <Region Number>: ")
	sys.exit()
regionNumber = sys.argv[1] # [0]-> script name [1]~ -> params

# encode params 
API = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp"
values = {
	'stnId': regionNumber
}
params = parse.urlencode(values) # for korean, it is necessary
url = API + "?" + params
print("url: ", url)

# download
data = req.urlopen(url).read()
text = data.decode('utf-8')
print(text)

"""
	[using shebang (first line), we can execute this script like linux command without python3] 
	-> chmod 766 thisfilename
	-> ./thisfilename 108
"""
