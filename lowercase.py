import sys

fin = open(sys.argv[1], "r", encoding="utf-8")
fout = open(sys.argv[2], "w", encoding="utf-8")

def deal():
    no = 0
    for line in fin:
        no += 1
        # if no % 100 == 0:
        #     return
        if no % 10000 == 0:
            print("\rsolved %dw lines"%(no/10000), end='')
        fout.write(line.lower())
    print("\nDone. Total lines: %d." % no)

deal()

fin.close()
fout.close()