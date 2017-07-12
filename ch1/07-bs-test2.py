from bs4 import BeautifulSoup

html = """
<html>
	<body>
		<h1 id="title">Scraping?</h1>
		<p id="body">analyze web page</p>
		<p>extract information</p>
	</body>
</html>
"""

soup = BeautifulSoup(html, 'html.parser')

title = soup.find(id="title")
body = soup.find(id="body")

print("#title: ", title.string)
print("#body: ", body.string)
