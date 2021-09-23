# 默认 源语言src为英文en 目标语言tgt为中文zh
srcfile=$1
tgtfile=$2
moses_path=./mosesdecoder-master/scripts/tokenizer/tokenizer.perl

echo -e "### STEP-0 ###"
wc -l $srcfile
wc -l $tgtfile


echo -e "\n\n\n### STEP-1 remove_blank_line.py ###"
src_before=$srcfile
tgt_before=$tgtfile
src_after=$src_before.rmbkline
tgt_after=$tgt_before.rmbkline
python remove_blank_line.py $src_before $tgt_before $src_after $tgt_after
wc -l $src_after
wc -l $tgt_after


echo -e "\n\n\n### STEP-2 language_detect.py ###"
src_before=$src_after
tgt_before=$tgt_after
src_after=$src_before.langid
tgt_after=$tgt_before.langid
python language_detect.py $src_before $tgt_before $src_after $tgt_after language.err en zh
wc -l $src_after
wc -l $tgt_after


echo -e "\n\n\n### STEP-3 remove_html.py ###"
src_before=$src_after
tgt_before=$tgt_after
src_after=$src_before.rmhtml
tgt_after=$tgt_before.rmhtml
python remove_html.py $src_before $src_after html.en.err
python remove_html.py $tgt_before $tgt_after html.zh.err
wc -l $src_after
wc -l $tgt_after


echo -e "\n\n\n### STEP-4 lowercase.py ###"
src_before=$src_after
src_after=$src_before.lowercase
python lowercase.py $src_before $src_after
wc -l $src_after
wc -l $tgt_after


echo -e "\n\n\n### STEP-5 tokenizer.perl ###"
src_before=$src_after
src_after=$src_before.token
perl $moses_path -l en -no-escape -threads 6 < $src_before > $src_after
wc -l $src_after
wc -l $tgt_after


echo -e "\n\n\n### STEP-6 jieba_token.py ###"
tgt_before=$tgt_after
tgt_after=$tgt_before.token
python jieba_token.py $tgt_before $tgt_after
wc -l $src_after
wc -l $tgt_after


echo -e "\n\n\n### STEP-7 remove_long_sentence.py###"
src_before=$src_after
tgt_before=$tgt_after
src_after=$src_before.rmlongst
tgt_after=$tgt_before.rmlongst
python remove_long_sentence.py $src_before $tgt_before $src_after $tgt_after
wc -l $src_after
wc -l $tgt_after


echo -e "\n\n\n### STEP-8 remove_stop_words.py ###"
src_before=$src_after
tgt_before=$tgt_after
src_after=$src_before.rmstopwd
tgt_after=$tgt_before.rmstopwd
python remove_stop_words.py $src_before $src_after stop_words.en.err
python remove_stop_words.py $tgt_before $tgt_after stop_words.zh.err
wc -l $src_after
wc -l $tgt_after


echo -e "\n\n\n### STEP-9 remove_blank_line.py ###"
src_before=$src_after
tgt_before=$tgt_after
src_after=$src_before.rmbkline
tgt_after=$tgt_before.rmbkline
python remove_blank_line.py $src_before $tgt_before $src_after $tgt_after
wc -l $src_after
wc -l $tgt_after


echo -e "\n\n\n### FINISH !!! ###"