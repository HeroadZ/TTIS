import json
from wordcloud import WordCloud, ImageColorGenerator
import numpy as np
import util
from PIL import Image
import matplotlib.pyplot as plt
from collections import defaultdict, Counter
from scipy.ndimage import gaussian_gradient_magnitude

def createStopwords(path):
    with open(path, 'r', encoding='utf-8') as f:
        stop = set([line.rstrip('\n') for line in f])
    stop.update(['二手', '一个', ' ', '一起', '一起去', '一起玩', '伙伴', '小伙伴', '喜欢', '朋友', '玩',
                '租', '附近', '日本', '地方', '有没有', '找', '一只', '回国', '回', '近期', '飞', '带',
                '帮带', '最近', '东西', '前辈', '专业', '学校', '学',])
    return stop

def create_mask_color(img_path):
    mask = np.array(Image.open(img_path))

    # create mask  white is "masked out"
    mask[mask > 220] = 255

    return ImageColorGenerator(mask), mask

def makeImage(dic, img, font_p="../resources/yahei.ttf", file_name="res/test.png"):
    color, mask = create_mask_color('../resources/pika.jpg')
    wc = WordCloud(background_color='gray', font_path=font_p, mask=mask)

    # generate word cloud
    wc.generate_from_frequencies(dic)
    # change color
    wc.recolor(color_func=color)

    # save to file
    wc.to_file(file_name)

    # show
    # plt.imshow(wc, interpolation="bilinear")
    # plt.axis("off")
    # plt.show()


def freAna(data):
    fre_d = defaultdict(list)
    stopwords = createStopwords('../resources/cn_stopwords.txt')
    for date, a in data.items():
        for k, v in a.items():
            fre_d[k] += v
    for k, v in fre_d.items():
        fre_d[k] = {a: b for a, b in Counter(v).most_common() if a not in stopwords}
    return fre_d


if __name__ == "__main__":
    data = util.read_data('../data/seg.json')
    fre_d = freAna(data)
    for k in util.CATEGORY:
        makeImage(fre_d[k], img='../resources/pika.jpg', file_name='res/'+k+'.png')