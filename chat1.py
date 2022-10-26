# 讀取input檔，並輸出output(對話記錄中，每一行都有人名加冒號)

# 讀取檔案
def read_file(filename):
	lines = []
	with open(filename, 'r', encoding='utf-8-sig') as f:
		for line in f:
			lines.append(line.strip())
	return lines

# 轉換檔案
def convert(lines):
	new = []
	person = None
	for line in lines:
		if line == 'Allen':
			person = 'Allen'
			continue
		elif line == 'Tom':
			person = 'Tom'
			continue
		if person:
			new.append(person + ': ' + line)
	return new

# 儲存檔案
def write_file(filename, lines):
	with open(filename, 'w', encoding='utf-8-sig') as f:
		for line in lines:
			f.write(line + '\n')

# 定義main-把上面的打包進來
def main():
	lines = read_file('input.txt')
	lines = convert(lines)
	write_file('output.txt', lines)

# 執行main
main()