#!/usr/bin/env python
import sys
import json
import codecs
import collections


def main(args):
	field = args[0]
	array = json.load(sys.stdin)
	s = [unicode(e[field]) for e in array]
	s = [(item, count) for item, count in collections.Counter(s).items() if count > 1]
	w = codecs.getwriter('utf-8')(sys.stdout)
	for item, count in sorted(s):
		w.write(u"%d - %s\n" % (count, item))
	w.flush()


if __name__ == '__main__':
	main(sys.argv[1:])
