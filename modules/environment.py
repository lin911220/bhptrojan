import os

# 擷取執行木馬的遠端機器上設定的環境變數

def run(**args):
	print("[*] In environment module.")
	return os.environment
