import re
import sys

regular_rule = '<[a-zA-Z0-9-\'"= :/;_#.%]{1,}[>]{0,}'

def init_html_tag_set(html_set):
	html_tag_set_path = 'html.label.set'
	set_file = open(html_tag_set_path, 'r', encoding="utf-8")
	while True:
		line = set_file.readline()
		line = str(line).strip()
		if not line:
			break
		if line not in html_set:
			html_set.add(line) # <dir>
			html_set.add(line[0:len(line)-1]) # <dir
			html_set.add(line[0] + '/' + line[1:]) # </dir>
	set_file.close()

html_set = set()
init_html_tag_set(html_set)

def del_html_tag(line, temp_tags):
	result = line
	for i in temp_tags:
		tag = i.split()[0]
		if tag in html_set:
			result = result.replace(i, "", 1)
	return result

src_file = open(sys.argv[1], "r", encoding="utf-8")
out_file = open(sys.argv[2], "w", encoding="utf-8")
err_file = open(sys.argv[3], "w", encoding="utf-8")

index = 0
while True:
	line = src_file.readline().strip()
	if not line:
		break

	temp_tags = re.findall(regular_rule, line)
	line_new = del_html_tag(line, temp_tags)

	if line != line_new:
		err_file.write(line + "\n")
		# err_file.write(line + "\t|||\t" + line_new + "\n")
	out_file.write(line_new + "\n")

	index += 1
	if index % 10000 == 0:
		print("\rProcessed %d lines." % index, end='')
print("\nDone. Total lines: %d." % index)

src_file.close()
out_file.close()
err_file.close()