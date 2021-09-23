import sys

src = sys.argv[1]
tgt = sys.argv[2]
merge = sys.argv[3]

fs = open(src, "r", encoding="utf-8")
ft = open(tgt, "r", encoding="utf-8")
fw = open(merge, "w", encoding="utf-8")

line_num = 0
while True:
    sline = fs.readline()
    tline = ft.readline()
    if sline == "" or tline == "":
        break
    sline = " ".join(sline.strip().split())
    tline = " ".join(tline.strip().split())
    # strip()去除行首行尾的换行符和空格 split()+" ".join()去除多余空格
    if sline == "" or tline == "":
        continue
    fw.write("%s\t%s\n" % (sline, tline))
    line_num += 1
    if line_num % 100000 == 0:
        print("\rProcessed %d lines." % line_num, end='')
print("\nDone. Total lines: %d." % line_num)

fs.close()
ft.close()
fw.close()