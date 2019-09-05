import os
import time
import re
import ctypes
import platform
import shutil

def run():
	print('start_deleteFile')
	while True:
		dir1 = os.listdir('d:/RecordFile')[0]
		freeSpace = get_free_space_mb('D:\\')
		if freeSpace <60:
			shutil.rmtree('d:\RecordFile\%s' %dir1)
			print('already delete dir %s' %dir1)
			print(time.asctime( time.localtime(time.time() ) ) )
		time.sleep(43200)

def get_free_space_mb(folder):
	free_bytes = ctypes.c_ulonglong(0)
	ctypes.windll.kernel32.GetDiskFreeSpaceExW(ctypes.c_wchar_p(folder), None, None, ctypes.pointer(free_bytes))
	return free_bytes.value/1024**3

def main():
	run()

if __name__=='__main__':
	main()
