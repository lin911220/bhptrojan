import os

# 列出目錄中所有檔案

def run(**args):
	print("[*] In dirlister module.")
	files = os.listdir(".")
	return str(files)
