import feedparser
from html import unescape
import random

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

# this was some regex function I accidentally found on the internet
def remove_html_tags(text):
    """Remove html tags from a string"""
    import re
    clean = re.compile('<.*?>')
    return re.sub(clean, '', text)

# this tag marks the end of useful content and contains incriminating source information
end_of_rss = '</div>'

NewsFeed = feedparser.parse(rss_source[random.randrange(0,len(rss_source),1)])

entry = NewsFeed.entries[random.randrange(0,len(NewsFeed['entries']),1)]

#print (entry.keys())
thing=entry.content[0]['value'].split(end_of_rss,1)
thing = remove_html_tags(thing[0])
print(unescape(thing))