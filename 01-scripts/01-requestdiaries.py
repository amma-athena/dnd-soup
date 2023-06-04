import requests
from bs4 import BeautifulSoup

# this script is meant to request the transcripts of each episode of the podcast series "Darknet Diaries".
# the goal of requesting these transcripts is to a) learn how to request texts from a website, b) learn how to store them nicely and c) learn about text analysis.

# 1. Requests

# this is where we nicely ask Jack if we can get his transcript

r = requests.get('https://darknetdiaries.com/transcript/1/')

for i in range(1,134):
    url = 'https://darknetdiaries.com/transcript/'+str(i)+'/'
    r = requests.get(url)
    with open(f"dnd_transcript_ep_{i}.txt", mode="w", encoding="utf-8") as resp_file:
        resp_file.write(r.text)

# we have now requested the html files of episodes 1 through 133.
# the next step is to make the soup!

r = r.text
soup = BeautifulSoup(r, 'html.parser')

print(soup.get_text())

