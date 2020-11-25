import os
import traceback

def anime():
	i = 0
	j = 0
	for root, dirs, files in os.walk("Anime"):
		for file in files:
			try:
				i += 1
				print("File: " + "Anime/" + file)
				yield "/Anime/" + file
			except:
				j += 1
				print(traceback.format_exc())
	print(f"Всего файлов: {i} Файлы с ошибкой: {j}")
	print("Done!")
