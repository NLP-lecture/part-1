import sys

filein_src = open(sys.argv[1], "r", encoding="utf-8")
filein_tgt = open(sys.argv[2], "r", encoding="utf-8")
fileout_src = open(sys.argv[3], "w", encoding="utf-8")
fileout_tgt = open(sys.argv[4], "w", encoding="utf-8")

src_lines = filein_src.readlines()
tgt_lines = filein_tgt.readlines()
for no in range(len(src_lines)):
    src = src_lines[no].strip()
    tgt = tgt_lines[no].strip()
    if src and tgt:
        fileout_src.write(src + "\n")
        fileout_tgt.write(tgt + "\n")

filein_src.close()
filein_tgt.close()
fileout_src.close()
fileout_tgt.close()