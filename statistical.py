# coding=gbk

import codecs
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

font_song = FontProperties(fname="C:/Windows/Fonts/simsun.ttc")
novels = ['天龙八部', '红楼梦', '神雕侠侣', '射雕英雄传', '鹿鼎记']

with open('name.txt', 'r', encoding='UTF-8') as name:
    characters_info = name.read()
    characters_name = characters_info.split('\n')
    name.close()
for novel in novels:
    with codecs.open("novel/{}.txt".format(novel), encoding='UTF-8') as t:
        content = t.read()
    chars = np.array(characters_name)
    counts = np.array([content.count(c) for c in chars])
    idx = counts.argsort()

    plt.barh(range(15), counts[idx[-15:]])
    plt.title(novel, fontproperties=font_song)
    plt.yticks(range(15), chars[idx[-15:]], fontproperties=font_song)
    plt.savefig("character_frequency/{}.png".format(novel))
    plt.show()
