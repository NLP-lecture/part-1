import jieba

text = "征战四海只为今日一胜，我不会再败了。"
print("original text:  ", text)

# 也可以使用jieba.lcut得到list的分词结果
seg = jieba.lcut(text)
print(seg)
print(' '.join(seg)) 