from bs4 import BeautifulSoup
soup = BeautifulSoup(
	"<p><a href='a.html'>test</a></p>",
	"html.parser")

print (soup.prettify())

a = soup.p.a

print(type(a.attrs))

print ('href' in a.attrs)

print (a["href"])
