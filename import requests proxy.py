import requests

proxies = {"http":"http://username:password@proxy_ip:proxy_port"}

r = requests.get("http://www.example.com/", proxies=proxies)

print(r.content)