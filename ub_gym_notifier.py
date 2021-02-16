import requests
from bs4 import BeautifulSoup
from notify_run import Notify

loc = 'Clark Hall'
url_pre = 'https://www.signupgenius.com/go/8050848a9a729a0fe3'
day = 'tuesday12'
days = ['monday','tuesday','wednesday','thursday','friday']
weekdays = [11,12,13,14,15]
url = url_pre + '-'+ day
notify_endpoint = 'https://notify.run/KQQrnm4IqCuxC6D7'

# notify_main = Notify()
# notify_main.endpoint = 'https://notify.run/KQQrnm4IqCuxC6D7'
# notify_main.send('Otha')

# res = requests.get(url)
# html_page = res.content
# soup = BeautifulSoup(html_page, 'html.parser')
# text = str(soup.find_all(text=True))

def find_all(a_str, sub):
    start = 0
    while True:
        start = a_str.find(sub, start)
        if start == -1: return
        yield start
        start += len(sub) # use start += 1 to find overlapping matches

def event_notifier(url,notify_endpoint,day):
    res = requests.get(url)
    html_page = res.content
    soup = BeautifulSoup(html_page, 'html.parser')
    text = str(soup.find_all(text=True))
    notify_main = Notify()
    notify_main.endpoint = notify_endpoint
    ocur = list(find_all(text, 'Already filled'))
    n_ocur = len(ocur)
    # n_ocur = 2
    if(n_ocur<4):
        print(loc+' '+str(4-n_ocur)+' '+'Slot Available for '+str(day))
        notify_main.send(loc+' '+str(4-n_ocur)+' '+'Slot Available for '+day)
    else:
        print(n_ocur)

# event_notifier(url,notify_endpoint)
