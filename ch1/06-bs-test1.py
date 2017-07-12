from bs4 import BeautifulSoup

html = """
<html>
	<body>
		<h1>Scraping?</h1>
		<p>analyze web page</p>
		<p>extract information</p>
	</body>
</html>
"""

soup = BeautifulSoup(html, 'html.parser')


h1 = soup.html.body.h1
p1 = soup.html.body.p
p2 = p1.next_sibling.next_sibling # first next_sibling -> space or nextline

print("h1: ", h1.string)
print("p: ", p1.string)
print("p: ", p2.string)
