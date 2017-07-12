# read library
import urllib.request

# define url and path
url = "http://uta.pw/shodou/img/28/214.png"
savename = "./test.png"

# download
urllib.request.urlretrieve(url, savename)
print ("success")
