import jieba
import sys

file_in = open(sys.argv[1], "r", encoding="utf-8")
file_out = open(sys.argv[2], "w", encoding="utf-8")

index = 0
while True:
    line = file_in.readline()
    line = line.strip()
    if not line:
        break
    tokens = jieba.cut(line)
    line = " ".join(tokens)
    file_out.write(line + "\n")

    index += 1
    if index % 10000 == 0:
        print("\rProcessed %d lines." % index, end='')
print("\nDone. Total lines: %d." % index)

file_in.close()
file_out.close()