#!/usr/bin/env python
import sys
import json
import codecs


def main(args):
	field = args[0]
	array = json.load(sys.stdin)
	s = {unicode(e[field]) for e in array}
	w = codecs.getwriter('utf-8')(sys.stdout)
	for e in sorted(s):
		w.write(e + u"\n")
	w.flush()


if __name__ == '__main__':
	main(sys.argv[1:])
