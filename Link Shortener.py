import pyshorteners


url = input("Please enter link:  ")
shortener = pyshorteners.Shortener()
s = shortener.tinyurl.short("url")
print(s)

