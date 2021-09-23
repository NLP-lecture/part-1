import sys

fo1 = open(sys.argv[1], "r")
fo2 = open(sys.argv[2], "r")
fout1 = open(sys.argv[3], "w")
fout2 = open(sys.argv[4], "w")
for a in fo1:
    b = fo2.readline()
    if len(a.strip().split(" ")) <= 120 and len(b.strip().split(" ")) <= 120:
        fout1.write(a)
        fout2.write(b)
