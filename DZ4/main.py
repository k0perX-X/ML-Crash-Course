import logging
import cv2
import os
import traceback
import time
import shutil

if os.path.exists("NewDataset"): shutil.rmtree("NewDataset")
if os.path.exists("log.txt"): os.remove("log.txt")
i = 0
j = 0
logging.basicConfig(filename="log.txt", level=logging.INFO)
for root, dirs, files in os.walk("Dataset"):
	if dirs != []:
		print(dirs)
		os.mkdir("NewDataset")
		for dir in dirs:
			os.mkdir("NewDataset/"+dir)
			for root1, dirs1, files1 in os.walk("Dataset/"+dir):
				for file in files1:
					try:
						i+=1
						print("File: " + "Dataset/"+dir+'/'+file)
						img = cv2.imread("Dataset/"+dir+'/'+file)
						img = cv2.resize(img, (50, 50))
						cv2.imwrite("NewDataset/"+dir+'/'+file, img)
					except:
						j += 1
						print(traceback.format_exc())
						logging.error(time.ctime(time.time()) + " File: " + "Dataset/"+dir+'/'+file + "афацф " + traceback.format_exc())
print(f"Всего файлов: {i} Файлы с ошибкой: {j}")
logging.info(f"Total errors: {j}")
print("Done!")