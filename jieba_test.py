import jieba

text = "<dir>征战四海只为今日一胜，我不会再败了。</dir>"
# jieba.cut直接得到generator形式的分词结果
seg = jieba.cut(text) 
print(' '.join(seg)) 

# 也可以使用jieba.lcut得到list的分词结果
seg = jieba.lcut(text)
print(seg)