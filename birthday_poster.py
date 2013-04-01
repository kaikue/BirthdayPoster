#BirthdayPoster v1.0 by Kai Kuehner
#Requires Python Requests: http://docs.python-requests.org/en/latest/
#Replace YOUR_ID with your Facebook ID or URL and ACCESS_KEY with a Facebook access token (from graph.facebook.com)

import webbrowser
import requests
import datetime


YOUR_ID = "put your ID here"
ACCESS_TOKEN = "put your access token here"

ids = {}
today = datetime.date.today()
friends = requests.get("https://graph.facebook.com/" + YOUR_ID + "?fields=friends.fields(birthday,first_name)&access_token=" + ACCESS_TOKEN)
text = friends.text
datastring = text[text.find("["):text.find("]") + 1]
exec("datalist = " + datastring)
for dct in datalist:
    if "birthday" in dct.keys():
        if int(dct["birthday"][:2]) == today.month and int(dct["birthday"][4:6]) == today.day:
            ids[dct["id"]] = dct["first_name"]

for person in ids.keys():
    link = "https://www.facebook.com/dialog/feed" + \
    "&to=" + person + \
    "?app_id=432238440193197" + \
    "&picture=http://us.123rf.com/400wm/400/400/dmstudio/dmstudio1006/dmstudio100600071/7318269-birthday-cake-with-burning-candles.jpg" + \
    "&name=Happy birthday!" + \
    "&caption=Happy birthday, " + ids[person] + "!" + \
    "&description=This is an automatically generated birthday message." + \
    "&redirect_uri=http://facebook.com/"
    webbrowser.open(link)
