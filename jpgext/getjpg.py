#!/usr/bin/python

import argparse
import jpgext as jpg

parser = argparse.ArgumentParser()
parser.add_argument("file", help="Input filename.")
parser.add_argument("--count", help="Maximum number of images to extract.", type=int)
args = parser.parse_args()

if not args.count:
	args.count = -1

jpg.extract_images(args.file, args.count)
