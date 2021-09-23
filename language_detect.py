import sys
from langid.langid import LanguageIdentifier, model

file_in_src = open(sys.argv[1], "r", encoding="utf-8")
file_in_tgt = open(sys.argv[2], "r", encoding="utf-8")
file_out_src = open(sys.argv[3], "w", encoding="utf-8")
file_out_tgt = open(sys.argv[4], "w", encoding="utf-8")
file_err = open(sys.argv[5], "w", encoding="utf-8")
src_lang = sys.argv[6]
tgt_lang = sys.argv[7]

identifier = LanguageIdentifier.from_modelstring(model, norm_probs=True)
# identifier.set_languages([src_lang, tgt_lang])
identifier.set_languages(["en", "zh", "de", "ja"])

line_num = 0
while True:
    line_src = file_in_src.readline().strip()
    line_tgt = file_in_tgt.readline().strip()
    if not line_src or not line_tgt:
        break

    src_iden = identifier.classify(line_src)
    tgt_iden = identifier.classify(line_tgt)
    if src_iden[0] != src_lang or src_iden[1] < 0.75 or tgt_iden[0] != tgt_lang or tgt_iden[1] < 0.75:
        file_err.write("%s\t%f ||| %s\t%f ||| " % (src_iden[0], src_iden[1], tgt_iden[0], tgt_iden[1]))
        file_err.write("%s\t%s\n" % (line_src, line_tgt))
    else:
        file_err.write("%s\t%f ||| %s\t%f ||| " % (src_iden[0], src_iden[1], tgt_iden[0], tgt_iden[1]))
        file_err.write("%s\t%s\n" % (line_src, line_tgt))
        file_out_src.write("%s\n" % line_src)
        file_out_tgt.write("%s\n" % line_tgt)

    line_num += 1
    if (line_num % 100000 == 0):
        print("\rProcessed %d lines." % line_num, end='')

print("\nDone. Total lines: %d." % line_num)

file_in_src.close()
file_in_tgt.close()
file_out_src.close()
file_out_tgt.close()
file_err.close()
