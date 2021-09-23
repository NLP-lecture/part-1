import sys
import re

def Process():
    file_in_path = str(sys.argv[1])
    file_out_path = str(sys.argv[2])
    file_log_path = str(sys.argv[3])
    file_err_path = str(sys.argv[4])
    
    file_in = open(file_in_path, 'r', encoding='utf-8', newline='\n')
    file_out = open(file_out_path, 'w', encoding='utf-8')
    file_log = open(file_log_path, 'w', encoding='utf-8')
    file_error = open(file_err_path, 'w', encoding='utf-8')

    regular_1 = u'[(（]{1,}[¡ãウ Ж£º¡ª�£©£¬ËþÊ½¹¤×÷Ì¨]{1,}[)）]{1,}'

    index = 0
    while True:
        line = 	file_in.readline()
        if not line:
            break
        line = str(line).strip()

        index += 1
        if index % 10000 == 0:
            print('\r[Process Info]:Now Processing '+ str(index) + '.', end='')
        
        ext = line.split('\t')

        old_line = line
        src_line = str(ext[0])
        tgt_line = str(ext[1])
        
        while True and len(src_line) > 0:
            if src_line[0] not in {'*', '-',  '–',  ' ', '+', '?', '.', '!', ',',  '/', '$',  '#', '！'}:
                break
            src_new_line = src_line[1:]
            line = line.replace(src_line, src_new_line)
            src_line = src_new_line

        while True and len(tgt_line) > 0:
            if tgt_line[0] not in {'*', '-',  '–',  ' ', '+', '?', '.', '!', ',',  '/', '$',  '#', '！'}:
                break
            tgt_new_line = tgt_line[1:]
            line = line.replace(tgt_line, tgt_new_line)
            tgt_line = tgt_new_line

        if len(src_line) == 0:
            file_error.write(line+'\n')
            continue
        if len(tgt_line) == 0:
            file_error.write(line+'\n')
            continue

        if line.find('¡ã') != -1:
            line = line.replace('¡ã', '°')

        if line.find('¨¨') != -1:
            line = line.replace('¨¨', '')

        if line.find('ウ') != -1:
            line = line.replace('ウ', '')

        if line.find('Ж') != -1:
            line = line.replace('Ж', '')

        if src_line.find('\n\n'):
            ch_new_sentence = src_line.replace('\n\n', '')
            line = line.replace(src_line, ch_new_sentence)

        if tgt_line.find('\n\n'):
            en_new_sentence = tgt_line.replace('\n\n', '.')
            line = line.replace(tgt_line, en_new_sentence)

        if line.find('Billy£º') != -1:
            line = line.replace('Billy£º', '')

        if line.find('�') != -1:
            line = line.replace('�', '')

        if line.find('oC') != -1 and line.find('℃') != -1:
            line = line.replace('oC', '℃')

        if line.find('~') != -1 and line.find('¡«') != -1:
            line = line.replace('¡«', '~')

        if line.find('¡æ') != -1:
            line = line.replace('¡æ' ,'  ℃ ')

        if line.find('%n%n') != -1:
            line = line.replace('%n%n', '')

        if line.find('……') != -1 and line.find('¡­') != -1:
            line = line.replace('¡­', '……')

        if line.find('...') != -1 and line.find('¡­') != -1:
            line = line.replace('¡­', '...')

        if line.find('¡¯') != -1:
            line = line.replace('¡¯', '’')

        if line.find('£©') != -1:
            line = line.replace('£©', ')')

        if line.find('£¨') != -1:
            line = line.replace('£¨', "(")

        if line.find('£¬') != -1:
            line = line.replace('£¬', '')

        if src_line[0] == '■':
            ch_new_sentence = src_line[1:]
            line = line.replace(src_line, ch_new_sentence )
        if tgt_line[0] == '■':
            en_new_sentence = tgt_line[1:]
            line = line.replace(tgt_line, en_new_sentence)

        if src_line[0] == '•':
            ch_new_sentence = src_line[1:]
            line = line.replace(src_line, ch_new_sentence )
        if tgt_line[0] == '•':
            en_new_sentence = tgt_line[1:]
            line = line.replace(tgt_line, en_new_sentence)

        if line.find('¡¢') != -1:
            line = line.replace('¡¢', '、')

        if line.find('¡±') != -1:
            line = line.replace('¡±', '')

        if line.find('¡ª') != -1 and line.find(' ') != -1:
            line = line.replace('¡ª', '')
            line = line.replace(' ', '')

        if line.find('¨º') != -1:
            line = line.replace('¨º', '')

        if line.find('¡°') != -1:
            line = line.replace('¡°', '')

        if line.find('¤') != -1:
            line = line.replace('¤', '')

        cover_list = re.findall(regular_1, line)
        if len(cover_list) > 0:
            for i in cover_list:
                line = line.replace(str(i), '')

        if line != old_line:
            file_log.write(old_line+'\t'+line+'\n')
        if line.strip() != "":
            file_out.write(line+'\n')

    print('\r[Process Info]:Now Processing '+ str(index) + '.')

    file_in.close()
    file_log.close()
    file_out.close()
    file_error.close()

Process()
