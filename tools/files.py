#!/usr/bin/env python3

import json
import os
import sys


def normalize_data(name):
	import unicodedata
	return unicodedata.normalize('NFD', name).lower()

def filename(js):
	try:
		filename = ("%s - %s.%s" % (js['title'].strip(), js['author'].strip(), js['extension'].strip()))
		return normalize_data(filename)
	except KeyError:
		print(js)
		raise

directory = sys.argv[1]
files = [normalize_data(f) for f in os.listdir(directory) if f not in ('.', '..')]
array = json.load(sys.stdin)

found = []
for d in array:
	if filename(d) not in files:
		found.append(d)

json.dump(found, sys.stdout, indent=True)