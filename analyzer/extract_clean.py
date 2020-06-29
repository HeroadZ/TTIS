import json
from bs4 import BeautifulSoup
from collections import defaultdict
import util

def clean(data):
    clean_data = {}
    names = defaultdict(int)
    

    for date, article in data.items():
        soup = BeautifulSoup(article, "html.parser")
        spans = soup("p")
        d = defaultdict(list)
        for s in spans:
            txt = s.get_text()
            if not txt or txt[0] != '【':
                continue

            tag = txt[1:4]
            names[tag] += 1

            for k, v in util.CATEGORY.items():
                if tag in v:
                    d[k].append(txt[5:-7])
                    break
        clean_data[date] = d
        print(date + 'finished.')

    print('finished.')
    # print(names)
    return clean_data


def main():
    articles = util.read_data('../data/articles.json')
    clean_data = clean(articles)
    util.save_data(clean_data, '../data/clean.json')

if __name__ == '__main__':
    main()