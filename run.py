import warnings
import os
from gensim.models.keyedvectors import KeyedVectors

warnings.filterwarnings(action='ignore', category=UserWarning, module='smart_open')
warnings.filterwarnings(action='ignore', category=UserWarning, module='gensim')

print('已扫描到以下模型')
for root, dirs, files in os.walk("./model", topdown=False):
    for i in range(len(files)):
        print(str(i + 1) + ':' + files[i])
model = int(input('请输入要载入的模型序号：'))
try:
    word_vectors = KeyedVectors.load_word2vec_format("model/{}".format(files[model - 1]), binary=True)
except Exception as e_model:
    print("Error:" + repr(e_model))
else:
    print('模型载入完毕')

print("\n1.找出前五名相似")
print("2.计算两词汇相似度")
print("3.输入三个词汇（Ex:郭靖与黄蓉的关系，如同杨过与小龙女的关系）")
while True:
    try:
        query = input("\n输入格式:郭靖，黄蓉……(注意:逗号为中文，最多三个词汇)\n")
        query_list = query.split("，")
        if len(query_list) == 1:
            print("词汇相似词前5排序")
            res = word_vectors.most_similar(query_list[0], topn=5)
            for item in res:
                print(item[0] + "," + str(item[1]))
        elif len(query_list) == 2:
            print("计算两词汇间余弦相似度")
            res = word_vectors.similarity(query_list[0], query_list[1])
            print(res)
        else:
            print("%s与%s的关系，如同%s与下列的关系" % (query_list[0], query_list[1], query_list[2]))
            res = word_vectors.most_similar(positive=[query_list[2], query_list[1]], negative=[query_list[0]], topn=10)
            for item in res:
                print(item[0] + "," + str(item[1]))
    except Exception as e:
        print("Error:" + repr(e))
