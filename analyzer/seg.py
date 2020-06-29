from LAC import LAC
import json
import util

def seg_data(data, lac):
    for date, article in data.items():
        for k, v in article.items():
            data[date][k] = [item for sub in lac.run(v) for item in sub]
    return data


def main():
    lac = LAC(mode='seg')
    data = util.read_data('../data/clean.json')
    data = seg_data(data, lac)
    util.save_data(data, '../data/seg.json')

if __name__ == "__main__":
    main()