from collections import Counter
import re
from collections import defaultdict
import sys


# print 'Number of arguments:', len(sys.argv), 'arguments.'
# print 'Argument List:', str(sys.argv)


# Counter = Counter(train_data)

def topten(filename, savefile, stopwordfile):
    stop_words = []
    with open(stopwordfile, 'r') as f:
        s = f.readlines()
        for i in range(len(s)):
            if len(s[i].split()[0]) < 7:
                stop_words.append(s[i].split()[0])

    fullWords = re.findall(r'\w+', open(filename, 'r').read().lower())
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

    return finalFreq[:10][0]


if __name__ == '__main__':

    if len(sys.argv) != 4:
        pass
    else:
        topten(sys.argv[1], sys.argv[2], sys.argv[3])
