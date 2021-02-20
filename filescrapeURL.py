import requests

url = input("Enter the URL?\n")
#splits the url into a list seperated by /
split = url.rsplit("/")

r = requests.get(url)
print("CONNECTED")
#saves the get request as in the specified location under what it was originally called.
save=open("/mnt/c/Users/Sal/Videos/scrapes/" + split[-1], "wb")
save.write(r.content)
