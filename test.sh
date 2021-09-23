# 1 测试读取、写入文件
python read_file.py test_data/read_file.en test_data/read_file.zh test_data/read_file.out

# 2 测试jieba中文分词
python jieba_token.py test_data/jieba.zh test_data/jieba.zh.out

# 3 测试Moses英语分词
perl ./mosesdecoder-master/scripts/tokenizer/tokenizer.perl -l en -no-escape -threads 6 < test_data/moses.en > test_data/moses.en.out

# 3 测试删除停用词
python remove_stop_words.py test_data/stop_words.zh test_data/stop_words.zh.out test_data/stop_words.zh.err

# 4 测试小写化
python lowercase.py test_data/lowercase.en test_data/lowercase.en.out

# 5 测试删除html标签
python remove_html.py test_data/html.zh test_data/html.zh.out test_data/html.zh.err

# 6 测试删除长句子
python remove_long_sentence.py test_data/long_sentence.en test_data/long_sentence.zh test_data/long_sentence.en.out test_data/long_sentence.zh.out

# 7 测试语言检测
python language_detect.py test_data/language.en test_data/language.zh test_data/language.en.out test_data/language.zh.out test_data/language.err en zh

# 8 测试删除、替换特殊字符
# python remove_special_symbol.py




