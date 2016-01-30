#!/usr/bin/python3
# -*- coding: utf-8 -*-

import itertools
import os
import sys

from openpyxl import *
import json
import distance


header_keys = {
	u'autor' : u'author',
	u'classificação' : u'category',
	u'título' : 'title',
	u'observações' : u'notes',
	u'estado da obra' : u'status',
	u'idioma' : u'language',
	u'formato' : u'content-type'
}

def lower(x): return x.lower()
def guess_content_type(ext):
	import mimetypes
	type, encoding = mimetypes.guess_type("file.%s" %ext.lower())
	if type is None:
		raise RuntimeError("type not known for %s" % ext)
	return type

key_processors = {x : lower for x in [u'status', u'language', u'category']}
#key_processors['title'] = unicode
key_processors['content-type'] = guess_content_type

def process_dict(d):
	# bad code
	r = {}
	for k, v in d.items():
		f = key_processors.get(k, lambda x : x)
		r[k] = f(v)
	return r

def sheet2dict(sheet):
    headers = [cell.value for cell in sheet.rows[0]]
    d = [{header_keys[k.lower()] : v.value for (k, v) in zip(headers, row) if k is not None and v.value is not None} for row in sheet.rows[1:]]
    return [process_dict(i) for i in d]


def by_key(d, key):
    l = {i[key] for i in d}
    return sorted(l)

def print_authors(d):
    for author in by_key(d, 'autor'):
        print(author)
    
def print_categories(d):
    for c in by_key(d, u'classificação'):
       print(c)

distance_treshold = 1

def similar(l):
	return ((c1, c2) for (c1, c2) in itertools.combinations(l, 2) if distance.levenshtein(c1, c2) <= distance_treshold)

def problematic_categories(d):
	for c1, c2 in similar(by_key(d, u'classificação')):
		print("%s --> %s" % (c1, c2))

def main(args):
    filename = args[0]
    wb = load_workbook(filename=filename)
    d = sheet2dict(wb.active)
    json.dump(d, sys.stdout, sort_keys=True, indent=2, ensure_ascii=True)

if __name__ == '__main__':
	main(sys.argv[1:])
