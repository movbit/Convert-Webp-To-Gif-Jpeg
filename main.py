
import os
import argparse
from time import sleep
import mmap
from PIL import Image


def getListFiles(ext, path):
	list_files = []

	for file in os.listdir(path):
		if file.endswith('.' + ext):
			list_files.append(file)

	return list_files

def convert_Webp_To_Gif_Jpeg(files, output_path):
	for file in files:
		path = output_path + '\\' + file

		try:
			type = getTypeFile(path)

			if type == "gif":
				im = Image.open(path)
				im.save (path[:-4] + 'gif', 'gif', save_all=True, optimize=True, background=0)

			else:
				im = Image.open(path).convert("RGB")
				im.save (path[:-4] + 'jpg', 'jpeg', optimize=True, background=0)

			sleep(5)

		except:
			pass

def getTypeFile(filename):
	with open(filename, "rb") as f:
		file_map = mmap.mmap (f.fileno(), 48, access=mmap.ACCESS_READ)
		flag = file_map[30:34]

		return "gif" if flag == "ANIM" else "image"



if __name__ == "__main__":
	PATH_DIR_WORK = os.getcwd()
	parser = argparse.ArgumentParser()
	parser.add_argument("-x", "--ext", help="File extension to search", default="webp", required=True)
	parser.add_argument("-s", "--search_path", help="Full path of the files to be converted", default=PATH_DIR_WORK)
	
	args = parser.parse_args()

	files = getListFiles(args.ext, args.search_path)
	if not files:
		print "\nNo files found"
		exit()

	convert_Webp_To_Gif_Jpeg(files, args.search_path)

