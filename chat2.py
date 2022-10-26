# 讀取input檔，並計算字數

# 讀取檔案
def read_file(filename):
	lines = []
	with open(filename, 'r', encoding='utf-8-sig') as f:
		for line in f:
			lines.append(line.strip())
	return lines

# 計算分別講了幾個字，幾個貼圖，幾張圖片
def count(lines):
	allen_word_count = 0
	viki_word_count = 0
	allen_sticker_count = 0
	viki_sticker_count = 0
	allen_pic_count = 0
	viki_pic_count = 0
	for line in lines:
		s = line.split(' ')
		time = s[0]
		name = s[1]
		text = s[2:]
		if name == 'Allen':
			if s[2] == '貼圖':
				allen_sticker_count += 1
			elif s[2] == '圖片':
				allen_pic_count += 1
			else:
				for m in text: # 如果不是貼圖，也不是圖片，再計算字數
					allen_word_count += len(m)
		elif name == 'Viki':
			if s[2] == '貼圖':
				viki_sticker_count += 1
			elif s[2] == '圖片':
				viki_pic_count += 1
			else:
				for m in text:
					viki_word_count += len(m)
	print('Allen說了', allen_word_count, '個字')
	print('Viki說了', viki_word_count, '個字')
	print('Allen貼了', allen_sticker_count, '個貼圖')
	print('Viki貼了', viki_sticker_count, '個貼圖')
	print('Allen貼了', allen_pic_count, '張圖片')
	print('Viki貼了', viki_pic_count, '張圖片')

# 定義main-把上面的打包進來
def main():
	lines = read_file('LINE-Viki.txt')
	lines = count(lines)

# 執行main
main()