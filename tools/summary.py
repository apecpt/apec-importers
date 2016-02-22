#!/usr/bin/env python3


import sys
import os
import json


array = json.load(sys.stdin)


for d in array:
	print("%s - %s" % (d['title'], d['author']))

print("length: %d" % len(array))