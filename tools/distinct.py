#!/usr/bin/env python
import sys
import json


def main(args):
	field = args[0]
	array = json.load(sys.stdin)
	s = {e[field] for e in array}
	for e in sorted(s):
		print e


if __name__ == '__main__':
	main(sys.argv[1:])
