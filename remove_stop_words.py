from re import T
import sys

# 需要先分词
file_in = open(sys.argv[1], "r", encoding="utf-8")
file_out = open(sys.argv[2], "w", encoding="utf-8")
file_err = open(sys.argv[3], "w", encoding="utf-8")
stop_words_set = set()

def init_stop_words_set(stop_words_set):
    stop_words_file = open("baidu_stopwords.txt", "r", encoding="utf-8")
    while True:
        line = stop_words_file.readline()
        line = line.strip()
        if not line:
            break
        if line not in stop_words_set:
            stop_words_set.add(line)
    stop_words_file.close()

init_stop_words_set(stop_words_set)

index = 0
while True:
    line = file_in.readline()
    line = line.strip()
    if not line:
        break
    line_new = line
    for word in line.split():
        if word in stop_words_set:
            line_new = line_new.replace(word, "", 1)
            file_err.write(word + " ")
    line_new = line_new.strip()
    file_err.write("\n")
    file_out.write(line_new + "\n")
    index += 1
    if index % 10000 == 0:
        print("\rProcessed %d lines" % index, end="")
print("\nDone. Total lines: %d." % index)

file_in.close()
file_out.close()
file_err.close()