# -*- coding: utf-8 -*-
from collections import Counter
import re
from collections import defaultdict
import sys
import wikipedia
import codecs
import requests

"""
ToDo: 0. Scrape articles in german (preferably wikipedia)
      1. API for german wiktionary: Working with Yandex translate API
      2. find bedeutung, beispiel for freq words 
      3. convert to Anki format
      4. Add to Anki
"""


# print 'Number of arguments:', len(sys.argv), 'arguments.'
# print 'Argument List:', str(sys.argv)
# def nextline(i):
#     return "\n"*i
#
# # Counter = Counter(train_data)
# def get_articles(theme,savefile, count=1):
#     wikipedia.set_lang("de")# don't change
#     list_of_articles = wikipedia.search(theme,count)
#     print(list_of_articles)
#     for article in list_of_articles:
#         with codecs.open(savefile,'a', encoding='utf-8') as ft:
#             ft.write(nextline(2))
#             #ft.write("---------------------{}--------------------------".format(article))
#             #ft.write(nextline(2))
#             ft.write(wikipedia.summary(article))
#             ft.write(nextline(2))
#
#
#
#
def topten(filename, savefile, stopwordfile):
    stop_words = []
    with open(stopwordfile, 'r') as f:
        s = f.readlines()
        for i in range(len(s)):
            if len(s[i].split()[0]) < 7:
                stop_words.append(s[i].split()[0])

    fullWords = re.findall(r'\w+', codecs.open(filename, 'r',encoding='utf-8').read().lower())
    d = defaultdict(int)
    for word in fullWords:
        if word not in stop_words:
            d[word] += 1
    finalFreq = sorted(d.items(), key=lambda t: t[1], reverse=True)
    finalFreq_some = finalFreq[10:20]
    with open(savefile, 'w') as ft:
        for i in range(len(finalFreq_some)):
            ft.write(finalFreq_some[i][0])
            ft.write("\n")

    return finalFreq[10:20]


# if __name__ == '__main__':
#     #get_articles("python","somegerman.txt",3)
#     x=topten("somegerman.txt","thisfile.txt","german_stopwords.txt")
#     print(x) # this is to be fed to text in Yandex api
#
#
#     # if len(sys.argv) != 4:
#     #     pass
#     # else:
#     #     topten(sys.argv[1], sys.argv[2], sys.argv[3])

API_KEY = 'trnsl.1.1.20191114T124156Z.cc3f512f191b463c.854a11eb83df2ce384753f773c5e762463610796'

url = 'https://translate.yandex.net/api/v1.5/tr.json/translate'

params = dict(key=API_KEY, text='krankenheit',lang='de-en')

res = requests.get(url,params=params)

print(res.text)