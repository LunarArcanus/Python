#!/usr/bin/python

import re

#	JPEG Extraction from binary files
#	FF D8 (2 bytes) = Start
#	FF D9 (2 bytes) = End

STARTBYTES = (0xFF, 0xD8)
ENDBYTES   = (0xFF, 0xD9)
SBS = [chr(v) for v in STARTBYTES]
EBS = [chr(v) for v in ENDBYTES]
PATTERN = re.compile(r"(?<={} {}).*?(?={} {})".format(
	STARTBYTES[0], STARTBYTES[1], ENDBYTES[0], ENDBYTES[1]))
ALL = -1

def extract_images(filename, count=ALL):
	"Extract <count> JPG images from <filename>."
	if (count < -1) or (count == 0):
		raise ValueError, "Wrong count given."
	imgfile = open(filename, "rb")
	fbytes = []
	n = 0
	while True:
		b = imgfile.read(1)
		if not b:
			break
		else:
			fbytes.append(str(ord(b)))
	fbytes = " ".join(fbytes)
	images = re.findall(PATTERN, fbytes)
	if count==ALL:
		while n<len(images):
			split = images[n].split()
			with open("%s_EXT.jpg" %(n), "a+b") as out:
				out.writelines(SBS)
				for x in split:
					out.write(chr(int(x)))
				out.writelines(EBS)
			n+=1
	elif count!=ALL:
		if count>=len(images):
			count = len(images)
		while n<count:
			split = images[n].split()
			with open("%s_EXT.jpg" %(n), "a+b") as out:
				out.writelines(SBS)
				for x in split:
					out.write(chr(int(x)))
				out.writelines(EBS)
			n+=1
	imgfile.close()
