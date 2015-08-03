#!/usr/bin/python

import os
import sys

from openpyxl import *
import json


def sheet2dict(sheet):
    headers = [cell.value for cell in sheet.rows[0]]
    d = [{k : v.value for (k, v) in zip(headers, row) if v.value is not None} for row in sheet.rows[1:]]
    return d

def main(args):
    filename = args[0]
    wb = load_workbook(filename=filename)
    d = sheet2dict(wb.active)
    json.dump(d, sys.stdout, sort_keys=True, indent=2, ensure_ascii=False)



if __name__ == '__main__':
	main(sys.argv[1:])
