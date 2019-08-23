import codecs
import jieba
import warnings
import os
from gensim.models import word2vec

warnings.filterwarnings(action='ignore', category=UserWarning, module='smart_open')

novels=['天龙八部','红楼梦','射雕英雄传','神雕侠侣','鹿鼎记']
print('训练准备过程开始，预计将消耗一段时间')
sentences = []
jieba.load_userdict("user_dict.txt")  # 载入自定义词典

for novel in novels:
    print('正在对{}进行分词.'.format(novel))
    with codecs.open('novel/{}.txt'.format(novel), encoding='UTF-8') as f:
        sentences += [list(jieba.cut(line.strip())) for line in f]
print('分词完成.')

print('正在保存分词结果到sentences.txt.')
f = open('sentences.txt', 'w', encoding='UTF-8')
text = ''
for line in sentences:
    text += ' '.join(line)
    text += '\n'
f.write(text)
f.close()
print('保存完成.')

print("训练中……")
# Load file
sentence = word2vec.Text8Corpus("sentences.txt")
# Setting degree and Produce Model(Train)
model = word2vec.Word2Vec(sentence,size=500, window=5, min_count=5, workers=4, sg=1, max_vocab_size=120000000)  # size=500, window=5, min_count=5, workers=4, sg=1, max_vocab_size=120000000
try:
    # 删除重复模型
    os.remove("model/all.model.bin")
except:
    pass
else:
    print('检测到同名模型，将自动删除')
# Save model
model.wv.save_word2vec_format("model/all.model.bin",binary=True)
print("训练模型已存储")
