from bs4 import BeautifulSoup

html = """
<html>
	<div id="meigen">
		<h1>wiki books</h1>
		<ul class="items">
			<li>aaa</li>
			<li>bbb</li>
			<li>ccc</li>
		</ul>
	</div>
</html>
"""

soup = BeautifulSoup(html, 'html.parser')

h1 = soup.select_one("div#meigen > h1").string
print("h1: ", h1)

li_list = soup.select("div#meigen > ul.items > li")
for li in li_list:
	print("li: ", li.string)
