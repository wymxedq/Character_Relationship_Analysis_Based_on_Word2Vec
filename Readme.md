# 基于Word2Vec的文本词汇关系分析

## 文件说明

### 文件目录

1. 文件夹：
   - character_frequency：用于存放生成的词频统计图
   - model：存放已训练的模型以供读取使用
   - novel：存放小说文本

2. 文件
   - name.txt：存储小说里的人物名字，已包括红楼梦、鹿鼎记、射雕英雄传、神雕侠侣、天龙八部五本小说人物名字
   - sentences.txt：分词后的小说文本
   - user_dict.txt：存储小说里的人名及大部分专有名词，已包括五本小说的人名以及金庸武侠小说的所有招式
   - all_model.py：用于生成all.model.bin的程序文件
   - train.py：训练模型的程序文件
   - run.py：加载已有模型，并查询词汇之间的关系
   - statistical.py：用于生成词频统计图

## 代码说明

- 环境要求：python3环境

  ​					jieba

  ​					gensim

- 运行 statistical.py 将生成词频统计图，结果存放在 character_frequency 文件夹中

- 运行 train.py 将生成训练模型，文件将存放在 model 文件夹中，名称格式为小说名-小说名.model.bin

-  运行 run.py 将加载 model 文件夹下已有模型，并进行词汇间的关系分析

