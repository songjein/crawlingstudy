from bs4 import BeautifulSoup
from urllib.request import *
from urllib.parse import *
from os import makedirs
import os.path, time, re

proc_files = {}

def enum_links(html, base):
	soup = BeautifulSoup(html, "html.parser")
	links = soup.select("link[rel='stylesheet']") # css
	links += soup.select("a[href]") # links
	result = []
	# extract and change relative addr to absolute
	for a in links:
		href = a.attrs['href']
		url = urljoin(base, href)
		result.append(url)
	return result

def download_file(url):
	o = urlparse(url)
	savepath = "./" + o.netloc + o.path
	if re.search(r"/$", savepath):
		savepath += "index.html"
	savedir = os.path.dirname(savepath)
	if os.path.exists(savepath): return savepath
	# create download folder
	if not os.path.exists(savedir):
		print("mkdir=", savedir)
		makedirs(savedir)
	# download file
	try:
		print("download=", url)
		urlretrieve(url, savepath)
		time.sleep(1) # 1 sec 
		return savepath
	except:
		print("fail to download", url)
		return None

def analyze_html(url, root_url):
	savepath = download_file(url)
	if savepath is None: return
	if savepath in proc_files: return
	proc_files[savepath] = True
	print("analyze_html=", url)
	# extract links
	html = open(savepath, "r", encoding="utf-8").read()
	links = enum_links(html, url)

	for link_url in links:
		# if link point out another root path
		if link_url.find(root_url) != 0:
			if not re.search(r".css$", link_url): continue
		# if html
		if re.search(r".(html|htm)$", link_url):
			# recursively analyze html file
			analyze_html(link_url, root_url)
			continue
		# etc.
		download_file(link_url)
	
if __name__ == "__main__":
	url = "https://docs.python.org/3.5/library/"
	analyze_html(url, url)
