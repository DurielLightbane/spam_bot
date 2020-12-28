import urllib.request
import json
import random
import requests
import time
import feedparser
from html import unescape

# this was some regex function I accidentally found on the internet
def remove_html_tags(text):
    """Remove html tags from a string"""
    import re
    clean = re.compile('<.*?>')
    return re.sub(clean, '', text)

# this tag marks the end of useful content and contains incriminating source information
end_of_rss = '</div>'

# shitpost library
rss_source = ["https://old.reddit.com/r/nosleep/.rss",
"https://old.reddit.com/r/copypasta/.rss",
"https://old.reddit.com/r/AmItheAsshole/.rss",
"https://old.reddit.com/r/confessions/.rss",
"https://old.reddit.com/r/confession/.rss",
"https://old.reddit.com/r/relationship_advice/.rss",
"https://old.reddit.com/r/TrueOffMyChest/.rss",
"https://old.reddit.com/r/DoesAnybodyElse/.rss",
"https://old.reddit.com/r/explainlikeimfive/.rss",
"https://old.reddit.com/r/TwoXChromosomes/.rss",
"https://old.reddit.com/r/unpopularopinion/.rss",
"https://old.reddit.com/r/tifu/.rss"
]

# target of harassment
real_url = "https://docs.google.com/forms/d/e/1FAIpQLSdwyftrW2dHCQ-gOYZaPpAoWT7iTFuK_KwJK9baTOMio-pFdw/formResponse"

# my test URL to make sure this fuckery works
my_url = "https://docs.google.com/forms/d/e/1FAIpQLSe4K_1nxIkwo9LUGDfBabAOj5zpbl5z-NQ_DjlWapeWSln1HA/formResponse"

# user agent information, because apparently the forms need it
user_agent = {'Referer':real_url,'User-Agent': "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.52 Safari/537.36"}

i = 0

while True:
    NewsFeed = feedparser.parse(rss_source[random.randrange(0,len(rss_source),1)])

    entry = NewsFeed.entries[random.randrange(0,len(NewsFeed['entries']),1)]

    #print (entry.keys())
    thing=entry.content[0]['value'].split(end_of_rss,1)
    thing = remove_html_tags(thing[0])

    # build submission as dict containing entry ID and choice of canned meat.
    submission = {"entry.1051680581": unescape(thing)}
    print(unescape(thing))
    # POST submission, returns HTML code
    r = requests.post(real_url, data=submission, headers=user_agent)
    
    # I like reading the HTML codes
    print (r)

    # Look, I'm lazy and wanted a do-while loop
    if (r.status_code != 200):
        break
    
    # increment counter and print total so far
    i += 1
    print ("Submissions: " + str(i))

    # Take a break after all your hard work, but not too long
    time.sleep(0.5)
