#!/usr/bin/python
# -*- coding: utf-8 -*-

import itertools
import os
import sys

from openpyxl import *
import json
import distance


def sheet2dict(sheet):
    headers = [cell.value for cell in sheet.rows[0]]
    d = [{k.lower() : v.value for (k, v) in zip(headers, row) if k is not None and v.value is not None} for row in sheet.rows[1:]]
    return d


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

def problematic_categories(d):
	cs = by_key(d,u'classificação')
	for c1, c2 in itertools.combinations(cs, 2):
		if distance.levenshtein(c1, c2) <= distance_treshold:
			print "%s --> %s" % (c1, c2)

def main(args):
    command = args[0]
    filename = args[1]
    wb = load_workbook(filename=filename)
    d = sheet2dict(wb.active)
    if command == "json":
        json.dump(d, sys.stdout, sort_keys=True, indent=2, ensure_ascii=False)
    elif command =="authors":
    	print_authors(d)
    elif command == "categories":
    	print_categories(d)
    	problematic_categories(d)




if __name__ == '__main__':
	main(sys.argv[1:])
