#!/usr/bin/env python
import codecs
import itertools
import sys
import distance


def similar(strings, distance_threshold=1):
	return [(c1, c2) for (c1, c2) in itertools.combinations(strings, 2) if distance.levenshtein(c1, c2) <= distance_threshold]

def main(args):
	if len(args) > 0:
		th = int(args[0])
	else:
		th = 1
	lines = [l.strip().decode("utf-8") for l in sys.stdin.readlines()]
	dups = similar(lines, th)
	w = codecs.getwriter('utf-8')(sys.stdout)
	for (s1, s2) in sorted(dups):
		w.write (u"%s|%s\n" % (s1,s2))
		w.flush()

if __name__ == '__main__':
	main(sys.argv[1:])
