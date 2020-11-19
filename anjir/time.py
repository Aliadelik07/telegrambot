import requests
from time import sleep

i = 0
while i < 8:
    guys =["@aliadelimahi", "@rnkrz", "@BlackZQ", "@lil1245", "@k1mhtdi", "@Mohammadaminkzm", "@sociopatch", "@Arm4nB"]
    chatid = 809514744
    text ="https://api.telegram.org/bot809514744:AAFWCeoM-XjFvndmjlG1GNJ6ayG6QNJr8ww/sendMessage?chat_id=80987657&text=it's your turn "+guys[i]
    requests.post(text)
    i += 1
    if i == 8:
        i=0
    sleep(24*60*60)