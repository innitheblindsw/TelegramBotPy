import requests
import time

# Proxy user
proxies = {"http":"http://user:pass@proxy:port"}
#r = requests.get("http://www.example.com/", proxies=proxies)
#print(r.content)

# list of quotes
quotes = [
    'First, solve the problem. Then, write the code. – John Johnson',
    'Experience is the name everyone gives to their mistakes. – Oscar Wilde',
    'Code is like humor. When you have to explain it, it’s bad. – Cory House',
    'Before software can be reusable it first has to be usable. – Ralph Johnson',
    'Optimism is an occupational hazard of programming: feedback is the treatment. - Kent Beck'
]

# loop through the quotes
for quote in quotes:
    chat_id = requests.get('https://api.telegram.org/bot1157813326:AAEkOM1xQd1HjBHXxPlBTmrcKxIfJFr792w/getUpdates', proxies=proxies)
    print (chat_id.text)
    url = 'https://api.telegram.org/bot1157813326:AAEkOM1xQd1HjBHXxPlBTmrcKxIfJFr792w/sendMessage?chat_id=852226201&text="{}"'.format(quote)
    s = requests.get(url, proxies=proxies)
    #print ( s.content )
    print("---")
    #print ("send")
    #requests.post(url, proxies=proxies)
    # sends new quotes every 20seconds
    time.sleep(10)