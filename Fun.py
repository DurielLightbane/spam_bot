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

# JSON methodology

"""
# Need to open JSON file correctly and grab story by index. 
with open("data_file.json", "r") as db:
    data = json.load(db)
    spam =[]
    spam = data['Story']

    i = 0

    # Fuck these kids, begin cyber bullying routine
    while True:
        #let RNGeesus take the wheel
        index_choice = random.randrange(0,len(spam),1)
    
        # build submission as dict containing entry ID and choice of canned meat.
        submission = {"entry.1051680581": spam[index_choice]}

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

"""

#real_submission = {"entry.1051680581": "So my cat, Franki, recently came down with a pretty severe stomach virus. The vet gave me some anti biotic drops to put in his food but when I’d do that Franki wouldn’t touch it. So, the vet suggested using a small dropper tube to insert the medicine directly into his anus. The first time was absolute hell, my cat fought me the whole time but once the tube was in and the medicine pushed out he seemed to calm quite a bit. Well the next day he was acting strange, he has always been an independent cat, rarely coming around, never wanting to be held, but as I sat on the couch he started walking back and forth meowing and rubbing my leg. He then went and jumped up on the table where we’d done the application the night before and meowed louder and louder until I decided I guess we will go ahead and do the medicine treatment. This time he didn’t fight me though, and when I inserted the tube he closed his eyes, stretched his neck, and let out a noise that can only be described as a moan of pure ecstasy. Maybe the medicine made him feel better, I supposed. That night he slept on my bed curled up right next to me, which he had never done before. For the next week he’d do the same thing every day, meow on the table until he got his ‘fix’... But then the medicine ran out. Even though I had no medicine he’d still cry and beg for it, I thought maybe if I insert it without medicine he will realize it doesn’t make him feel better anymore and forget about it. Well that was 2 weeks ago and he is only getting worse. He walks around me all day with his tail up presenting his rectum and trying to entice me. He is demanding insertions more and more often. Yesterday I caught him looking longingly at the turkey baster... When I sit he jumps in my lap purring and rubbing me affectionately. It was then in horror I realized my cat thinks I’m his gay lover, and that I’ve been sexually pleasing him for weeks now. Needless to say the sexual tension between us is palpable. How do I let my cat know that I’m not gay, but still like him as a friend?"}
#submission = {"entry.2111692148": "When I was 13 I tried to fuck a banana. It wasn't peeled and was so painful, I ended up squishing it with my vagina, contracting in pain. Then the peel popped open inside me. I felt this and panicked to pull the banana out. It was just a peel now. I had a banana smoothie in my vagina. I pushed to give birth to this banana abomination but it didn't come out because the fruit was sticking to my walls. I went in with my fingers and scraped out as much banana I could before my mom tried to talk to me. I rushed to get out of the bathroom with the scent of banana afterbirth on my body, praying she wouldn't question the banana peel and chunks in the bathroom garbage can. Looking back, she probably noticed them, but I'm still grateful she never asked and let me get away. I have enough regret from this."}




#TODO:
#RNG timed submissions
#RNG personas
#RNG post type
#RNG characters, parks, kingdoms
